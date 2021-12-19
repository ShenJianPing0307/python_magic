import heapq

def bubble(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    """
    j=0
    [2, 6, 1, 7, 4, 5]
    j=1
    [2, 1, 6, 7, 4, 5]
    ...
    """




def main():
    li = [6, 2, 1, 7, 4, 5]
    # sort方法
    # li.sort()
    # print("最小元素",li[0], "最大元素",li[len(li)-1])

    # sorted
    # li = sorted(li)
    # print("最小元素", li[0], "最大元素", li[len(li) - 1])

    # heapq
    # print("最小元素", heapq.nsmallest(1,li), "最大元素", heapq.nlargest(1,li))

    # 冒泡排序
    bubble(li)
    print(li)
    print("最小元素", li[0], "最大元素",li[len(li)-1])



if __name__ == '__main__':
    main()
