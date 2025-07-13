# class A:
#     def f1(self):
#         print("Base Class")

# class B(A):
#     def child(self):
#         print("Derived Class")

# b=B()
# b.f1()
# b.child()

from datetime import datetime
class person:
    def properties(self):
        self.name='Diksha'
        self.dob='2007/2/21'
    def calaculate(self):
        current_date = datetime.today()
        print(current_date)
        y,m,d=map(int,self.dob.split('/'))
        self.dob=datetime(y,m,d)
        self.age=current_date.year-self.dob.year
        return self.age

class voter(person):
    def is_eligible(self):
        if(self.calaculate() > 18):
            print("Voter is eligible")
        else:
            print("Not eligible")
    def display(self):
        print(self.name)
        print(self.dob)
        print(self.age)


d=voter()
d.properties()
d.is_eligible()
d.display()

#example with constructor and destructor in inheritance
# class Base:
#     def __init__(self):
#         print("Base")

#     def __del__(self):
#         print("Destructor")

# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Derived")
#     def __del__(self):
#         super().__del__()
#         print("Destructor")
# d=Derived()


#example of method overridding
# class A:
#     def f1(self):
#         print("Base class")

# class B(A):
#     def f1(self):
#         super().f1()
#         print("derived class")
# obj=B()
# obj.f1()


#constructor with parameter
# class A:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name}")
    
# class B(A):
#     def __init__(self,name,age):
#         A.__init__(self,name)
#         self.age=age
#         print(f"{age}")

# obj=B("Diksha",20)

