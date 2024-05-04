#1
class String1():
    def __init__(self):
        self.st = ""

    def getString(self):
        self.st = input()

    def printString(self):
        print(self.st.upper())

st = String1()
st.getString()
st.printString()

#2
class Shape(object):
    def __init__(self):
        pass
        
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.l = l

    def area(self):
        return self.l*self.l

aSquare= Square(3)
print (aSquare.area())



#3
class Shape(object):
    def __init__(self):
        pass
        
    def area(self):
        return 0

class Ractangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.l = l
        self.w = w

    def area(self):
        return self.l*self.w

aRactangle= Ractangle(3, 5)
print (aRactangle.area())



#4
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return "x is - {} \ny is - {}".format(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y
        return ""
    
    def dist(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2)**(1/2)
        print((self.x - x)**2)
        print((self.y - y)**2)
        return round(dist, 3)


p = Point(3, 5)
print(p.move(2, 4))
print(p.show())
print(p.dist(3, 5))





#5
class Account(object):
    def __init__(self, o, b):
        self.owner = o
        self.balance = int(b)

    def deposit(self, m):
        self.balance += m
        return self.balance

    def withdraw(self, m):
        if(m <= self.balance):
            self.balance -= m
            return self.balance
        else:
            print("Not can be overdown \nMax access: {}".format({self.balance}))
            return ""

Man = Account("Name", 50000)
print(Man.balance)
print(Man.deposit(100))
print(Man.withdraw(200))
print(Man.withdraw(100000))



#6
class onlyprime(object):
    def __init__(self, mylist):
        self.list = mylist
    
    def filter(self):
        prime = []
        for i in range(len(self.list)):
            temp = True
            for j in range(2, int(i)):
              if (int(i) % (j)) == 0:
                temp = False
                break      
            if temp:
              if i != 0 and i !=1:
                prime.append(i)
        return prime

a = [1, 2, 3, 4, 5, 6, 7, 8]
lis = onlyprime(a)
print(lis.filter())