from application import create_app
from models import *
from tests.test_db.fake_db_1 import init_db

app = create_app()
app.app_context().push()
db.create_all()
init_db(db)
