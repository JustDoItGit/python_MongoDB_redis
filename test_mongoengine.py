from mongoengine import connect
from mongoengine import StringField
from mongoengine import IntField
from mongoengine import FloatField
from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField
from mongoengine import ListField
# from mongoengine import Document
from mongoengine import DynamicDocument

connect('students', host='127.0.0.1', port=27017)

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


class Grade(EmbeddedDocument):
    """ 成绩 """
    name = StringField(required=True)
    score = FloatField(required=True)


# class Student(Document):
class Student(DynamicDocument):
    """ 学生 """
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))
    # remark = StringField()

    meta = {
        'collection': 'students',
        # 'ordering': ['-age']
    }


class TestMongoEngine(object):
    @staticmethod
    def add_one():
        """ 添加一条数据到数据库 """
        yuwen = Grade(
            name='语文',
            score=90
        )
        shuxue = Grade(
            name='数学',
            score=100
        )
        stu_obj = Student(
            name='张三5',
            age=15,
            sex='male',
            grades=[yuwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    @staticmethod
    def get_one():
        """ 查询一条数据 """
        return Student.objects.first()

    @staticmethod
    def get_more():
        """ 查询多条数据 """
        return Student.objects.all()

    @staticmethod
    def get_from_oid(oid):
        """ 根据ID来获取数据 """
        return Student.objects.filter(pk=oid).first()

    @staticmethod
    def update():
        """ 修改数据 """
        # 修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)
        # 修改多条数据
        # return Student.objects.filter(sex='male').update(inc__age=10)

    @staticmethod
    def delete():
        """ 删除数据 """
        # 删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        # 删除多条数据
        return Student.objects.filter(sex='male').delete()


def main():
    obj = TestMongoEngine()
    rest = obj.add_one()
    print(rest.pk)
    print(rest.id)  # id 和 pk 一样

    # rest = obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rows = obj.get_more()
    # for row in rows:
    #     print(row.name)

    # rest = obj.get_from_oid('5bfcb68bc47c0ff7bea8e669')
    # if rest:
    #     print(rest.id)
    #     print(rest.name)

    # rest = obj.update()
    # print(rest)

    # rest = obj.delete()
    # print(rest)


if __name__ == '__main__':
    main()
