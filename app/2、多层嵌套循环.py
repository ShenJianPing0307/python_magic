from itertools import product

def main():
    # for i in range(1, 5):
    #     for j in range(1, 5):
    #         for z in range(1, 5):
    #             print(i, j ,z)

    for i, j, z in product(range(1, 5), (1, 5), (1, 5)):
        print(i, j, z)


if __name__ == '__main__':
    main()