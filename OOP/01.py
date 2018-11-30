# 定义一个学生类，用来形容学生
# 定义一个空的类

class Student():
    # 一个空类,pass 代表直接跳过，此处pass不能省略
    pass

# 定义一个对象

mingyue = Student()

# 定义一个雷，用来描述听Python的学生

class PythonStudent():

    # 用None给不确定的赋值
    name = None
    age = 18
    course = "Python"

    # def 需要注意缩进的层级
    # 系统默认由一个self参数
    def doHomework(self):
        print("I'm doing my homework")

        # 推荐在函数末尾使用return 语句


# 实例化一个叫yueyue的学生，具体是一个人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()

