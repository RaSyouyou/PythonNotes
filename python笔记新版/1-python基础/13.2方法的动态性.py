#python的方法没有重载
#在java中可以定义同名方法达到同名不同参数列表的目的
#同名方法谁在最后谁有效
class Person:
    count =0

    def __init__(self,n):
        Person.count +=1 #直接操作
        self.name = n
    def work(self):
        print(self.name,'said\'work,work!\'')

    def __del__(self):
        Person.count -=1



def play_game(s):
    print('{0}在玩游戏,名字是{1}'.format(s,s.name))

def work2(s):
    print(s.name,"something need doing?")

Person.play = play_game #把函数赋值给类
p1 = Person('huangxudong')
print(p1.name)
p1.work()
p1.play()
#重写
Person.work = work2
p1.work()

print(dir(p1))
print(p1.count)

p2 = Person('sunyifeng')
print(p2.count)
print(p1.count)
del(p1)
print(Person.count)

