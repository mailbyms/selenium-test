1、HTMLTestRunner是Python标准库的unittest模块的扩展，无法通过pip安装；

2、从 http://tungwaiyip.info/software/HTMLTestRunner.html 下载 `HTMLTestRunner.py` 并将文件放到python3安装目录的Lib下

3、修改 `HTMLTestRunner.py` 文件
- No module named StringIO  
  Python 3 改为 io。第94行引入的名称要改，改成import io，539行要改成self.outputBuffer = io.BytesIO()

- AttributeError: 'dict' object has no attribute 'has_key'  
  642行去做修改，if not rmap.has_key(cls): 需要换成 if not cls in rmap: 

- 'str' object has no attribute 'decode'  
  Python 3 不需要decode 了。772行，ue = e.decode('latin-1')，直接改成 ue = e ，同样 766 类似的uo = o.decode('latin-1')，直接改成 uo = o ；

- output = saxutils.escape(uo+ue), TypeError: can't concat bytes to str
  778行的内容escape(uo+ue) 改成 escape(str(uo)+ue)

- TypeError: unsupported operand type(s) for >>: 'builtin_function_or_method' and 'RPCProxy'
  631行的 print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime) 修改为 print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))