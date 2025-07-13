# class focus:
#     def f1(self):
#         print("f1")
#         print(id(self))  #self is compulsury parameter
# obj=focus()
# print(id(obj))
# obj.f1()
# obj1=focus()
# print(id(obj1))
# obj1.f1()

# #function with parameter
# class focus:
#     def f1(self,a):
#         print("f1",a)
#         print(id(self))  
# obj=focus()
# print(id(obj))
# obj.f1(10)

# class student:
#     def info(self):
#         self.name='diksha'
#         self.rollno='1'
#     def display(self):
#         print(self.name)
#         print(self.rollno)
# obj2=student() 
# obj2.info()
# obj2.display()
# obj2.marks=10
# print(obj2.__dict__)
# obj=student()
# obj.info()
# obj.display()
# print(obj.__dict__)


#instace variable
# class employee:
#     def info(self,a,b,c):
#         self.name=a
#         self.id=b
#         self.salary=c
#     def display(self):
#         print(self.name)
#         print(self.id)
#         print(self.salary)
# obj2=employee() 
# obj2.info('diksha',12,12000)
# obj2.display()
# print(obj2.__dict__)
# obj=employee()
# obj.info('kolhe',3,1000)
# obj.display()
# print(obj.__dict__)


#02/07/2025
# class Bank:
#     def accept(self,a,b,c):
#         self.name=a
#         self.acc_no=b
#         self.balance=c

#     def deposite(self):
#         amt=int(input("Enter amount you want to deposite:"))
#         self.balance=amt+self.balance
#         print(self.balance)

#     def withdrawal(self):
#         amount=int(input("enter amount you want to withdrawal:"))
#         if amount<self.balance:
#             self.balance=self.balance-amount
#             print("amount are withdrawal:",self.balance)

#         else:
#             print("Insufficient balance")

#     def display(self):
#         print(self.name)
#         print(self.acc_no)
#         print(self.balance)

# obj=Bank()
# obj.accept("diksha",1231376,1000)
# obj.deposite()
# obj.withdrawal()
# obj.display()
# print(obj.__dict__)

# class rectangle:
#     def accept(self):
#         self.length=int(input("Enter length:"))
#         self.breath=int(input("Enter breath:"))

#     def calculate(self):
#         self.area=self.length*self.breath
#         print("Area of rectangle",self.area)
#     def display(self):
#         print(self.length)
#         print(self.breath)
#         print(self.area)
# obj=rectangle()
# obj.accept()
# obj.calculate()
# obj.display()
# print(obj.__dict__)

#oder class 
#it consist of instance variable productname,pquantity,product price,discount,total
#accept function accept from user name,qty,price
#calcualte total function in this function
#Calculate discount function condition:
# if total amt is greater than 500 discount 5%
# if total >1000 discount 15%
#if total >2000 discount 30%
#else no discount
#display product name,product quantity,product price,discount,total

# class order:
#     def accept(self):
#         self.product_name=input("Enter the product name:")
#         self.qty=int(input("Enter quantity:"))
#         self.price=int(input("Enter price:"))
#     def calculate(self):
#         self.total=self.qty*self.price
#         print("Total Bill:",self.total)
#     def discount(self):
#         self.dis=0
#         if self.total>=2000:
#             self.dis=self.total*0.30
#             print("total Bill after discount:",self.dis)
#         elif self.total>=1000:
#             self.dis=self.total*0.15
#             print("total Bill after discount:",self.dis)
#         elif self.total>=500:
#             self.dis=self.total*0.5
#             print("total Bill after discount:",self.dis)
#         else:
#             print("No discount apply on your order")
#     def display(self):
#         print(self.product_name)
#         print(self.qty)
#         print(self.price)
#         print(self.total)
#         print(self.dis)

# obj=order()
# obj.accept()
# obj.calculate()
# obj.discount()
# obj.display()





