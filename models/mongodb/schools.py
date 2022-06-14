from mongoengine import *

from models.mongodb import BaseModel


class Schools(Document, BaseModel):
    school_id = StringField()
    school_name = StringField()
    level_count = StringField()
    school_type = IntField()
    is_active = StringField()
    created_time = DateTimeField()
    updated_time = StringField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

        self.collection_name = 'schools'

    def serialize(self):
        return {
            'school_id': self.school_id,
            'school_name': self.school_name,
            'level_count': self.level_count,
            'school_type': self.school_type,
            'is_active': self.is_active,
            'created_time': self.created_time,
            'updated_time': self.updated_time
        }

    def list_school(self, search_option):
        try:
            return self.find(search_option)
        except Exception as e:
            print('Users::list_all_user():message error: %s' % str(e))