#Hybrid Inheritance Structure
class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

