from application import create_app
from models import *

app = create_app()
app.app_context().push()
db.create_all()
