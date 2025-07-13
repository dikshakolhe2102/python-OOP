#constructor executes only one time for one object
#non parameterised constructor or Default constructor
#it is a special method or special function
# class Demo:
#      def __init__(self):
#           print("Constructor")
#      def f1(self):
#           print("f1")
# obj=Demo()
# obj.f1()

#parameterised constructor
#
# class Focus:
#      def __init__(self,a,b):
#           self.a=a
#           self.b=b
#      def f1(self):
#           print(self.a,self.b)
# obj=Focus(10,20)
# obj.f1()
# obj.x=100
# print(obj.__dict__)
# obj1=Focus(30,40)
# obj1.f1()
# print(obj1.__dict__)


#in this comstructor priority always at the last constrctor
#constructor overloading is not supported in python

# class Focus:
#      def __init__(self):
#           print("Default")
#      def __init__(self,a,b):
#           print("Parameterised")
     
# obj=Focus()
# obj1=Focus(30,40)


#example of parameterised constructor
class employee:
    def __init__(self,a,b,c,d):
        self.name=a
        self.mobile_no=b
        self.salary=c
        self.position=d
    def dislay(self):
        print(self.name)
        print(self.mobile_no)
        print(self.salary)
        print(self.position)
obj=employee('Diksha',12322,1000,'manager')
obj.dislay()
print(obj.__dict__)
obj1=employee('Kolhe',1234568,2000,'dvgsf')
obj1.dislay()
print(obj1.__dict__)
obj2=employee('jaydeep',656757,3000,'asistant')
obj2.dislay()
print(obj2.__dict__)