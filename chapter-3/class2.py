class A :
    count=10

a =A()
b=A()
A.count=100
print(a.count,A.count,b.count)
a.count=50
print(a.count,A.count,b.count)

class B(A) :

    def __init__(self,name) :
        self._name = name
    def say_hello(self) :
        print('hello ,i am %s'%self._name)

    @classmethod
    def gl_hello(cls):
        print('hello . i am',cls)

    @staticmethod
    def st_hello():
        print('hello .static method')

b =B('cgl')
b.say_hello()
b.gl_hello()
B.gl_hello()
b.st_hello()
B.st_hello()
print(B.__bases__)
print(issubclass(B,A))

c=B('cgl')
d=c
print(c,d)
del c
print(c,d)