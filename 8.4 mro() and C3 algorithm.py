#Illustrating mro()
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(D.mro())
#Illustrating C3 algorithm
class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B):
    pass
class E(B,C):
    pass
class X(D,E,C):
    pass
print(X.mro())