from utils import config


class Order:

    CMD_BUY = "BUY"
    CMD_SELL = "SELL"

    DOLLAR_CURRENCY = "DOLLAR"

    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_DECLINED = "declined"

    def __init__(self, request_params):
        self.cmd = request_params[config.FIELD_COMMAND_TYPE]
        self.amount = request_params[config.FIELD_AMOUNT]
        self.src = request_params[config.FIELD_SOURCE]
        self.dst = request_params[config.FIELD_DST]
        self.currency = request_params.get(config.FIELD_CURRENCY, Order.DOLLAR_CURRENCY)

        self.status = Order.STATUS_PENDING

        self.request_params = request_params

    def approve(self):
        self.status = self.STATUS_APPROVED

    def decline(self):
        self.status = self.STATUS_DECLINED

    def to_json(self):
        return self.request_params
