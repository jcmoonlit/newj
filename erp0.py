from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
from time import sleep
import re

#ERP-分销市场-产品信息
brand_new = 'Crazedigi'
un="liufutang"
pd="Aa1234567"
cookies=[
{
    'domain': 'erp.mambacart.com',
    'expiry': 1625834972,
    'httpOnly': False,
    'name': 'rememberMe',
    'path': '/',
    'secure': False,
    'value': 'true'
}, 
{
    'domain': 'erp.mambacart.com',
    'expiry': 1627822173,
    'httpOnly': False,
    'name': 'MZT-TOEKN',
    'path': '/',
    'secure': False,
    'value': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsaXVmdXRhbmciLCJleHAiOjE2MjU4MzQ5NzMsImlhdCI6MTYyNTIzMDE3M30.Exi6A8inGBjAADbxjpg7GqFoby2pU9pesHe4tTk38tFf00VCGazBC7yD-QDw6UHPW8b5j9VuZUyI9K3pX_BCjw'
}, 
{
    'domain': 'erp.mambacart.com',
    'expiry': 1625834972,
    'httpOnly': False,
    'name': 'password',
    'path': '/',
    'secure': False,
    'value': 'YzQ0NzU1YzMzNzkzMTNkYjE3M2U1M2MzZThmYjY3MDE='
}, 
{
    'domain': 'erp.mambacart.com',
    'expiry': 1625834972,
    'httpOnly': False,
    'name': 'username',
    'path': '/',
    'secure': False,
    'value': 'liufutang'
}

]

url="http://erp.mambacart.com/distribution/productList"
#产品列表
class ERP():
	isRefresh = False
	def __init__(self,brower):
		self.brower = brower
		self.action = webdriver.ActionChains(self.brower)
		self.node = None
		self.js = {}

	#添加cookie
	def add_cookies(self):
		for co in cookies:
			self.brower.add_cookie(co)

	#进入ERP
	def come_in(self):
		self.brower.get(url)
		self.add_cookies()
		self.brower.get(url)

	def get_card_list(self):
		card_list=self.brower.find_elements_by_xpath('//*[@id="page-wrapper"]//*[@class="mzt-card-grid_list"]/li[@class="mzt-card-grid_product"]') 
		return card_list

	def perform(self):
		self.action.perform()

	#点击进入
	def get_in(self,card_single):
		#card_single.click()
		card=card_single.find_element_by_xpath('.//img')
		print("card_picer: ",card_single.find_element_by_xpath('.//*[@class="mzt-card-product_price"]/span').text)
		# self.action.move_to_element(card).click(card).perform()
		self.brower.execute_script("arguments[0].click()",card)
		# webdriver.ActionChains(self.brower).move_to_element(card_single).click(card_single).perform()
		# self.node=WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@class="el-drawer__body"]')))
		# self.brower.implicitly_wait(10)

	#关闭产品信息
	def close(self):
		cls_btn = self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button')
		if cls_btn.is_displayed():
			# cls_btn.click()
			self.action.move_to_element(cls_btn).click(cls_btn).perform()
			# self.brower.execute_script("arguments[0].click()",cls_btn)
			# self.brower.implicitly_wait(10)

	# #标题
	# title = self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/*[@role="heading"]').get_attribute('title')

	#获取产品信息详情
	def get_node(self):
		# if self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]').is_displayed():
		# 	self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')
		# return self.node
		# self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')

		if not self.node:
			# if self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]').is_displayed():
			self.node=self.brower.find_element_by_xpath('//*[@class="el-drawer__body"]')
		# else:
		# 	print('yes')
		# 	return self.node

	#获取产品信息的图片
	# 图片链接
	def get_imgs(self,num=9):
		imgs=self.node.find_elements_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul//li/div[@class="el-image"]/img')
		if len(imgs)>=num:
			li_imgs=[imgs[i].get_attribute("src") for i in range(0,num)]
		else:
			li_imgs=[n.get_attribute("src") for n in imgs]
		return li_imgs

	#产品编码
	def get_sku(self):
		id_number=self.node.find_element_by_xpath('.//*[@class="mzt-detail-number"]/span[2]').text
		sku = re.sub(r'.+(?=8X\d+)','YASDF',id_number)
		return sku
	#价格
	def get_picer(self):
		try:
			self.pic=self.node.find_element_by_xpath('.//*[@class="mzt-skupicer"]')
			picer0 = self.pic.get_attribute('innerHTML')
			# picer0 = self.pic.text
			# picer = re.search(r'\d+[.]?\d*',picer0).group()
			# raise Exception
			return picer0
		finally:
			print('picer:',picer0)
		# return picer
	#替换字符
	def replace(self,st):
		r = re.sub("{}".format(chr(8209)),'-',st)
		return  re.sub('{}'.format(chr(8451)),"°C",r)
	
	#选择英文描述信息
	def get_info(self):
		btn = self.node.find_element_by_xpath('.//*[@id="tab-en_US"]')
		self.brower.execute_script("arguments[0].click()",btn)
		# webdriver.ActionChains(self.brower).move_to_element(btn).click(btn).perform()
		pps=self.node.find_elements_by_xpath('.//*[@id="pane-en_US"]//div[@class="el-textarea"]/textarea')
		#标题
		title = self.replace(pps[0].get_attribute("value"))
		#关键词
		search_terms = pps[1].get_attribute("value")
		#五点 bullet point[2-6]
		#re.sub("(?=')",r'\\',p.get_attribute("value"))
		points = [self.replace(re.sub("(?=')",r'\\',p.get_attribute("value"))) for p in pps[2:7] ]
		self.js['title'] = title
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
		description = re.sub("(?=')",r'\\',desc)
		self.brower.switch_to.default_content()
		return description

	# self.brower.switch_to_frame()                   切换到iframe上(过时了)
	# self.brower.switch_to.frame()                   切换到iframe上（推荐）
	# self.brower.switch_to.parent_frame()			  切换回父级页面
	# self.brower.switch_to.default_content()         切换回原主页面


	#测试
	def test(self):
		try:
			if self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button').is_displayed():
				self.close()
				# self.brower.implicitly_wait(10)
			card_list = self.get_card_list()
			for card_single in card_list[0:4]:
				self.get_in(card_single)
				self.get_node()
				sleep(0.5)
				self.get_picer()
				id_number=self.node.find_element_by_xpath('.//*[@class="mzt-detail-number"]/span[2]').text
				print(id_number)
				# self.brower.implicitly_wait(10)
				# js = self.get_all().copy()
				# print("sku ",js['sku'])
				self.close()
		finally:
			self.close()


	def get_all(self):
		self.get_node()
		self.get_info()
		imgs=self.get_imgs()
		sku=self.get_sku()
		picer=self.get_picer()
		description = self.get_desc()
		self.js['imgs'] = imgs
		self.js['sku'] = sku
		self.js['picer'] = picer
		self.js['desc'] = description
		return self.js

	def main(self):
		info = []
		if self.brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button').is_displayed():
			self.close()
		card_list = self.get_card_list()
		for card_single in card_list:
			self.get_in(card_single)
			sleep(0.5)
			# self.brower.implicitly_wait(10)
			js = self.get_all().copy()
			print("sku ",js['sku'])
			info.append(js)
			self.close()
		return info
			
if __name__ == '__main__':
	def fn(kw):
		print(kw['age'])
	js={
		"name":'yanjc',
		"age":16
	}
	fn(js)

	# {
	# 	'picer':'12',
	# 	'sku':,
	# 	'imgs':[],
	# 	'title':,
	# 	'point':[],
	# 	'search':,
	# 	'desc':
	# }