from pymongo import *

# 连接MongoDB数据库
Client = MongoClient()
# 打开或创建名为data的collection，collection相当于关系型数据库中的数据库
# 在MongoDB中，collection是文档的集合
db = Client.data
# 或者使用类似引用字典值的方式打开或创建collection
# db = Client['data']

# 定义要插入的文档（字典）
person1 = {"name": "Bill", "age": 55, "address": "地球", "salary": 1234.0}
person2 = {"name": "Mike", "age": 12, "address": "火星", "salary": 434.0}
person3 = {"name": "John", "age": 43, "address": "月球", "salary": 6543.0}
# 创建或打开一个名为persons的文档，persons相当于关系型数据库中的表
persons = db.persons
# 先删除persons文档中的所有数据，以免多次运行程序导致文档中有大量重复的数据
persons.delete_many({'age': {'$gt': 0}})

# 使用insert_one方法插入文档
personId1 = persons.insert_one(person1).inserted_id
personId2 = persons.insert_one(person2).inserted_id
personId3 = persons.insert_one(person3).inserted_id
print(personId3)
'''
也可以使用insert_many方法一次插入多个文档
personList = [person1,person2,person3]
result = persons.insert_many(personList)
print(result.inserted_ids)
'''
# 搜索persons文档中的第一条子文档，相当于关系型数据库中的记录
print(persons.find_one())
print(persons.find_one()['name'])
# 搜索所有数据
for person in persons.find():
    print(person)
print('--------------')
# 更新第1个满足条件的文档中的数据，使用update_many方法可以更新所有满足条件的文档
persons.update_one({'age': {'$lt': 50}}, {'$set': {'name': '超人'}})  #
# persons.delete_one({'age':{'$gt':0}})  # 只删除满足条件的第1个文档
# 搜索所有满足age小于50的文档
for person in persons.find({'age': {'$lt': 50}}):
    print(person)

print('--------------')
# 搜索所有满足age大于50的文档
for person in persons.find({'age': {'$gt': 50}}):
    print(person)
# 输出persons中的文档总数
print('总数', '=', persons.count())
