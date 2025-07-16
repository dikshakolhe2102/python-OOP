# #multiple inheritace is also called as method resolution order(MEO)
# #calling of constructor is depends on order in super method
# class A:
#     def __init__(self):
#         print("Constructor of parent 1")
# class B:
#     def __init__(self):
#         print("Constructor of parent 2")
# class C(B,A):
#     def __init__(self):
#         B.__init__(self)
#         super().__init__()
#         print("Constructor of child class")
# obj1=C()


# #Method overriding in multiple inheritance
# #same function name,same parameters in differnt class it also called as runtime polymorphism
# class A:
#     def M1(self):
#         print("Method of parent 1")
# class B:
#     def M1(self):
#         print("Method of parent 2")
# class C(B,A):
#     def M1(self):
#         #B.M1(self)
#         print("Method of child class")
# obj1=C()
# obj1.M1()

