try :
 print(10/2)
except Exception as e:
 print('error occur~~~',e)
else :
 print('success!!! ')
finally:
 print('finally code')

class MyException(Exception) :
    pass

def throw():
    raise MyException('this is my exception')

throw()