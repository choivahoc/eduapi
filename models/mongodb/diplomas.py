from mongoengine import *

from models.mongodb import BaseModel


class Diplomas(Document, BaseModel):
    user_id = StringField()
    graduate_info = DictField()
    academic_ability = StringField()
    awarded_place = IntField()
    awarded_date = StringField()
    degree_awarder = DateTimeField()
    id_graduate_certification = StringField()
    graduate_certification_date = StringField()
    signature_header_master = StringField()
    signature_student = StringField()
    diplomas_image = StringField()
    transcript = ListField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

        self.collection_name = 'diplomas'

    def serialize(self):
        return {
            'user_id': self.user_id,  # id sinh viên
            'graduate_info': self.graduate_info,
            'academic_ability': self.academic_ability,  # học lực
            'awarded_place': self.awarded_place,  # nơi cấp bằng
            'awarded_date': self.awarded_date,  # ngày cấp bằng
            'degree_awarder': self.degree_awarder,  # thông tin người cấp
            'id_graduate_certification': self.id_graduate_certification,  # số hiệu bằng, mã bằng
            'graduate_certification_date': self.graduate_certification_date,  # Ngày quyết định cấp bằng
            'signature_header_master': self.signature_header_master,  # chữ kí hiệu trưởng
            'signature_student': self.signature_student,  # chữ kí sinh viên
            'diplomas_image': self.diplomas_image,  # ảnh bằng
            'transcript': self.transcript
        }

    def list_diplomas(self, search_option):
        try:
            return self.find(search_option)
        except Exception as e:
            print('Users::list_all_user():message error: %s' % str(e))