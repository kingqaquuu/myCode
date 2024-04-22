class Student():
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


def main():
    student = input("请输入学生信息：姓名 年龄 电话号码，以空格分隔：")
    student = student.split(" ")
    stu1 = Student(student[0], student[1], student[2])
    print("学生信息：姓名：%s 年龄：%s 电话：%s" % (stu1.name, stu1.age, stu1.tel))


if __name__ == "__main__":
    main()
