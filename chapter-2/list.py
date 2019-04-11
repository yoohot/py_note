# my_list=[1,2]
# print(my_list)
# print(my_list[1])
# print(print)

# my_list=['ab','bc','cd','de','ef','fg']
# print(my_list[-1:-5:-2])
# list1= [1,2,3,1,2,4,5,1,2,5,2,3,1]
# list2=['a','b','c']
# print(list1+list2)
# print(list1*2)
# print(max(list2))
# print(min(list1))
# print(list1.count(2))
# if 6 in list1 :
#  print(list1.index(6))
# else:
#    print('no value in list')

# num = list1[1]
# num+=2
# print(list1,num)

# s=[1,2,3,4,5]
# s[0]=6
# print(s)
# s[0:2]=[-1,2]
# print(s)
# s[::2]=[-1,-3,-5]
# print(s)
# del s[0]
# print(s)
# del s[0:2]
# print(s)
# print('可变序列基本方法使用：')
# abs = ['张三','里斯','wangwu']
# print(abs)
# abs.append('zhao六')
# print(abs)
# abs.insert(0,'First')
# print(abs)
# abs.extend('abc')
# print(abs)
# cl=[1,2,3]
# print(cl)
# cl.clear()
# print(cl)
# print(abs.pop(0))
# print(abs)
# abs.append('张三')
# abs.remove('张三')
# print(abs)
# abs.reverse()
# print(abs)
# cl=[1,2,4,1,5,1,7,2,3,9,1]
# cl.sort()
# print(cl)
# cl.sort(reverse=True)
# print(cl)
list = ['a','b',32,21.02,print]
for item in list :
    print(type(item),":",item)
else :
    print('o v e r')
a,b,c,d,e = list
print(a,b,c,d,e)
a,*b,c = 1,2,3,4,5
print(type(b))