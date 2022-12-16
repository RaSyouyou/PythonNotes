class Man:
    def eat(self):
        print('吃饭')

class Chinese(Man):
    def eat(self):
        print('用筷子吃饭')


class English(Man):
    def eat(self):
        print('用叉子吃饭')

class Indian(Man):
    def eat(self):
        print('用手吃饭')

def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print('吃饭不能')

manEat(Chinese())