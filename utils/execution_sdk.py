import logging

from utils import config
from utils.order import Order
import time

logging.basicConfig(level=logging.INFO, format=config.LOG_FORMAT)
logger = logging.getLogger()


class ExecutionSdk:

    @staticmethod
    async def execute_orders(orders: list):
        """
        take decoded order json and create generic order item 'Order', and approve/decline the order,
        then encode back to json to easily transport the item
        :param orders:
        :return:
        """
        try:
            logger.info("in execute_orders sdk call")
            order_objects = list()
            for order_json in orders:
                order_object = Order(order_json)
                order_object.approve()
                order_objects.append(order_object.to_json())# create random function approve/decline to test
            time.sleep(4)  # simulate remote api overhead
            logger.info('sdk call executed successfully...')
            return order_objects
        except Exception as ex:
            logger.exception(ex)
            return None
    # @staticmethod
    # def _approve_order(order):
    #     order[config.FIELD_STATUS] = Order.STATUS_APPROVED
    #
    # @staticmethod
    # def _decline_order(order):
    #     order[config.FIELD_STATUS] = Order.STATUS_DECLINED
