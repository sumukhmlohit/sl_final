class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    
    def area(self):
        area=self.l*self.b
        print("Area of a rectangle is ",area)


l=int(input('Enter length'))
b=int(input('Enter breadth'))
ob=Rectangle(l,b)
ob.area()
