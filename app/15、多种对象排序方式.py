def sortFunc(item):
    return item[1]


def main():
    """sort方法"""
    # l1 = [2, 5, 7, 1, 3]
    # l1.sort()
    # print(l1)

    l2 = [("苹果", 10), ("香蕉", 5), ("梨子", 15)]
    l2.sort(key=sortFunc)
    print(l2)


def main1():
    """sorted方法"""
    l2 = [("苹果", 10), ("香蕉", 5), ("梨子", 15)]
    res = sorted(l2, key=lambda x:x[1])
    print(res)

import operator

class Person:

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __repr__(self):
        return "Person({}, {})".format(self.username, self.age)

def main2():
    """operator.attrgetter"""
    l3 = [Person("zhangsan", 20), Person("lisi", 15), Person("wuwang", 16)]
    # res = sorted(l3, key=lambda x:x.age)
    # print(res)

    res = sorted(l3, key=operator.attrgetter("age", "username"))
    print(res)






if __name__ == '__main__':
    main2()
