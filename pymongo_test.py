from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class TestMongo(object):
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['blog']

    def add_one(self):
        """ 新增数据 """
        post = {
            'title': '标题',
            'x': 1,
            'content': '博客内容，……',
            'created_at': datetime.now()
        }
        return self.db.blog.posts.insert_one(post)

    def get_one(self):
        """ 查询一条数据 """
        return self.db.blog.posts.find_one()

    def get_more(self):
        """ 查询多条数据 """
        return self.db.blog.posts.find({'x': 2})

    def get_one_from_oid(self, oid):
        """ 查询指定ID的数据 """
        obj = ObjectId(oid)
        return self.db.blog.posts.find_one({'_id': obj})

    def update(self):
        """ 修改数据 """
        # 修改一条数据
        # rest = self.db.blog.posts.update_one({'x': 11}, {'$inc': {'x': 10}})
        # return rest
        # 修改多条数据
        rest = self.db.blog.posts.update_many({}, {'$inc': {'x': 10}})
        return rest

    def delete(self):
        """ 删除数据 """
        # 删除一条数据
        # return self.db.blog.posts.delete_one({'x': 12})
        # 删除多条数据
        return self.db.blog.posts.delete_many({'x': 12})


def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest.inserted_id)

    # rest = obj.add_one()
    # print(rest['_id'])

    # rest = obj.get_more()
    # for item in rest:
    #     print(item['_id'])

    # rest = obj.get_one_from_oid('5bfb8721dc4693b4c182c3a7')
    # print(rest)

    # rest = obj.update()
    # print(rest.matched_count)
    # print(rest.modified_count)

    rest = obj.delete()
    print(rest.deleted_count)


if __name__ == '__main__':
    main()
