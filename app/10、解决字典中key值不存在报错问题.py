def main():
    d = {"username": "zhangsan"}
    # print(d["age"])
    # 方式一
    print(d.get("age", None))  # 如果key不存在就返回None，根据返回值进行后期逻辑处理


import collections


def main1():
    """方式二"""
    d = collections.defaultdict(int)
    d['username'] = "zhangsan"
    print(d)
    print(d["age"])


if __name__ == '__main__':
    main1()
