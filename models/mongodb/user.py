from mongoengine import *

from models.mongodb import BaseModel


class Users(Document, BaseModel):
    user_id = StringField()
    role_user = StringField()
    full_name = StringField()
    avatar = StringField()
    user_name = StringField()
    email = StringField()
    password = StringField()
    profile = StringField()
    created_time = IntField()
    updated_time = IntField()
    citizen_identity_card = DictField()
    school = ListField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

        self.collection_name = 'users'

    def serialize(self):
        return {
            'user_id': self.user_id,
            'role_user': self.role_user,
            'full_name': self.full_name,
            'avatar': self.avatar,
            'email': self.email,
            'password': self.password,
            'profile': self.profile,
            'created_time': self.created_time,
            'updated_time': self.updated_time,
            'citizen_identity_card': self.citizen_identity_card,
            'school': self.school
        }

    def create_account(self, data_user):
        try:
            print('Users::create_user():data_user: %s' % str(data_user))
            self.insert(data_user)
        except Exception as e:
            print('Users::create_user():message error: %s' % str(e))

    def delete_user(self, user_id):
        try:
            print('Users::delete_user():data_user: %s' % str(user_id))
            search_option = {
                'user_id': user_id
            }
            self.delete_one(search_option)
        except Exception as e:
            print('Users::delete_user():message error: %s' % str(e))

    def update_user(self, data_user, user_id):
        try:
            print('Users::update_user():data_user: %s' % str(data_user))
            search_option = {
                'user_id': user_id
            }
            self.upsert(search_option, data_user)
        except Exception as e:
            print('Users::update_user():message error: %s' % str(e))

    def list_user(self, search_option):
        try:
            return self.find(search_option)
        except Exception as e:
            print('Users::list_all_user():message error: %s' % str(e))

    def get_user(self, user_id):
        try:
            search_option = {
                'user_id': user_id
            }
            return self.find_one(search_option)
        except Exception as e:
            print('Users::list_all_user():message error: %s' % str(e))
