# s = {'a','b','a','23','china'}
# print(s,len(s))
# s.add('abc')
# s.update({1,2,3})
# print(s)
# result = s.pop()
# print(result)
# s.pop()
# s.pop()
# print(s)
# result = s.remove('23')
# print(result)
 
s1 = {1,2,3,4,5}
s2={2,5,7,9,0}

s = s1 & s2
print(s)

s= s1 | s2
print(s)

s= s1 ^ s2
print(s)
print(s1 <= s2)
print({2,5} <= s2)