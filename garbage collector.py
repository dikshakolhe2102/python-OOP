#Destructor :It is a speical method which destroyes object and releases resources tied to objects.
            # Destructor is automatically called when object is destroyed.
            #  Desructor is called based on below condition
                #   1) When reference counting reaches to 0
                #    2) When variable goes out of socpe 
            # 

#Ex:1 :When variable goes out of socpe 
class Example:
   def __init__(self):
         print("Object Created")
   def __del__(self):
        print("Object destroyed")
e1=Example()
print("End")        #o/p will be  Object Created End Object destroyed



#Ex:2 : When reference counting reaches to 0
class Example:
   def __init__(self):
         print("Object Created")
   def __del__(self):
        print("Object destroyed")
e1=Example()
e1=None          # only refernce will set to none
print("End")        #o/p will be  Object Created  Object destroyed End


#Ex:3 : When object refernce to many  object
import time
class Example:
   def __init__(self):
         print("Object Created")
   def __del__(self):
        print("Object destroyed")
e1=Example() 
e2=e1
e3=e2
e4=e3
del e1
print("e1 is destroyed") 
time.sleep(5)  
print("End of program")     
time.sleep(5) 
# del e2
# del e3
# print("e2 and e3 will destroyed")
# del e4




