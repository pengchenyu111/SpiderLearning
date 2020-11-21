import csv

with open('files/data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['产品ID', '产品名称', '生产企业', '价格'])
    writer.writerow(['0001', 'iPhone9', 'Apple', 9999])
    writer.writerow(['0002', '特斯拉', '特斯拉', 12345])
    writer.writerow(['0003', '荣耀手机', '华为', 3456])
# 修改字段分隔符
with open('files/data1.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['产品ID', '产品名称', '生产企业', '价格'])
    writer.writerow(['0001', 'iPhone9', 'Apple', 9999])
    writer.writerow(['0002', '特斯拉', '特斯拉', 12345])
    writer.writerow(['0003', '荣耀手机', '华为', 3456])

# 一次性写入多行
with open('files/data2.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['产品ID', '产品名称', '生产企业', '价格'])
    writer.writerows([['0001', 'iPhone9', 'Apple', 9999],
                      ['0002', '特斯拉', '特斯拉', 12345],
                      ['0003', '荣耀手机', '华为', 3456]])

# 写入字典形式的数据，注意字典的key一定要和fieldnames中一致，否则会抛异常
with open('files/data3.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['产品ID', '产品名称', '生产企业', '价格']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'产品ID': '0001', '产品名称': 'iPhone9', '生产企业': 'Apple', '价格': 9999})
    writer.writerow({'产品ID': '0002', '产品名称': '特斯拉', '生产企业': '特斯拉', '价格': 12345})
    writer.writerow({'产品ID': '0003', '产品名称': '荣耀手机', '生产企业': '华为', '价格': 3456})

# 追加数据
with open('files/data.csv', 'a', encoding='utf-8') as f:
    fieldnames = ['产品ID', '产品名称', '生产企业', '价格']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow({'产品ID': '0004', '产品名称': '量子战衣', '生产企业': '斯塔克工业', '价格': 99999999999})
