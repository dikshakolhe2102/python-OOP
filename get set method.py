#getter setter method
class student:
    def setName(self,a):
        self.name=a
    def getName(self):
        print(self.name)
    def setRollno(self,b):
        self.rollno=b
    def getRollno(self):
        print(self.rollno)
    def setMarks(self,c):
        self.mark=c
    def getMarks(self):
        print(self.mark)
obj=student()
obj.setName("Diksha")
obj.getName()
obj.setRollno(10)
obj.getRollno()
obj.setMarks(100)
obj.getMarks()
print(obj.__dict__)
obj1=student()
obj1.setName("Kolhe")
obj1.getName()
print(obj1.__dict__)

