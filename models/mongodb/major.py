
from mongoengine import *

from models.mongodb import BaseModel


class Majors(Document, BaseModel):
    major_id = StringField()
    major_name = StringField()
    department_id = StringField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

        self.collection_name = 'majors'

    def serialize(self):
        return {
            'major_id': self.major_id,
            'major_name': self.major_name,
            'department_id': self.department_id
        }
