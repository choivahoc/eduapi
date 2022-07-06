from peewee import *

from models.mysql.basemodel import BaseModel


class lms_posts(BaseModel):
    class Meta:
        table_name = 'lms_posts'

    ID = IntegerField(primary_key=True)
    post_date = DateTimeField(128)
    post_content = CharField(1)
    post_title = CharField(4)
    post_name = CharField(11)
    post_type = CharField(128)

    def serialize(self):
        return {
            'id': self.ID,
            'post_date': self.post_date,
            # 'post_content': self.post_content,
            'post_title': self.post_title,
            'post_name': self.post_name,
            'post_type': self.post_type,
        }

    @staticmethod
    def get_post():
        try:
            posts = lms_posts.select().where(
                (lms_posts.post_type == 'stm-courses'))
            for post in posts:
                print(post.serialize())
        except Exception as e:
            print(e)
            print('Posts::test_get_post():message error:%s' % str(e))
            return None

    @staticmethod
    def get_description_post():
        try:
            posts = lms_posts.select().where(
                (lms_posts.post_title == 'Elasticsearch'))
            for post in posts:
                print(post.serialize())
        except Exception as e:
            print(e)
            print('Posts::test_get_post():message error:%s' % str(e))
            return None


if __name__ == '__main__':
    lms_posts().get_description_post()
