import itertools
import operator


def main():
    students = [
        {'gender': 'male', 'age': 12},
        {'gender': 'female', 'age': 13},
        {'gender': 'male', 'age': 15},
        {'gender': 'male', 'age': 12},
        {'gender': 'female', 'age': 16},
        {'gender': 'male', 'age': 12},
        {'gender': 'female', 'age': 15},
    ]

    students.sort(key=operator.itemgetter("age"))

    # print(students)

    res = itertools.groupby(students, key=operator.itemgetter("age"))
    # print(list(res))

    for age, item in res:
        # print(age, list(item))
        print("{}岁的人数有{}".format(age, len(list(item))))


if __name__ == '__main__':
    main()
