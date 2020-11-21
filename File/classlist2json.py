import json


class Product:
    def __init__(self, d):
        self.__dict__ = d


f = open('files/products.json', 'r', encoding='utf-8')
jsonStr = f.read()
# 将JSON字符串转换为Product对象列表
products = json.loads(jsonStr, object_hook=Product)
# 输出Product对象列表中所有Product对象的相关属性值
for product in products:
    print('name', '=', product.name)
    print('price', '=', product.price)
    print('count', '=', product.count)
f.close()


# 定义将Product对象转换为字典的函数
def product2Dict(product):
    return {
        'name': product.name,
        'price': product.price,
        'count': product.count
    }


# 将Product对象列表转换为JSON字符串
jsonStr = json.dumps(products, default=product2Dict, ensure_ascii=False)
print(jsonStr)
