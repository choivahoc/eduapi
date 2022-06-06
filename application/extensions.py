from helpers.action_logger import ActionLogger
from simplekv.memory import DictStore
from flask_kvsession import KVSessionExtension
from webargs.flaskparser import FlaskParser
from flask_sqlalchemy import SQLAlchemy

action_logger = ActionLogger()
db = SQLAlchemy()
parser = FlaskParser()
store = DictStore()
kvsession = KVSessionExtension(store)
