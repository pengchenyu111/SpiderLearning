from pymysql import *
import json


# 打开MySQL数据库，其中127.0.0.1是MySQL服务器的IP，root是用户名，12345678是密码
# test是数据库名
def connectDB():
    db = connect("127.0.0.1", "root", "PCY90321", "pymysql", charset='utf8')
    return db


db = connectDB()


# 创建persons表
def createTable(db):
    # 获取Cursor对象
    cursor = db.cursor()
    sql = '''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);'''

    try:
        # 执行创建表的SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
    return False


# 向persons表插入4条记录
def insertRecords(db):
    cursor = db.cursor()
    try:
        # 首先将以前插入的记录全部删除
        cursor.execute('DELETE FROM persons')
        # 下面的几条语句向persons表中插入4条记录
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )");
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
              VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
        # 提交到数据库执行
        db.commit()
        return True
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
    return False


# 查询persons表中全部的记录，并按age字段降序排列
def selectRecords(db):
    cursor = db.cursor()
    sql = 'SELECT name,age,salary FROM persons ORDER BY age DESC'
    cursor.execute(sql)
    # 调用fetchall方法获取全部的记录
    results = cursor.fetchall()
    # 输出查询结果
    print(results)
    # 下面的代码将查询结果重新组织成其他形式
    fields = ['name', 'age', 'salary']
    records = []
    for row in results:
        records.append(dict(zip(fields, row)))
    return json.dumps(records)


if createTable(db):
    print('成功创建persons表')
else:
    print('persons表已经存在')

if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')
print(selectRecords(db))
db.close()
