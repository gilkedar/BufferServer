import asyncio
from threading import Lock
import uuid
from cerberus import Validator
import threading
import logging
from queue import Queue

from utils.transaction_order_schema import transaction_schema
from utils.execution_sdk import ExecutionSdk
from utils import config
from utils.error import ErrorInvalidInput, ErrorCallingExecutionServer
from utils.order import Order


logging.basicConfig(level=logging.INFO, format=config.LOG_FORMAT)
logger = logging.getLogger()

# condition_var = asyncio.Condition()


class TransactionsManager:

    def __init__(self, batch_size):
        self.batch_size = batch_size

        self.responses = dict()
        self.responses_lock = Lock()

        # self.queue = asyncio.Queue(maxsize=0)
        self.queue = Queue()  # no need to set max size unless limited by resources
        self.queue_lock = Lock()

        self.execute_lock = Lock()
        self.is_executing = False

    @staticmethod
    def generate_request_id():
        request_id = str(uuid.uuid4())
        return request_id

    @staticmethod
    def create_new_order(request_params):  # can use factory if there are more objects to create
        return Order(request_params)

    @staticmethod
    def validate_request(request_params):
        v = Validator(transaction_schema)
        if not v.validate(request_params):
            raise ErrorInvalidInput(v.errors)

    async def handle_new_request(self, request_params):

        request_id = self.generate_request_id()

        logger.info(f"handling new request - {request_id}")

        TransactionsManager.validate_request(request_params)

        transaction_item = TransactionsManager.create_new_order(request_params)

        self.enqueue_order(request_id, transaction_item)

        if self.is_queue_ready():
            threading.Thread(target=asyncio.run, args=(self.execute(),)).start()

            #  Alternative with condition variable to eliminate the polling routine

            # async with condition_var:
            #     logger.info("Notifying all waiting reqeusts...")
            #     condition_var.notify_all()

        # res = await self.wait_for_response_condition(request_id)
        res = await self.wait_for_response_polling(request_id)

        return res

    def enqueue_order(self, request_id, item):
        with self.queue_lock:
            self.queue.put((request_id, item))

    def dequeue_item(self):
        with self.queue_lock:
            item = self.queue.get()
        return item

    def add_response(self, request_id, item):
        with self.responses_lock:
            self.responses[request_id] = item

    def get_response(self, request_id):
        with self.responses_lock:
            ans = self.responses.get(request_id)
        return ans

    def is_response_ready(self, request_id):
        ans = request_id in self.responses
        logger.info(f"is response ready for '{request_id}' - {ans}")
        return ans

    def is_queue_ready(self):
        ans = False
        if self.queue.qsize() >= self.batch_size and not self.is_executing:
            ans = True
        logger.info(f"checking if queue is ready to execute - {ans}")

        return ans

    async def wait_for_response_polling(self, request_id):
        while True:
            logger.info("polling wait for response...")  # need to add timeout
            if self.is_response_ready(request_id):
                item = self.get_response(request_id)
                return item
            else:
                await asyncio.sleep(1)  # polling, need to change to condition variable

    # async def wait_for_response_condition(self, request_id):
    #     while True:
    #         logger.info(f"in wait for response condition loop - {request_id}")
    #         if self.is_response_ready(request_id):
    #             return self.responses.get(request_id)
    #         else:
    #             async with condition_var:
    #                 logger.info(f"going to sleep until response is ready - {request_id}")
    #                 # await self.condition.wait_for(lambda: self.is_response_ready(request_id))
    #                 await condition_var.wait()
    #                 logger.info(f"waking up - {request_id}")

    async def execute(self):
        with self.execute_lock:
            self.is_executing = True
            logger.info("sending batch to execution sdk...")
            orders = [self.dequeue_item() for _ in range(self.batch_size)]
            ids, order_items = zip(*orders)
            encoded_orders = [item.to_json() for item in order_items]
            results = await ExecutionSdk.execute_orders(encoded_orders)
            if not results:
                raise ErrorCallingExecutionServer("Error calling execution sdk")
            for i, order_res in enumerate(results):  # assuming it comes back in the same order
                self.add_response(ids[i], order_res)
            logger.info("finished execution sdk")
            self.is_executing = False
