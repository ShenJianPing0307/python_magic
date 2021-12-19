from itertools import permutations
def main():
    a = [1, 2, 3]
    result = []
    for i in a:
        for j in a:
            for k in a:
                if len(set((i, j ,k))) == 3:
                    result.append((i, j, k))
    print(result)

def main2():
    a = [1, 2, 3]
    res = permutations(a)
    print(list(res))

if __name__ == '__main__':
    main2()