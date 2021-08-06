# from __future__ import annotations
# 新版本的特新引入到
from typing import Union
import random,re,time
from dataclasses import dataclass, field
subject=('Phone Tripod Review',
'Flexible Phone Tripod Test',
'Product Review (Phone Tripod)',
'Product Test (iPhone Tripod with Remote)',
'Phone Tripod Stand Review on Amazon',
'Portable Phone Tripod Review on Amazon',
'Product Test (Phone Camera Tripod)',
'Phone Camera Tripod Review',
'Product Review (Flexible iPhone Tripod)',
'Product Review (Flexible Phone Tripod)')
def fn(user="jaco",host="1111"):
	print(user,host)

class MyException(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return "My exception!!!"

@dataclass
class Jaco():
	name:str
	age:int
	address:str
	infomation:str

class JC():
	def __init__(self,name):
		self._name=name
		print('init')
	def __call__(self):
		print('call')

	def replace(self,st) -> Union[str,int]:
		r = re.sub(r"\n",'-',st)
		return  re.sub('{}'.format(chr(8451)),"°C",r)

def strong_br(*args,string=''):
		r = string
		for arg in args:
			r=re.sub(r'(?={})'.format(arg),'<strong>',r,flags=re.I)
			r=re.sub(r'(?<={})'.format(arg),'</strong>',r,flags=re.I)
			# strong(arg)
		r=re.sub(r"(?=\d\.\D)",'<br/>',r)
		return r

def fn(x,y):
	return x,y

def me():
	raise MyException()

def wait_to():
	pass

def testfnn(value):
	if '"' in value and "'" in value:
		substrings = value.split("\"")
		result = ["concat("]
		for substring in substrings:
			result.append("\"%s\"" % substring)
			result.append(", '\"', ")
		result = result[0:-1]
		if value.endswith('"'):
			result.append(", '\"'")
		return "".join(result) + ")"

def testloop():
	_is= True
	i=0
	while _is:
		try:
			print("i",i)
			# time.sleep(2)
			me()
		except MyException as e:
			print(e)
			i+=1
			if i>=10:
				_is=False
		else:
			pass
	print("i",i)

class Testcls:
	@classmethod
	def hacls(cls):
		s=cls()
		print(s)
		print("cls new start!")

	def __new__(cls):
		print("__new__")
		return super()
	
	def __init__(self):
		print('init')

if __name__ == '__main__':

	print(testfnn("sdff"))
	jaco = Jaco('yan',25,"baoli",'nothing')
	print(jaco.name)
	# testloop()
	# h = {
	#   'user':"yan",
	#   'host':'192.168.1.1'
	# }
	# fn()
	# fn('user','127.0.0.1')
	# fn('user',host='127.0.0.2')
	# fn(**h)
	# print(random.choice(subject))
	# try:
	#   jc = JC('yan')
	#   jc()
	#   print(jc.replace('abcdef \n\n600'))

		
	# finally:
	#   print("error")
	
	# args=[1,2,3,4,5,6,7,8,9,10]
	# for num in args:
	#   try:
	#       print(100/(num-3))
	#       input("!")
	#   except ZeroDivisionError:
	#       # args.append(num)
	#       # time.sleep(2)
	#       print(num,'当前分母为0')
	#   # finally:
	#   #   print("yan")
	#   #   
	# print("end!")