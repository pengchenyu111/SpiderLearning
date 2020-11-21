import json


class Product:
    # 通过类的构造方法初始化3个属性
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


# 用于将Product类的实例转换为字典的函数
def product2Dict(obj):
    return {
        'name': obj.name,
        'price': obj.price,
        'count': obj.count
    }


# 创建Product类的实例
product = Product('特斯拉', 1000000, 20)
# 将Product类的实例转换为JSON字符串，ensure_ascii关键字参数的值设为True，
# 可以让返回的JSON字符串正常显示中文
jsonStr = json.dumps(product, default=product2Dict, ensure_ascii=False)
print(jsonStr)
