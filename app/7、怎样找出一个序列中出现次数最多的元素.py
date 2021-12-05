
def main():
    """方式一"""
    l1 = [1, 2, 15, 5, 1, 2, 3]
    """
    key: 元素
    value: 元素出现的次数
    {1:2, 2:2，...}
    """
    d_count = {}
    for i in l1:
        d_count[i] = d_count.get(i, 0) + 1
    print(d_count)

    """
    d_count.items() = [(1,2),(2,2)...]
    """
    d = sorted(d_count.items(), key=lambda x:x[1], reverse=True)
    print(d[0])

from collections import Counter

def main1():
    """方式二"""
    l1 = [1, 2, 15, 5, 1, 2, 3]
    d_count = Counter(l1)
    print(d_count)
    top = d_count.most_common(1)
    print(top)

if __name__ == '__main__':
    main1()