# sys模块：提供了一些变量和函数，可以获取到python解析器的信息
#    import sys
#   sys.argv :执行py文件时，命令行中包含的参数，返回一个列表
#   sys.modules:获取当前程序中获取的所有模块，返回一个字典
#   sys.path:模块搜索路径(import的搜索路径，类似环境变量)，返回一个列表
#   sys.platform:当前运行环境,win32，linux... 返回字符串
#   sys.exit():退出程序
# os模块：访问操作系统的一些信息
#   import os
#   os.environ:获取系统环境变量
#   os.system(..):执行cmd命令
import sys,os,pprint
print(sys.argv)
print(sys.modules)
print(sys.path)
print(sys.platform)
print(os.environ)
print(os.system('dir'))
pprint.pprint(sys.path)
sys.exit()
print('end... wont occur')

