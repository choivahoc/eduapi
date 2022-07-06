from peewee import *

from helpers.utils import MySQL
from playhouse.db_url import connect, schemes
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import RetryOperationalError


class MyRetryDB(RetryOperationalError, PooledMySQLDatabase):
    pass


schemes['mysql+pool+retry'] = MyRetryDB

db = connect(MySQL.URI_SQL, use_unicode=True, charset='utf8mb4')

schemes['mysql+pool+retry'] = MyRetryDB


# **************Models***********************
class BaseModel(Model):
    class Meta:
        database = db
