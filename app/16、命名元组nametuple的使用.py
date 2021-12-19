from collections import namedtuple

def main():
    # student = ["zhangsan", 25]

    Student = namedtuple("Student", ["name", "age"])

    student = Student("zhangsan", 25)

    # 元组的特性
    print(student[0], student[1])

    name, age = student
    print(name, age)

    # 属性取值
    print(student.name, student.age)

    # 修改值
    student.name = "lisi"
    print(student.name, student.age)



if __name__ == '__main__':
    main()