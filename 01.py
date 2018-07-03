'''
定义一个学生类，用来形容学生
'''
#定义一个空类
class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass
#定义一个对象
mingyue = Student()
#在定义一个类，用来描述听python的学生
class PythonStudent():
    name = None
    age  = 18
    course = "Python"
    #1.def 是缩进层级
    #2 系统默认由一个self参数
    def doHomework(selfself):
        print("我在做作业")
        return None
#实例化一个叫月月的学生，是一个具体的人
yueyue  = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进去参数
yueyue.doHomework()



