class Person :
    name = 'cgl'
    age = 20
    print('code')

    def __init__(self,name) : # self 后的参数需要由创建时传入
        print('init excute ... ')
        self.name = name

    def say_hello(self) :
        print('hello i am %s'%self.name )

p1 = Person('swk')
# p1.say_hello()
# p2= Person()
# p1.age=22
# print(p1.name)

class Dog :

  def __init__(self,name,age,color) :
     self.name=name
     self.age=age
     self.color=color

  def introduce(self) :
    print('Dog:',self.name,self.age,self.color)

# d1 =Dog('petty',3,'yellow')
# d1.introduce()

class Article :

    def __init__(self,title:str,length:int) :
         self._title=title
         self._length=length

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title) :
        self._title=title


    @property
    def length(self):
        return self._length

    @length.setter
    def length(self,length):
        self._length=length


art =Article('习近平欧洲之行',250)
print(art.title,art.length)
art.title='中共国家主席欧洲之行'
art.length=350
print(art.title,art.length)

