from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys
from time import sleep
import re

#ERP-分销市场-产品信息
brand_new = 'Crazedigi'
un="liufutang"
pd="Aa1234567"

url0="http://erp.mambacart.com/distribution/productList"
url="http://erp.mambacart.com/login"

#产品列表
class ERP():
	def __init__(self,brower):
		self.brower = brower
		self.action = webdriver.ActionChains(self.brower)
		self.node = None
		self.js = {}
	def __call__(self):
		self.brower.get(url)
		# self.come_in()

	#execute_script
	def es(self,script,*args):
		return self.brower.execute_script(script,*args)

	
	#进入ERP
	def come_in(self):
		# self.brower.get(url)
		# self.add_cookies()
		# self.brower.get(url)
		un=self.brower.find_element_by_xpath('//*[@type="text"]')
		pw=self.brower.find_element_by_xpath('//*[@type="password"]')
		sub=self.brower.find_element_by_xpath('//*[text()="登录"]')
		un.send_keys("liufutang")
		pw.send_keys("Aa1234567")
		sub.click()
		# self.es("arguments[0].click()",self.xpath('//*[contains(text(),"分销市场")]'))
		# self.es("arguments[0].value='liufutang'",un)
		# self.es("arguments[0].value='Aa1234567'",pw)

		
	def get_card_list(self):
		card_list=self.brower.find_elements_by_xpath('//*[@id="page-wrapper"]//*[@class="mzt-card-grid_list"]/li[@class="mzt-card-grid_product"]//img') 
		return card_list

	#点击进入
	def get_in(self,card_single):
		#card_single.click()
		self.brower.execute_script("arguments[0].click()",card_single)
		# webdriver.ActionChains(self.brower).move_to_element(card_single).click(card_single).perform()
		# self.brower.implicitly_wait(10)

	#关闭产品信息
	def close(self):
		cls_btn = self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button')
		if cls_btn.is_displayed():
			# print('ready closing!')
			cls_btn.find_element_by_xpath('//*[@id="el-drawer__title"]/button').click()
		# self.brower.implicitly_wait(10)

	# #标题
	# title = self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/*[@role="heading"]').get_attribute('title')

	#获取产品信息详情
	def get_node(self):
		WebDriverWait(self.brower,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="mzt-product-details el-loading-parent--relative"]')))
		self.node=WebDriverWait(self.brower,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="mzt-product-details"]')))
		# if not self.node:
		# 	# if self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]').is_displayed():
		# 	self.node1=WebDriverWait(self.brower,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="mzt-product-details el-loading-parent--relative"]')))
		# 	# self.node1=self.brower.find_element_by_xpath('//*[@class="mzt-product-details el-loading-parent--relative"]')
		# 	# self.node0=self.brower.find_element_by_xpath('//*[@class="mzt-product-details"]')
		# 	self.node=WebDriverWait(self.brower,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="mzt-product-details"]')))
		# 	# self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')
		# # if self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]').is_displayed():
		# # 	self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')
		# # # else:
		# # # 	self.node = None
		# # return self.node

	#获取产品信息的图片
	def getimgs(self):
		self.imgsdiv=self.node.find_element_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul/div')
		self.imgsl=self.node.find_elements_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul/div//li')
		self.imgs=self.node.find_elements_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul//li/div[@class="el-image"]/img')

		
	# 图片链接
	def get_imgs(self,num=9):
		imgs=self.node.find_elements_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul//li/div[@class="el-image"]/img')
		if len(imgs)>=num:
			# fo	r i in range(0,num):
			# 	print(self.brower.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth!='undefined' &&arguments[0].naturalWidth>0",imgs[i]))
			# 	print(i,imgs[i].get_attribute("src"))
			li_imgs=[imgs[i].get_attribute("src") for i in range(0,num)]
		else:
			# for i in imgs:
			# 	print(self.brower.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth!='undefined' &&arguments[0].naturalWidth>0",i))
			# 	print(i.get_attribute("src"))
			li_imgs=[n.get_attribute("src") for n in imgs]
		return li_imgs
	#

	#产品编码
	def get_sku(self):
		id_number=self.node.find_element_by_xpath('.//*[@class="mzt-detail-number"]/span[2]').text
		sku = re.sub(r'.+(?=8X\d+)','ZW777',id_number)
		_sku = re.sub(r'.+(?=8X\d+)','',id_number)
		return sku,_sku
	#价格
	def get_picer(self):
		try:
			self.pic=self.node.find_element_by_xpath('.//*[@class="mzt-skupicer"]')
			picer0 = self.node.find_element_by_xpath('.//*[@class="mzt-skupicer"]').text
			picer = re.search(r'\d+[.]?\d*',picer0).group()
			return picer
		finally:
			print(picer0)
	#替换字符
	def replace(self,st):
		r = re.sub("(?=')",r'\\',st)
		r = re.sub("{}".format(chr(8209)),'-',r)
		r = re.sub("{}".format(chr(8457)),'°F',r)
		return  re.sub('{}'.format(chr(8451)),"°C",r)
	def xpath(self,xpath):
		try:
			node = self.brower.find_element_by_xpath(xpath)
		except NoSuchElementException as e:
			print(e)
			return None
		else:
			return node
	#选择英文描述信息
	def get_info(self):
		btn = self.node.find_element_by_xpath('.//*[@id="tab-en_US"]')
		self.brower.execute_script("arguments[0].click()",btn)
		# webdriver.ActionChains(self.brower).move_to_element(btn).click(btn).perform()
		pps=self.node.find_elements_by_xpath('.//*[@id="pane-en_US"]//div[@class="el-textarea"]/textarea')
		#标题
		title = self.replace(re.sub(r"\n",'',pps[0].get_attribute("value")))
		_titlecn = self.xpath('//div[@id="pane-zh_CN"]//div[@class="el-textarea"]//textarea[1]')
		titlecn = self.replace(re.sub(r"\n",'',_titlecn.get_attribute("value")))
		#关键词
		search_terms = self.replace(re.sub(r"\n",'',pps[1].get_attribute("value")))
		#五点 bullet point[2-6]
		#re.sub("(?=')",r'\\',p.get_attribute("value"))
		points = [self.replace(re.sub(r"\n",'',p.get_attribute("value"))) for p in pps[2:7] ]
		self.js['title'] = title
		self.js['titlecn'] = titlecn
		self.js['points'] = points
		self.js['search'] = search_terms
		return self.js

	#描述
	#iframe
	def get_desc(self):
		iframe=self.node.find_element_by_xpath('.//*[@id="pane-en_US"]//iframe')
		#转换到内
		self.brower.switch_to.frame(iframe)
		# description = self.brower.find_element_by_xpath('//body').text
		desc = self.brower.find_element_by_xpath('//body').get_attribute('innerHTML')
		self.brower.switch_to.default_content()
		description = self.replace(desc)
		description = self.strong(description)
		weight = self.get_weight(description)
		return description,weight
	
	def get_weight(self,r):
		r = re.search(r"(?:weight:\D*|weight:\D*\d+-)(\d+)(?=\s*g)",r,flags=re.I)
		if r:
			r=r.group(1)
		else:
			r=0
		return r
	
	#加回车
	def add_br(self,string):
		return re.sub(r"(?=\d\.\D)",'<br/>',string)

	def remove_br(self,string):
		return re.sub(r"<br/>\s*<br/>|<br/>&nbsp;<br/>",'<br/>',string)
	
	#取消加粗
	def not_html(self,string=''):
		return re.sub(r'<.+?>','',string)

	#加粗
	def strong(self,string):
		# print(string)
		r = self.not_html(string)
		# print(r)
		args = re.findall(r'Package\s\w+:|Packing\s\w+:|[A-Z]\w*\s[a-z]\w*:|[A-Z][a-z]+:|[A-Z][a-z]+\([^()]+\):',r)
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
		r=self.add_br(r)
		# print(r)
		r=self.remove_br(r)
		r=re.sub(r"^<br/>","",r,1)
		return r
	
	#测试
	def test(self):
		if self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button').is_displayed():
			self.close()
		card_list = self.get_card_list()
		id_number='$$$'
		for card_single in card_list:
			self.get_in(card_single)
			self.get_node()
			# sleep(0.8)
			# self.brower.implicitly_wait(10)
			# js = self.get_all().copy()
			# print("sku ",js['sku'])
			# self.get_node()
			# 需要判断是否js更新完毕
			self.get_picer()
			self.get_imgs()
			id_num=self.node.find_element_by_xpath('.//*[@class="mzt-detail-number"]/span[2]').text
			if id_number == id_num:
				print('Yes',id_num)
				break
			id_number=id_num
			print(id_number)
			# sleep(0.5)
			# input('wait!')
			self.close()


	def get_one(self,RMB=110):
		self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')
		self.get_info()
		picer=self.get_picer()
		if int(float(picer)) < RMB:
			imgs=self.get_imgs()
			sku,_sku=self.get_sku()
			description, weight = self.get_desc()
			self.js['imgs'] = imgs
			self.js['sku'] = sku
			self.js['_sku'] = _sku
			self.js['picer'] = picer
			self.js['desc'] = description
			self.js['weight'] = weight
			return self.js
		else:
			return {}


	def get_all(self,RMB=110):
		# self.get_node()
		self.get_info()
		picer=self.get_picer()
		if int(float(picer)) < RMB:
			imgs=self.get_imgs()
			sku,_sku=self.get_sku()
			description, weight = self.get_desc()
			self.js['imgs'] = imgs
			self.js['sku'] = sku
			self.js['_sku'] = _sku
			self.js['picer'] = picer
			self.js['desc'] = description
			self.js['weight'] = weight
			return self.js
		else:
			return {}

	def main(self):
		info = []
		# if self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button').is_displayed():
		self.close()
		card_list = self.get_card_list()
		sku0='$$$'
		for card_single in card_list:
			self.get_in(card_single)
			self.get_node()
			# sleep(0.5)
			# self.brower.implicitly_wait(10)
			js = self.get_all().copy()
			if not bool(js):
				self.close()
				continue
			sku = js['sku']
			if sku0 == sku:
				print('Yes:',sku)
				break
			sku0=sku
			print("sku ",sku0)
			info.append(js)
			self.close()
		return info
			
if __name__ == '__main__':
	pass
	# {
	# 	'picer':'12',
	# 	'sku':,
	# 	'imgs':[],
	# 	'title':,
	# 	'point':[],
	# 	'search':,
	# 	'desc':
	# }
