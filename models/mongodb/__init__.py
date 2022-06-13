from pymongo import MongoClient, ReadPreference

from helpers.utils import Mongo

db_name = Mongo.DB
mongo_client = MongoClient(Mongo.URI, connect=False)


class BaseModel:
    collection_name = ''

    def insert(self, dictionary):
        db = mongo_client[db_name]
        return db[self.collection_name].insert_one(dictionary)

    def upsert(self, search_option, dictionary):
        db = mongo_client[db_name]

        document = db[self.collection_name].find_one(search_option)
        if document:
            print('__init__::upsert():update:document: %s' % dictionary)
            document.update(dictionary)
            db[self.collection_name].replace_one(filter=search_option, replacement=document, upsert=True)
        else:
            print('__init__::upsert():insert:document: %s' % dictionary)
            db[self.collection_name].insert_one(dictionary)

    def find(self, search_option):
        db = mongo_client[db_name]

        return db.get_collection(self.collection_name, read_preference=ReadPreference.SECONDARY_PREFERRED).find(
            search_option)

    def find_all(self):
        db = mongo_client[db_name]
        return db.get_collection(self.collection_name, read_preference=ReadPreference.SECONDARY_PREFERRED).find()

    def find_specify_fields(self, search_option, fields):
        db = mongo_client[db_name]
        projection = dict(_id=0)  # Exclude ID
        for field in fields:
            projection[field] = 1
        return db.get_collection(self.collection_name, read_preference=ReadPreference.SECONDARY_PREFERRED).find(
            search_option, projection if len(fields) > 0 else None)

    def distinct(self, fields, query):
        db = mongo_client[db_name]

        if type(fields) is str:
            return db[self.collection_name].distinct(fields, query)

        return None

    def _aggregate(self, group, match: object, sort=None, count=None, project=None):
        db = mongo_client[db_name]
        pipeline = []
        if match:
            pipeline.append({"$match": match})
        pipeline.append({"$group": group})
        if sort:
            pipeline.append({"$sort": sort})
        if count:
            pipeline.append({"$count": count})
        if project:
            pipeline.append({"$project": project})
        print('__init__::_aggregate():pipeline: %s' % pipeline)
        return db[self.collection_name].aggregate(pipeline)

    def delete_many(self, delete_options):
        db = mongo_client[db_name]
        db[self.collection_name].delete_many(delete_options)

    def update_one(self, search_option, dictionary):
        db = mongo_client[db_name]

        document = db[self.collection_name].find_one(search_option)
        if document:
            print('__init__::update_one():update:document: %s' % dictionary)
            document.update(dictionary)
            db[self.collection_name].replace_one(filter=search_option, replacement=document, upsert=False)

    def insert_document(self, dictionary):
        db = mongo_client[db_name]
        print('__init__::insert_document():insert:document: %s' % dictionary)
        db[self.collection_name].insert_one(dictionary)

    def update_many(self, filter_option, update_option):
        db = mongo_client[db_name]
        db[self.collection_name].update_many(filter_option, update_option)

    def insert_many(self, document):
        db = mongo_client[db_name]
        db[self.collection_name].insert_many(document)

    def find_one(self, search_options):
        db = mongo_client[db_name]
        return db[self.collection_name].find_one(search_options)

    def delete_one(self, delete_options):
        db = mongo_client[db_name]
        db[self.collection_name].delete_one(delete_options)

    def count_by_query(self, count_option):
        db = mongo_client[db_name]
        return db[self.collection_name].count(count_option)

    def update_one_row(self, filter_option, update_option):
        db = mongo_client[db_name]
        print('__init__::update_one_row():update:document: %s' % update_option)
        db[self.collection_name].update_one(filter_option, update_option)

    def update_or_insert(self, search_option, dictionary, fields=None):
        db = mongo_client[db_name]
        document = db[self.collection_name].find_one(search_option)
        if document:
            print('__init__::upsert():update:document: %s' % dictionary)
            update_objects = dict()
            for field in fields:
                if field in dictionary:
                    update_objects[field] = dictionary[field]
            print("update_or_insert::update_objects {}".format(update_objects))
            db[self.collection_name].update_one(
                {
                    "_id": document["_id"]
                },
                {
                    "$set": update_objects
                }
            )
        else:
            print('__init__::upsert():insert:document: %s' % dictionary)
            db[self.collection_name].insert_one(dictionary)

    def aggregate_data(self, pipeline):
        db = mongo_client[db_name]
        print('__init__::aggregate_data():pipeline: %s' % pipeline)
        return db[self.collection_name].aggregate(pipeline)
