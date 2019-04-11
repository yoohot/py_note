## python 流程控制

### 条件判断语句 if
    1if 条件表达式：语句 #也可以代码块包含多行,有严格格式要求,换行tab或四个空格(官推)
                   不能空格和tab混用
      if True : 
         print('代码块一')
      	print（'代码块二'）
      print('非代码块')
     input()函数命令行输入，返回字符串，可以带参数 eg:input('请输入：')

     2if-else语句
        if 表达式 ：
           代码块
        else ：
           代码块
     3if elif elif ... else
       if 表达式：
          代码块
       elif 表达式 ：
          代码块
       elif 表达式 ：
          代码块
       else
          代码块：

###循环
   1while
    while 条件表达式 :
      代码块
    else :
      代码块（while结束后执行）
   2嵌套循环
    while 条件表达式 :
      代码块(可包含while循环)
      while 条件表达式 :
       代码块
      else :
       代码块（while结束后执行）
    else :
      代码块（while结束后执行）
   3 break 和 continue 只对最近的循环起作用
     break：立即跳出循环，连循环else语句也不执行
     continue:跳过本次循环进入下一轮，else会执行
   4 pass 占位符，直接通过
   ext：引入time模块来统计执行时间
    from time import *
    time()函数返回当前时间浮点 秒

### 序列squence
  可变序列：序列中元素可改变 
         list
  不可变序列：序列中元素不可变
         字符串 str
         元组 tuple
 序列通用操作
   eg：[],[1,'abc',True,None,[1,2,3],print]
  1获取元素：
    eg:list[0]
    下标可以是负数，表示从后往前 -1表示倒数第一个
  2列表长度：
    len(list)
  3切片：获取列表指定部分
list[起始下标（默认0):结束下标（不包括该元素，默认列表长度)]：半包(]
list[起始：结束：步长]：步长 默认1.表示每步长个元素获取第一个元素，负数
  4通用操作
   +：拼接两个列表
   *：复制列表n次
   in/not in:检查元素是否在列表
   max()/min():最大值，最小值
   方法：python的方法跟函数差不多，只是必须通过对象.调用 x.method()
   list.index(x[,i[,j]]):获取x对象的下标:i和j可选：i查找起始位置，j查找结束位置ij半包
   list.count(x):统计x次数
 可变序列基本操作：
   不可变序列可以通过list()转为list序列
   修改元素： list[1]='aaa'
   删除元素： del list[2]
   切片修改： list[0：2]=[1,2,3,4,5] ext:当设置步长list[::2],则赋值的list长度必须等于
            切片中的元素个数
   删除切片： del list[0:2]  del list[0:6:2]
 可变序列基本方法：
   append(x):末尾添加元素
   insert(n,x) 在指定位置n插入元素x
   extend(序列)：将参数序列添加到当前序列之后
   clear():清空序列
   pop(n):删除并返回指定下标的元素,不传参数则删最后一个
   remove(x):删除指定元素第一个
   reverse():反转列表
   sort():元素排序，默认升序，可以传reverse=True 来降序
 遍历序列：
    1while循环遍历
    2for循环
      for 变量 in 序列:
        代码块
      else :
      代码块（for结束后执行）
 range(x,y,z):x z 可省；生成自然数序列，x起始位置，y结束位置，z步长
 元组：不可变序列，相当于不可变列表；不希望序列被改变时使用元组
      （）创建元组 eg： tuple =()，tuple2=(1,2,3,4) ,元素不为空时（）可省略，t=1,3
       元素只有一个，后边需要加逗号 t4=(1,) or t4 =1,
 序列解包(解构)： t5=1,2,3  a,b,c=t5 则a=1 b=2 c=3 eg值交换:a=100 b=200 a,b = b,a
               解包时变量数量必须等于序列大小，ext a,b,*c =(1,2,3,4,5) c为列表

可变对象：值可变的对象
         a=[1,2] a=[2,3] ：这种时改变量不是改变量的值 a[0]=1 这是改对象值
         可以通过id()来判断
== 和 is 
 a=[1,2,3] b=[1,2,3] a==b True, a is b False

### 字典（mapping）
   作用类似java中map，存储对象的容器k：v。列表存储性能好，查询性能不足；
   字典通过唯一的key，快速查找对应对象
   创建：1 {k1：v,k2:v},key可以是任意的不可变对象。key不能重复，否则v会被替换
        2 dict()函数： d=dict(name='a',age=18) 这种方式key为str
                     双值序列(只含两个元素)，可以将包含双值子序列的序列传给dict()
                      d=dict(['ab',(1,2),['n','k']])
   获取：d[key],若不存在,报错
        d.get(key),若不存在，不报错返回None，可以加get(key,默认值)
   长度：len() key个数
   in 和 not in:
   修改：1 dict[key]=value,key不存在则添加
        2 d.setdefault(key[,defatut]) 如果key存在，则不添加
        3 d.update(dict)合并dict到d，key会被覆盖
   删除： del d[key] 不存在,报错
         setdefault()
         popitem()随机删除一个键值对，一般是删除最后一个，返回key value 元组
         pop(key) 删除，并返回，不存在的key会报错，可以pop(key,default)指定默认值不会
          报错；
         clear():清空
   copy()：对字典进行浅复制，两对象独立，id不同；但是字典中的对象是直接引用的，同java
          中的浅复制；eg：{'a':{'a':'bbb'}}其中的字典是直接公用的
   遍历：keys(): 返回字典所有的key;for 遍历
        values():返回所有value；重复不会覆盖
        items():返回双值序列的序列； for k,v in d.items: ...
### 集合（set）
    1只能存储不可变对象 str，数字，bool...，
    2存储无序，不能通过下标来获取元素，可以list()转换
    3元素不重复 not in 判断元素 
    创建： {...},创建空集合不能{}，这是字典，使用set()函数
          set()，可以将序列或字典转为集合，字典时只会取key
    len():元素个数
    add():添加元素
    update(s)：合并集合/序列/字典
    pop():随机删除一个元素
    remove(k):删除指定元素,key不存在报错
    clear()：清空
    集合间操作：不会影响原来集合，返回新集合
     &： 交集
     |： 并集
     -: 差集
     ^:异或 两集合中不相交部分
     <=: 判断一个集合是否位另外一个集合的子集 <  == > >=



