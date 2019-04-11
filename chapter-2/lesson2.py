from time import *
#if 10%2 == 0 : print('yes !!!') 
if False :
    print('hello')
    print('cgl')
    print('!!!')
#print('abc')
#a = input()
#if int(a) > 10 :
#    print('a > 10')

#a = 63
#if a>18 :
#    print('u r grownman')
#else :
# print('u r child')
#if a <= 6 :
 #   print('u r baby')
#elif a <=18 :
 #   print('u r child')
#elif a < 55 :
 #   print('u r grownman')
#else :
#    print('u r old man')
#print('第一题 判断奇偶数：')
#num = int(input('请输入数字：'))
#if num % 2 ==0 :
# print(f'{num} 是一个偶数')
#else :
# print(f'{num} 是一个奇数')

#print('第二题 判断闰年:')
#year = int(input('请输入年份：'))
#if year % 4 ==0 and year % 100 != 0 :
#    print(f'{year} 是一个闰年')
#else :
#    print(f'{year} 不是闰年')

#print('第三题 判断狗的人类年龄：')
#age = int(input('请输入狗的年龄：'))
#if age <0 :
#   print('请输入大于0的年龄')
#elif age <=2 :
#   print('狗的人类年龄为',age*5)
#else :
#    print('狗的人类年龄为',10+(age-2)*4)
begin =time()
i =1
count = 0 
while i< 1000000000 :
  count += i
  i+=2
else :
 print("第一题1000000内奇数之和为:",count)
 end = time()
 print('总共花费',end-begin)

# i= 7
# num =0
# count =0
# while i<100 :
#   count+=i
#   num+=1
#   i+=7
# else :
#     print(f'第二题100内7的倍数之和{count},次数{num}')

# i = 1
# while i <10 :
#   j = 1
#   while i >= j :
#      print(f'{j} * {i} = %2d'%(i*j),end ='|')
#      j += 1
#   else :
#      print('')
#   i+=1

# i = 5
# j = 0
# while i > j :
#     j+=1
#     if j == 3 :
#         break
#     print(j)
# else :
#     print('循环结束')



