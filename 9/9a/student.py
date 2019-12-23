class Student:
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Marks:' ,self.marks)

    def accept(self):
        self.name=(input('Enter name'))
        self.age=int(input('Enter age'))
        for i in range(3):
            self.marks.append(int(input('Enter marks')))
        
o1=Student("Manish",25,[91,82,78])
o1.display()
o2=Student("Rajesh",28,[95,81,72])
o2.display()
o3=Student(" ",0,[])
o3.accept()
o3.display()
