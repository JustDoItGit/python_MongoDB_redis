import redis


class Base:
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


class TestString(Base):
    def __init__(self):
        Base.__init__(self)

    def test_set(self):
        """ set -- 设置值 """
        rest = self.r.set('user2', 'Amy')
        print(rest)
        return rest

    def test_get(self):
        """ get -- 获取值 """
        rest = self.r.get('user3')
        print(rest)
        return rest

    def test_mset(self):
        """ mset -- 设置多个键值对 """
        d = {
            'user3': 'Bob',
            'user4': 'Bobx'
        }
        rest = self.r.mset(d)
        print(rest)
        return rest

    def test_mget(self):
        """ mget -- 获取多个键值对 """
        ls = ['user3', 'user4']
        rest = self.r.mget(ls)
        print(rest)
        return rest

    def test_del(self):
        """ del """
        rest = self.r.delete('user3')
        print(rest)
        return rest


class TestList(Base):
    def __init__(self):
        Base.__init__(self)

    def test_push(self):
        """ lpush/rpush -- 从左/右插入数据 """
        # t = ('Amy', 'Jhon')
        t = ['Amy', 'Jhon']
        rest = self.r.lpush('l_eat3', *t)
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

    def test_pop(self):
        """ lpop/rpop -- 移除最左/右的元素并返回 """
        rest = self.r.lpop('l_eat3')
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)


class TestSet(Base):
    def __init__(self):
        # super().__init__()
        Base.__init__(self)

    def test_sadd(self):
        """ sadd -- 添加/元素 """
        ls = ['Cat', 'Dog']
        rest = self.r.sadd('zoo3', *ls)
        print(rest)
        rest = self.r.smembers('zoo3')
        print(rest)

    def test_srem(self):
        """ srem -- 删除元素 """
        rest = self.r.srem('zoo2', 'Dog')
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_sinter(self):
        """ sinter -- 返回几个集合的交集 """
        rest = self.r.sinter('zoo2', 'zoo3')
        print(rest)

    def test_sunion(self):
        """ sunion -- 返回几个集合的交集 """
        rest = self.r.sunion('zoo1', 'zoo3')
        print(rest)


def main():
    # str_obj = TestString()
    # str_obj.test_set()
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    # str_obj.test_del()

    # list_obj = TestList()
    # # list_obj.test_push()
    # list_obj.test_pop()

    set_obj = TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    # set_obj.test_sinter()
    set_obj.test_sunion()


if __name__ == '__main__':
    main()
