#OOP
print("\n Example 1 \n")
class Lamp:
    def __init__(self, state): #constructor of class. self represents the current instance, and state is an input argument
        self.state = state

    def TurnOn(self):
        print("ON")
        self.state = True

    def TurnOff(self):
        print("OFF")
        self.state = False

    def IsTurned(self):
        print(self.state)
        return self.state

lamp1 = Lamp(True)
print("state of lamp1 after initializing = ",lamp1.IsTurned())
lamp1.TurnOff()
print("state of lamp1 after turning off = ",lamp1.IsTurned())


#basic class instantiation
print("\n Example 2 \n")

class MyClass:
    def __init__(self, i,j ):
        self.num1 = i
        self.num2=j
    def show(self):
        print(self.num1, self.num2)

obj = MyClass(3,2)
obj1 = MyClass(10,20)
obj.show()

print("\n Example 3 - Single Inheritance \n")
class ColorLamp(Lamp):
    def __init__(self, state, color):
        super().__init__(state)
        self.color = color
    def SetColor(self, new_color):
        self.color = new_color
    def GetColor(self):
        return self.color

c = ColorLamp(False,"Orange")
print("Color of lamp c = ", c.GetColor(), " and state = ", c.IsTurned())
c.SetColor("Red")
c.TurnOn()
print("New color of lamp c = ", c.GetColor(), " and state = ", c.IsTurned())

print("\n Example 4 - Multiple Inheritance \n")

class base1:
    def __init__(self,x):
        self.x =x
    def showx(self):
        print(self.x, '\n')

class base2:
    def __init__(self,y):
        self.y = y
    def showy(self):
        print(self.y, '\n')

class derived(base1, base2):
    def set(self, num1, num2):
        self.x = num1
        self.y = num2

obj1 = base1(100)
obj2 = base2(200)
#When you instantiate derived(1), Python looks for an __init__ method using its Method Resolution Order (MRO). 
# Because base1 is listed first in class derived(base1, base2):, 
# Python defaults to using base1.__init__.
obj3 = derived(1)
obj3.set(2,3)
obj3.showx()
obj3.showy()

print("\n Example 5 - Method Overriding \n")
class MyClass:
    def __init__(self, i, j):
        self.num1 = i
        self.num2 = j
    def show(self):
        print(self.num1, self.num2)
    
class Child(MyClass):
    def __init__(self, i):
        print("Child class")
        super().__init__(10, 20)
        self.k = i * 100
    def show(self):
        super().show()
        print(self.k)

obj = MyClass(1,2)
obj.show()

child = Child(8)
child.show()




        
