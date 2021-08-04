from flask import Flask, request, jsonify
import logging
import os
import asyncio
# from quart import Quart

from utils import config
from utils.error import ApplicationServerError
from utils.transactions_manager import TransactionsManager

logging.basicConfig(level=logging.INFO, format=config.LOG_FORMAT)
logger = logging.getLogger()

app = Flask(__name__)
# app = Quart(__name__)

MESSAGE_QUEUE_SIZE = os.environ.get('MESSAGE_QUEUE_SIZE', config.MESSAGE_QUEUE_SIZE)
PORT = os.environ.get('PORT', config.DEFAULT_PORT)

transaction_manager = TransactionsManager(batch_size=config.MESSAGE_QUEUE_SIZE)


@app.route(config.APP_SERVER_ENDPOINT, methods=['POST'])
def create_transaction():

    logger.info(f"\n\n-------------------------------------------------------------")

    try:
        request_params = request.get_json()
        coroutine = transaction_manager.handle_new_request(request_params)
        response = asyncio.run(coroutine)
        print(response)
    except ApplicationServerError as ex:
        logger.exception(ex)
        return jsonify(f"Application Server Error - {ex}"), 400
    except Exception as ex:
        return jsonify(f"Unknown Error - {ex}"), 401

    logger.info(f"**************************************************************")
    return jsonify(response), 200


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=PORT)

