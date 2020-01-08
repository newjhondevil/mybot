import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config

from heroku_config import Var

class Development(Var):
  APP_ID = 947802
  API_HASH = "17b1e55ff6633d8e88165cc92eab08a1"
