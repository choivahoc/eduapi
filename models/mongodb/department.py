
from mongoengine import *

from models.mongodb import BaseModel


class Departments(Document, BaseModel):
    department_id = StringField()
    department_name = StringField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

        self.collection_name = 'departments'

    def serialize(self):
        return {
            'department_id': self.department_id,
            'department_name': self.department_name
        }
