from utils import config

transaction_schema = {
  config.FIELD_COMMAND_TYPE: {
    "type": "string",
    "required": True,
  },
  config.FIELD_AMOUNT: {
    "type": "number",
    "required": True,
  },
  config.FIELD_SOURCE: {
        "type": "string",
        "required": True,
    },
  config.FIELD_DST: {
        "type": "string",
        "required": True,
    },
  config.FIELD_CURRENCY: {
        "type": "string",
        "required": False,
    }
}