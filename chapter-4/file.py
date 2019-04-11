with open('file/test.txt',encoding='utf8')  as test :
    print(test)
    content = test.read()
    print(content)

with open('file/test.txt',mode='r+',encoding='utf-8') as f :
    for line in f :
        print(line,end='')
    f.write('test write....')

#test.read() close file