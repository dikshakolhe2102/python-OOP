#static method
# class college:
#     @staticmethod
#     def f1():
#         print("f1")
# college.f1()
# d=college()
# #d.f1()       by using object name we can not call static method

#instance method
# class college:
#     def f2(self):
#         print("f2")
# #college.f2()       
# d=college()
# d.f2()


# class specifier:
#     a=10              #public
#     _b=20             #protected
#     __c=30            #private
# print(specifier.a)
# print(specifier._b)
# print(specifier.__c)


class specifier:
    def f1(self):
        print("Public")
    def f2(self):
        print("Protected")
    def f3(self):
        print("Private")
d=specifier()
d.f1()
d._f2()
d.__f3()







