import pymongo

class KasMongo:
    def __init__(self, username, password, cluster, db, collection):
        self.client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.jc8vxxk.mongodb.net/")
        self.db = self.client[db]
        self.collection = self.db[collection]

    def insert(self, key, value):
        """
        Добавляет документ с указанным ключом и значением в коллекцию.
        """
        data = {key: value}
        self.collection.insert_one(data)

    def find(self, key, value):
        """
        Ищет документ по указанному ключу и значению.
        """
        data = self.collection.find_one({key: value})
        return data

    def find_all(self, query=None):
        """
        Возвращает все документы, соответствующие запросу.
        Если запрос не указан, возвращаются все документы.
        """
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def update(self, key, old_value, new_value):
        """
        Обновляет значение указанного ключа с old_value на new_value.
        """
        self.collection.update_one({key: old_value}, {"$set": {key: new_value}})

    def delete(self, key, value):  
        """
        Удаляет один документ, соответствующий указанному ключу и значению.
        """
        self.collection.delete_one({key: value})

    def delete_many(self, query):
        """
        Удаляет все документы, соответствующие запросу.
        """
        self.collection.delete_many(query)

    def count_documents(self, query=None):
        """
        Возвращает количество документов, соответствующих запросу.
        Если запрос не указан, возвращает общее количество документов в коллекции.
        """
        if query is None:
            query = {}
        return self.collection.count_documents(query)

    def distinct(self, key):
        """
        Возвращает уникальные значения указанного ключа.
        """
        return self.collection.distinct(key)

    def aggregate(self, pipeline):
        """
        Выполняет агрегирующий запрос с использованием указанного конвейера.
        """
        return list(self.collection.aggregate(pipeline))

    def create_index(self, keys, **kwargs):
        """
        Создает индекс для указанного ключа или комбинации ключей.
        """
        return self.collection.create_index(keys, **kwargs)

    def list_indexes(self):
        """
        Возвращает список всех индексов в коллекции.
        """
        return list(self.collection.list_indexes())

    def drop_index(self, index_name):
        """
        Удаляет указанный индекс.
        """
        self.collection.drop_index(index_name)

    def drop_collection(self):
        """
        Удаляет всю коллекцию.
        """
        self.collection.drop()

    def close(self):
        """
        Закрывает соединение с MongoDB.
        """
        self.client.close()