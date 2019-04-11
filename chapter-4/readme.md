### 模块化
一个文件就是一个模块，文件名要符合标识符规范
引入模块： import 模块名 [ as 别名]
每一个模块都有一个__name__属性：获取到模块的名字 eg print(__name__)
__name__为__main__是主模块，一个程序只有一个，python开始执行的模块，主模块名可以
不符合标识符规范。
使用：引入的模块可以直接通过模块名访问变量，函数，类...;
引入模块部分：from 模块名 import 变量,函数,类..[as 别名]这样可以直接使用,不需要模块名
                    from 模块名 import * :引入模块所有内容
#起了别名的方法，变量，类等不会覆盖本模块中重名的方法，变量..
#添加了下划线的变量只能在模块内访问，这只针对 from m import *情况
#模块中的测试代码需 if __name__ == '__main__' : 测试代码,避免被别的模块引入时被执行


### 包 package

包也是一个模块，当一个模块代码过多时,或需要分解为多个模块时,这时需要用到包,包就是一个文
件夹，只需要一个空的__init__.py件即可。当然它也可以执行包的初始化代码，或者定义__all__ 
等变量。
当然包底下也能包含包
引入包下其他模块 from 包 import X,X
__pycache__是模块的缓存文件,py代码需要转为机器码再执行。使用模块（包）时需要这些缓存


### 标准库
开箱即用,python提供的一套标准的模块库
sys模块：提供了一些变量和函数，可以获取到python解析器的信息
   import sys
  sys.argv :执行py文件时，命令行中包含的参数，返回一个列表
  sys.modules:获取当前程序中获取的所有模块，返回一个字典
  sys.path:模块搜索路径(import的搜索路径，类似环境变量)，返回一个列表
  sys.platform:当前运行环境,win32，linux... 返回字符串
  sys.exit():退出程序
os模块：访问操作系统的一些信息
  import os
  os.environ:获取系统环境变量
  os.system(..):执行cmd命令

### 异常和文件
异常：
try：
  代码块
except [NameError]:#NameError是一个异常类,不跟异常类,会捕获所有异常相当于加Exception
  代码块
except [NameError] [as 变量]:#将异常对象赋值给变量，可以代码块中使用 
  代码块
[else：]#（可选）
  代码块
finally:
  代码块#无论是否异常，都会最后执行
异常传播:出现异常，所有的异常信息会被保存在一个异常对象中，异常传播实际上就是异常对象抛
给调用处；python中提供了多种异常对象。
抛出异常：raise 语句， raise Exception类或实例
自定义异常： 只需要创建类继承Excpetion

文件：
打开文件：open()函数,返回文件对象；\\代替\ 或 / 或 r'\tzifuc\huan' 原始字符串不转义
   open打开的文件分两种：纯文本文件 和 二进制文件，默认纯文本形式打开
   open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
    closefd=True, opener=None)
关闭文件： 
        1文件对象.close()
        2 with ... as 语句 with open(file,encoding='utf-8') as f :
                             代码块#执行完自动关闭文件
文本文件：
 简单读取：通过f.read()方法读取文本文件全部内容
 大文件读取：read()可以接受size参数，指定要读取的字符数，默认-1读取全部，每次会记录读取
          的位置，所以可以继续往后读，若读的是二进制，size表示字节数
 文件读取2：readline()读取一行内容，readlines()读取每行封装成列表返回
          遍历eg: for line in file_obj:
                    print(line)
 文件写入：f.write()写入，若是文本文件，传入字符串参数,写入前open()需指定mode参数，返回
         写入的字符数
         mode:
            r:只读
            w:删除原文件内容并开始写入，可多次写入
            a:append，追加
            +：r+ 可读可写不能创建 w+ 读写新建 a+可读写追加
            x:不存在新建文件，存在则报错
            b:操作二进文件，rb，wb...
            t:操作文本文件默认。r相当于rt
二进制文件：rb，wb
f.tell()方法查看当前读取到的位置
f.seek(n,mode=0)修改当前读取到的位置 mode: 0默认,从头计算 1从当前位置 2从最后向前计算
其他操作：os模块
  os.listdr():相当于ls命令
  os.getcwd():获取当前目录
  os.chdir():切换当前目录
  os.mkdir():创建目录
  os.rmdir():删除目录
  os.remove():删除文件
  os.rename():重命名，可以移动





 