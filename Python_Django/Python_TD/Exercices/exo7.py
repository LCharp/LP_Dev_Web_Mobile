class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    
class P2:
    def __init__(self,x):
        self.setX(x)

    def getX(self):
        return self.__reduce_ex__
    def setX(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else: 
            self.__x = x
    x = property(getX, setX)

print (P.__doc__)
p1=P(2000)
print(p1.x)
p1.x = 500
print(p1.x)
p1.x=-12
print(p1.x)

print (P2.__doc__)
p1=P2(2000)
print(p1.x)
p1.x=500
print(p1.x)
p1.x=-12
print(p1.x)

print (p1.__dict__['_P2__x'])
print(p1._P2__x)

print(p1.__x)
