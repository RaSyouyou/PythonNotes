
class MySingleton:

    __obj = None

    def __new__(cls,*args,**kwargs):
        if cls.__obj ==None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self,name):
        self.name = name