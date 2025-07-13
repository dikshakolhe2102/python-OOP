#class variable:1) A class variable is a variable that is shared among all instances of a class.
                #  2) It is defined within the class and outside any instance methods.
                #  3) Class variables are accessed using the class name or an instance of the class.
                #  4) They are typically used to store data that is common to all instances.
# class variable is the value of all the methods are same
##declaration of class variable
#using object name condition(if same name of instance variable and class variable
# then interpreter 1st preference is instance variable)
class Demo():
    x=1                        #within the class
    def __init__(self):
        Demo.y=2               #using class name in constructor
    def f1(self):
        Demo.z=3               #using class name in function
d=Demo()
Demo.a=10                       #using class name 
print(Demo.__dict__)            


class Demo():
    x=1                        #within the class
    def __init__(self):
        Demo.y=2               #using class name in constructor
        print(Demo.y)          #access using class name
    def f1(self): 
        Demo.z=3               #using class name in function
        print(Demo.z)          #access using class name
        print(Demo.x)          #access using class name
d=Demo()
d.f1()
Demo.a=10                       #using class name 
print(Demo.a)                   #access using class name



class demo:
    x=1                          #class variable
    def __init__(self,p):
        self.a=p                  #instance variable

d=demo(10)
demo.x=100
print(d.__dict__)
print(demo.__dict__)
d1=demo(20)
print(d1.__dict__)
print(demo.__dict__)


#  Instance Variable :If the value of a variable varies from object to object, then such variables are called instance variables.
#                      For every object, a separate copy of the instance variable will be created.
                #      Instance variables are used within the instance method.
                # We can access the instance variable using the object and dot (.) operator.

# Create Instance Variables
class Student:
    pass
s1 = Student()
s1.name="ABC"
s1.age=3
# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)


# create second object
s2= Student()
s1.name="pqr"
s1.age=5

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)

#Example of instance variable with method
class Employee:
    def setdata(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age :",self.age)

#create object of employee
emp1=Employee()
emp1.setdata("ABC",25)
emp1.display()
print(emp1.__dict__)

#create 2nd object of employee
emp2=Employee()
emp2.setdata("PQR",30)
emp2.salary=50000
emp2.display()
print(emp2.__dict__)