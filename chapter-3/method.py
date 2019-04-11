def cal(a=10,b=20,c=20) :
    print(a,b,c)


def sum(a,b,*c,**d) :
    '''
     计算和
    '''
    result = a+b
    for i in c :
        result += i
    print(result)
    print(d)
    return result

#result = sum(1,2,3,4,5,6,e=1,f=2)
#print(result)
#help(sum)

def inout(a:int) :
    print(a)
    a=100

a=20
#inout(a)
#print(a)
a=200
def gl() :
    a=100
    def gl2():
        global a
        a=50
        print('gl2:a=',a)
    gl2()
    print('gl:a=',a)
#gl()
#print('global:a=',a)

#help(locals)
l = [1,2,3,4,5,6,7,8,9]
l1 = filter(lambda i : i % 2 == 0 ,l)
print('filter : ',list(l1))
l2=map(lambda i : i + 2,l)
print('map:',list(l2))

y=(1,2,3,4,5)
print(*y)
d={'a':'av','b':'bv','c':'cv'}
 
 
def decorate1(fn) :
    def new_fn(*a,**b) :
        print('decorate1 start ...')
        r = fn(*a,**b)
        print('decorate1 end ...')
        return r
    return new_fn

def decorate2(fn):
    def new_fn(*a,**b) :
        print('decorate2 start ...')
        r=fn(*a,**b)
        print('decorate2 end ...')
        return r
    return new_fn

@decorate2
@decorate1
def add(a,b,c,d) :
    return a+b+c+d

print('add result:',add(1,2,3,4))

def m(a=10):
    print('m 1',a)

def m(): #覆盖上面的m
    print('m2')
 


