d ={'name':'cgl','age':26,'address':'hubei',"family":{"father":'c',"mather":'m'} }
# print(d,type(d))
# print(d['address'])
# d['address'] ='hubei xiaogan '
# print(d['address'])
# d=dict(name='cgl',address='湖北')
# print(d)
# print(d['address'])

# d=dict(['ab',[2,3],('name','cgl')])
# print(d)
# print(d[2],d['name'])
# d={}
# d.setdefault('name','cgl')
# print(d)
# print(d.setdefault('name','cgl2'))
# print(d)
# print(d.setdefault('addr'))
# print(d)

# print('name' in d)
# print(len(d))
# print('开始：',d)
# d.setdefault('name','cgllll')
# print('setdefault 后:',d)
# u ={'gender':'male'}
# d.update(u)
# print('update 后:',d)

# print(type(d.keys()))
# print(d.keys())
# d.setdefault('phone',26)
# print(d.values())

# result = d.popitem()
# print(result) #元组
# print(type(result))

# result = d.pop('name2','key not exists')
# print(result,type(result))
# copy = d.copy()
# copy['family'].setdefault('brother','cc')
# copy['name'] = 'cl'
# print(d)
# print(copy)
# d.update({'name':'ccggll','face':'smile'})
# print(d)
for key in d.keys() :
 print(d[key],type(d[key]))
print(d.values(),type(d.values()))
for k,v in d.items() :
    print(k,':',v)
