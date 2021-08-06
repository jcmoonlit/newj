from typing import Union
import re

#替换字符
def replace(st:str) -> str:
	r = re.sub("(?=')",r'\\',st)
	r = re.sub("{}".format(chr(8209)),'-',r)
	r = re.sub("{}".format(chr(8457)),'°F',r)
	return  re.sub('{}'.format(chr(8451)),"°C",r)


#加回车
def add_br(string:str) -> str:
	return re.sub(r"(?=\d\.\D)",'<br/>',string)

def remove_br(string:str):
	return re.sub(r"<br/>\s*<br/>|<br/>&nbsp;<br/>",'<br/>',string)
	
#取消加粗
def not_html(string:str='') -> str:
	return re.sub(r'<.+?>','',string)

#加粗
def strong(string:str) -> str:
	# print(string)
	r = not_html(string)
	# print(r)
	args = re.findall(r'Item Type:|Package\s\w+:|Packing\s\w+:|[A-Z]\w*\s[a-z]\w*:|[A-Z][a-z]+:|[A-Z][a-z]+\([^()]+\):',r)
	args = list(set(args))
	# print(args)
	for arg in args:
		if arg.upper() in ["Descriptions:".upper(),"Description:".upper(),"Features:".upper(),"Feature:".upper(),"Specifications:".upper(),"Specification:".upper(),"Note:".upper(),"Notes:".upper()]:
			r=re.sub(r'(?={})'.format(arg),'<br/>',r,flags=re.I)
			r=re.sub(r'(?<={})'.format(arg),'<br/>',r,flags=re.I)
			r=re.sub(r'(?={})'.format(arg),'<strong>',r,flags=re.I)
			r=re.sub(r'(?<={})'.format(arg),'</strong>',r,flags=re.I)
		else:
			r=re.sub(r'(?={})|[A-Z][a-z]+\([^()]+\):'.format(arg),'<br/>',r,flags=re.I)
	r=add_br(r)
	# print(r)
	r=replace(r)
	r=remove_br(r)
	r=re.sub(r"^<br/>","",r,1)
	return r

# 重量
def get_weight(r:str) -> Union[str,int]:
		r = re.search(r"(?:weight:\D*|weight:\D*\d+-)(\d+)(?=\s*g)",r,flags=re.I)
		if r:
			r=r.group(1)
		else:
			r=0
		return r