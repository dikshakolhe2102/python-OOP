# class college:
#     def __init__(self):
#         self.collegename='ahmednagar college'
#         self.department='Bca'
#     def display(self):
#         print(self.collegename)
#         print(self.department)

# class student:
#     def __init__(self):
#         self.name='Diksha'
#         self.mobileno=1234567890
#     def admission(self,obj):
#         self.a =obj
#     def print(self):
#         print(self.name)
#         print(self.mobileno)
#         self.a.display()
# obj1=college()
# obj2=student()
# obj2.admission(obj1)
# obj2.print()

#library has book
class book:
    def __init__(self):
        self.name='c++'
        self.author='Nirali Publication'
    def display(self):
        print("Book name:",self.name)
        print("Author:",self.author)

class library:
    def __init__(self):
        self.issue_date='01/07/2025'
        self.returndate='09/07/2025'
    def issuedate(self,obj):
        self.a=obj
    def print(self):
        print("Issue date:",self.issue_date)
        print("Return date:",self.returndate)
        self.a.display()

obj1=book()
obj2=library()
obj2.issuedate(obj1)
obj2.print()


