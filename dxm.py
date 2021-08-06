from typing import Union,List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re,time
import util
'''
gzqupdate
Abc123321.
错误信息，sku重复
//*[@class="errorMsgContent" and contains(text(),"重复")]
'''
'''3375301/706814011/11051400011/3422351/3775541/8620015011/13106351"
"amzProAdd.getAndInitAttr(715636,13106351);715636,13106351
(categoryDBId, categoryId)
 amzProAdd.getAndInitAttr(categoryDBId, categoryId);'''
sr='''
amzProAdd.initCategory("{}".split('\/'));
amzProAdd.categoryDeterInit();
'''
class MyException(Exception):
	pass

class CloseException(MyException):
	def __init__(self):
		pass
	def __str__(self):
		return "Unable to close the Main_Window!!!"

cookies=[
{'domain': 'www.dianxiaomi.com', 'expiry': 1656243957, 'httpOnly': True, 'name': 'dxm_s', 'path': '/', 'secure': False, 'value': 'McGPruMih-7wuet96vlZeaDHgMdaD9RS_IRuQ2Vwub8'}
,{'domain': 'www.dianxiaomi.com', 'expiry': 1656243957, 'httpOnly': True, 'name': 'dxm_t', 'path': '/', 'secure': False, 'value': 'MTYyNTEzOTk1NiFkRDB4TmpJMU1UTTVPVFUyITZhZWE4OWM2ZGY1MGQ5Yzg4YWY1ZDVjZDdkODAwNzA2'}
,{'domain': 'www.dianxiaomi.com', 'expiry': 1656243957, 'httpOnly': True, 'name': 'dxm_i', 'path': '/', 'secure': False, 'value': 'OTEzMjY3IWFUMDVNVE15TmpjITk3MGExNjNlODhjNDBkNzc5OWYzZmQ2YTVmOTM3NjRi'}
,{'domain': 'www.dianxiaomi.com', 'expiry': 1656243957, 'httpOnly': True, 'name': 'dxm_c', 'path': '/', 'secure': False, 'value': 'bW41MWdIZVMhWXoxdGJqVXhaMGhsVXchYTRmZmU5ZjhhMTFhNDRiNDIxYTM2ODc4N2ZjYjA0MTc'}
,{'domain': 'www.dianxiaomi.com', 'expiry': 1656243957, 'httpOnly': True, 'name': 'dxm_w', 'path': '/', 'secure': False, 'value': 'OGExNzA2YzI1ZDU2MjU4OGMxN2JhNmY2YzQyODM5MWEhZHowNFlURTNNRFpqTWpWa05UWXlOVGc0WXpFM1ltRTJaalpqTkRJNE16a3hZUSEyMTg0ZDUxNTlhODQ5YTczYzQ4N2QwM2RjOGJlNTlkNQ'}

]

script='''
function fn(x){
    let js={
    'agentProvideAuthDetailId': '21995249083604252',
    'country': 'US',
    'weight':x,
    'isDesc':0
        };
    let result;
    $.ajax({
    type:'post',
    url: "https://www.dianxiaomi.com/logisticFeeTemplate/calculateFeePageList.json",
    data:js,
    async:false,
    dataType: "json",
    success: function(data){result=data["logisticFeeList"][0]['discountprice'];}
    });
    return result;
};
return fn(%d);
'''
url = 'https://www.dianxiaomi.com/home.htm'
url0 = "https://www.dianxiaomi.com/amazonProduct/index.htm?dxmState=online"
class DXM():
	def __init__(self,brower:webdriver.Chrome):
		self.brower = brower
		self.brand_new = 'Crazedigi'
		self.id = {}
		self.set_wid()

	def __call__(self):
		self.get_in()

	#execute_script
	def es(self,script,*args):
		return self.brower.execute_script(script,*args)

	#添加cookie
	def add_cookies(self) -> None:
		for co in cookies:
			self.brower.add_cookie(co)

	#进店
	def get_in(self):
		self.brower.get(url)
		self.add_cookies()
		self.brower.get(url0)
		# self.es(script)


	def set_wid(self):
		self.id['main'] = self.brower.window_handles[0]

	#获取主窗口
	def get_wid(self)-> str:
		wid = self.id['main']
		return wid
	#添加创建窗口
	def add_nid(self,nid):
		self.id['nid'] = nid

	#是否有错误信息 errorMsgContent
	def iserrmsg(self) -> Union[bool,List[str]]:
		errs = self.esxpath('//*[@class="errorMsgContent"]')
		if len(errs) == 0:
			return False
		else:
			return [err.get_attribute('innerText') for err in errs]


	#是否是主窗口
	def ismain(self) -> bool:
		if self.brower.current_window_handle == self.id['main']:
			return True
		else:
			return False

	#取出创建窗口
	def pop(self) -> str:
		nid = self.id.pop('nid')
		return nid
	
	#关闭所以窗口（除了主窗口），并转到主窗口
	@property
	def closes(self):
		for b in self.brower.window_handles:
			try:
				self.brower.switch_to.window(b)
				if self.ismain():
					raise CloseException()
				self.brower.close()
			except CloseException as ce:
				print(ce)
		self.go_back0()

	#关闭当前窗口，并转到主窗口
	# @property
	def close(self):
		if self.ismain():
			raise CloseException()
		self.brower.close()
		self.brower.switch_to.window(self.id['main'])
		# return self.pop()

	#创建产品
	def click_btn(self):
		self.btn = self.brower.find_element_by_xpath('//button[contains(text(),"创建产品")]')
		# self.btn.click()
		self.es("arguments[0].click()",self.btn)
		self.add_nid(self.brower.window_handles[-1])
		self.brower.switch_to.window(self.id['nid'])
		# self.brower.implicitly_wait(5)
		self.store_btn = WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//button[@data-value="save-1" and @class="button btn-orange m-left10 toSubmit"]')))
		# self.store_btn=self.brower.find_element_by_xpath('//button[@data-value="save-1" and @class="button btn-orange m-left10 toSubmit"]')

	#获取节点
	def get_nodes(self):
		self.nodes:List[WebElement]=self.brower.find_elements_by_xpath('//div[contains(@class,"product-info-module-content onlineProductInfo")]')
	
	#获得节点0
	def get_div(self):
		self.div:List[WebElement] = self.brower.find_elements_by_xpath('//div[@class="product-info-module-content"]')

	#店铺信息 divv = //div[contains(@class,"product-info-module-content onlineProductInfo")]
	def set_dxminfo(self):
		#店铺账号
		self.shopid = self.nodes[0].find_element_by_xpath('.//select[@id="shopId"]')
		#站点选择
		self.site = self.nodes[0].find_element_by_xpath('.//select[@id="site"]')
		#产品分类
		self.category = self.nodes[0].find_element_by_xpath('.//select[@id="categoryHistoryId"]')
		#产品类型
		#feed_product_type = self.nodes[0].find_element_by_xpath('.//select[@id="feed_product_type"]')
		Select(self.shopid).select_by_index(1)
		# self.brower.implicitly_wait(10)
		Select(self.category).select_by_index(1)
		self.brower.implicitly_wait(10)
		#网络图片 .//button[contains(@onclick,"netUpload")]
		self.net_img = self.nodes[2].find_element_by_xpath('.//button[contains(@onclick,"netUpload")]')
		#输入框	//div[@id="imgModal"]//textarea[@id="netImgUrl"]
		self.input_img = self.nodes[2].find_element_by_xpath('//div[@id="imgModal"]//textarea[@id="netImgUrl"]')
		#添加	//div[@id="imgModal"]//button[contains(@onclick,"downImgFromUrl")]
		self.btn_img = self.nodes[2].find_element_by_xpath('//div[@id="imgModal"]//button[contains(@onclick,"downImgFromUrl")]')
		
		#divv[4]价格与运输
		#价格 	.//input[@id="standardPriceId"]
		self.picer = self.nodes[4].find_element_by_xpath('.//input[@id="standardPriceId"]')
		#数量	.//input[@id="quantityId"]
		self.quantity = self.nodes[4].find_element_by_xpath('.//input[@id="quantityId"]')
		self.brower.execute_script('arguments[0].value="5";',self.quantity)
		#self.quantity.send_keys('50')
		#时间	.//input[@id="fulfillment_latency"]
		self.deal = self.nodes[4].find_element_by_xpath('.//input[@id="fulfillment_latency"]')
		self.brower.execute_script('arguments[0].value="5";',self.deal)
		#self.deal.send_keys('5')
		

		#divv[5]描述信息 和 5点
		#5点		.//textarea[@name="bulletPoints"][0-4]
		# 	.//textarea[@id="bulletPointOneId"]
		# 	.//textarea[@id="bulletPointTwoId"]
		# 	.//textarea[@id="bulletPointThreeId"]
		# 	.//textarea[@id="bulletPointFourId"]
		# 	.//textarea[@id="bulletPointFiveId"]
		self.points = self.nodes[5].find_elements_by_xpath('.//textarea[@name="bulletPoints"]')
		
		#iframe	.//div[@id="cke_1_contents"]/iframe
		self.frame  = self.nodes[5].find_element_by_xpath('.//div[@id="cke_1_contents"]/iframe')

		#divv[6]关键词信息 .//textarea[@id="searchTermsOneId"]
		self.search = self.nodes[6].find_element_by_xpath('.//textarea[@id="searchTermsOneId"]')
		

		#===============================================================================================
		

		#div[0] 店小秘信息
		#店小秘分类	.//button[@data-names="treeSelectBtn"]
		self.dxm_category = self.div[0].find_element_by_xpath('.//button[@data-names="treeSelectBtn"]')
		#self.dxm_category.click()
		#户外用品  	.//ul[@data-names="treeSelect"]/li[@groupid="2753455"]
		#			.//ul[@data-names="treeSelect"]/li[@groupname="户外用品"]
		self.btn_category = self.div[0].find_element_by_xpath('.//ul[@data-names="treeSelect"]/li[@groupname="户外用品"]//a')
		self.brower.execute_script("arguments[0].click();",self.btn_category)
		#self.btn_category.click()
		
		
		#div[1] 产品信息

		#SKU			.//input[@id="skuId"]
		self.sku = self.div[1].find_element_by_xpath('.//input[@id="skuId"]')
		#产品标题		.//input[@id="productName"]
		self.title = self.div[1].find_element_by_xpath('.//input[@id="productName"]')

		#产品ID(upc)		.//input[@id="standardProductId"]
			#	输入框	.//input[@id="standardProductId"]
		# 输入upc
		# self.get_upc()
		# self.upc = self.div[1].find_element_by_xpath('.//input[@id="standardProductId"]')
		# self.brower.execute_script("arguments[0].value='1234' ",self.upc)
			#	自动获取	.//button[@class="button btn-determine m-left10"]
			#	upc选择	.//select[@id="upcSelect"]
				
		
		#品牌			.//input[@id="brandId"]
		self.brand = self.div[1].find_element_by_xpath('.//input[@id="brandId"]')
		#self.brand.send_keys(self.brand_new)
		self.brower.execute_script("arguments[0].value='{}';".format(self.brand_new),self.brand)
		#制造商			.//input[@id="designerId"]
		self.designer = self.div[1].find_element_by_xpath('.//input[@id="designerId"]')
		#self.designer.send_keys(self.brand_new)
		self.brower.execute_script("arguments[0].value='{}';".format(self.brand_new),self.designer)

	#获取upc
	def get_upc0(self,poolName='2021-06-25'):	
		upcSelect = self.brower.find_element_by_xpath('//select[@id="upcSelect"]')
		self.brower.execute_script("arguments[0].value='{}'".format(poolName),upcSelect)
		btn_upc = self.brower.find_element_by_xpath('//*[@class="button btn-determine m-right10 upcBatchEditBtn"]')
		# self.brower.execute_script("arguments[0].click()",btn_upc)
		self.brower.execute_script("amzProAdd.getUpcNumber()")
	
	def get_upc(self,poolName='2021-06-25'):
		auto_upc = self.brower.find_element_by_xpath('//button[@class="button btn-determine m-left10"]')
		self.brower.execute_script("arguments[0].click()",auto_upc)
		upcSelect = WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="upcSelect"]')))
		self.brower.implicitly_wait(5)
		# 通过 selenium 控制 select 元素
		Select(upcSelect).select_by_value(poolName)

		# 通过 JavaScript 控制 select 元素
		# self.es(f"arguments[0].value='{poolName}'",upcSelect)

		btn_upc = self.brower.find_element_by_xpath('//*[@class="button btn-determine m-right10 upcBatchEditBtn"]')
		self.brower.execute_script("arguments[0].click()",btn_upc)
		# self.brower.execute_script("amzProAdd.getUpcNumber()")

	def set_info(self,**kw):
		#上传图片
		# self.net_img.click()
		#self.brower.execute_script("arguments[0].click();",self.net_img)
		#self.brower.implicitly_wait(5)
		urls=''
		for url in kw['imgs']:
			urls+=url+r'\n'
		self.brower.execute_script("arguments[0].value='{}';".format(urls),self.input_img)
		#self.btn_img.click()
		self.brower.execute_script("arguments[0].click();",self.btn_img)
		#self.picer.send_keys(kw['picer'])
		picer = self.calc(kw['picer'],kw['weight'])
		self.brower.execute_script("arguments[0].value='{}';".format(picer),self.picer)
		#self.sku.send_keys(kw['sku'])
		self.brower.execute_script("arguments[0].value='{}';".format(kw['sku']),self.sku)
		#self.title.send_keys(kw['title'])
		self.brower.execute_script("arguments[0].value='{}';".format(kw['title']),self.title)
		#self.search.send_keys(kw['search'])
		self.brower.execute_script("arguments[0].value='{}';".format(kw['search']),self.search)

		'''
		for i in range(0,len(kw['points'])):
			self.points[i].send_keys(kw['points'][i])
		'''
		for (point_e,point_d) in zip(kw['points'],self.points):
			#point_d.send_keys(point_e)
			self.brower.execute_script("arguments[0].value='{}';".format(point_e),point_d)
		
		
		self.brower.switch_to.frame(self.frame)
		bd = self.brower.find_element_by_xpath('//body')
		# bd.send_keys(kw['desc'])
		self.brower.execute_script("arguments[0].innerHTML='{}'".format(kw['desc']),bd)
		self.brower.switch_to.default_content()
	
	def fnf(self):
		for b in self.brower.window_handles:
			try:
				self.brower.switch_to.window(b)
				if self.ismain():
					raise CloseException()
				store_btn = WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//button[@data-value="save-1" and @class="button btn-orange m-left10 toSubmit"]')))
				self.set_frame()
				self.es("arguments[0].click()",store_btn)
				hh=WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
				WebDriverWait(self.brower,5).until(EC.visibility_of(hh))
			except CloseException as ce:
				print(ce)
			else:
				self.close()
		self.go_back0()

	def set_frame(self) -> None:
		frame=self.xpath('//div[@id="cke_1_contents"]/iframe')
		if not frame:
			print("Don't found the tag of iframe")
		else:
			iprice = self.xpath('//input[@id="standardPriceId"]')
			price = iprice.get_attribute('value')
			# print(price)
			self.brower.switch_to.frame(frame)
			bd = self.xpath('//body')
			string = bd.get_attribute('innerHTML')
			weight = util.get_weight(string)
			string = util.strong(string)
			self.es(f"arguments[0].innerHTML='{string}'",bd)
			# print(bd.get_attribute('innerHTML'))
			self.brower.switch_to.default_content()
			print("weight: %s" %weight)
			if weight != 0:
				fee = self.get_fee(weight)
				prices = self.calc(price,fee)
				print("prices: %s" %prices)
				self.es(f"arguments[0].value='{prices}'",iprice)

	def fn(fnn):
		def fns(self):
			for b in self.brower.window_handles:
				try:
					self.brower.switch_to.window(b)
					if self.ismain():
						raise CloseException()
					fnn(self)
				except CloseException as ce:
					print(ce)
			self.go_back0()
		return fns
	
	@fn
	def gupcs(self):
		self.get_upc()
		self.brower.implicitly_wait(5)
		# time.sleep(0.5)


	def setfo(self,_ct="sports",_fpt="sportinggoods"):
		nodes = self.esxpath('//*[contains(@uid,"is_expiration_dated_product")] | //*[contains(@uid,"part_number")] | //*[contains(@uid,"size_name")]')
		ct = self.xpath('//select[@id="categoryType"]')
		fpt = self.xpath('//select[@id="feed_product_type"]')
		if ct.get_attribute('value') == "":
			self.es(f"arguments[0].value='{_ct}'",ct)
			self.es(f"arguments[0].value='{_fpt}'",fpt)
		if not ct.is_displayed() and fpt.get_attribute('value') == "":
			Select(fpt).select_by_value(f'{_fpt}')
			# self.es(f"arguments[0].value='{_fpt}'",fpt)
		# self.get_upc()
		if len(nodes) != 0:
			for node in nodes:
				if node.get_attribute("uid") == "is_expiration_dated_product":
					self.es("arguments[0].value='No'",node.find_element_by_xpath('.//select'))
				elif node.get_attribute("uid") == "part_number":
					self.es("arguments[0].value='1'",node.find_element_by_xpath('.//input'))
				elif node.get_attribute("uid") == "size_name":
					self.es("arguments[0].value='Small'",node.find_element_by_xpath('.//input'))
		else:
			print("'%s'" %self.brower.current_window_handle)
			print('Don\'t Finded!')

	def setfos(self,_ct="sports",_fpt="sportinggoods"):
		for b in self.brower.window_handles:
			try:
				self.brower.switch_to.window(b)
				if self.ismain():
					raise CloseException()
				self.setfo(_ct,_fpt)
			except CloseException as ce:
				print(ce)
			# else:
			# 	self.brower.close()
		self.go_back0()

	@property
	def publish(self):
		for b in self.brower.window_handles:
			try:
				self.brower.switch_to.window(b)
				if self.ismain():
					raise CloseException()
				save = self.brower.find_element_by_xpath('//button[@data-value="save-2"]')
				self.es("arguments[0].click()",save)
				hh=WebDriverWait(self.brower,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
				WebDriverWait(self.brower,1).until(EC.visibility_of(hh))
			except CloseException as ce:
				print(ce)
			except TimeoutException as te:
				print(te)
				errm = self.iserrmsg()
				if isinstance(errm,bool):
					hh=WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
					WebDriverWait(self.brower,5).until(EC.visibility_of(hh))
				elif isinstance(errm,list):
					for err in errm:
						if 'ParentSku重复' in err:
							print('长传产品重复')
							break
						elif '产品Id' in err:
							self.get_upc()
							WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[contains(text(),"获取成功")]')))
							self.es("arguments[0].click()",save)
							hh=WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
							WebDriverWait(self.brower,5).until(EC.visibility_of(hh))
							# self.close()
							break
				pass
			else:
				self.brower.close()
		self.go_back0()


	def edits(self,st):
		for b in self.brower.window_handles[1:]:
			self.brower.switch_to.window(b)
			self.es(sr.format(st))
		# self.go_back()

	# 确定窗口
	def judge(self):
		ntl='添加Amazon产品'
		wtl = self.brower.title
		if not ntl in wtl:
			self.brower.switch_to.window(self.brower.window_handles[-1])

	@property
	def edit_btn(self):
		btns = self.brower.find_elements_by_xpath('//a[text()="编辑"]')
		for btn in btns:
			self.es("arguments[0].click()",btn)

	# 单个
	def main(self,js):
		# self.click_btn()
		try:
			self.judge()
			self.get_nodes()
			self.get_div()
			self.set_dxminfo()
			self.set_info(**js)
			self.dxm_store()
			hh=WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
			WebDriverWait(self.brower,5).until(EC.visibility_of(hh))
		except Exception as e:
			print(e)
		else:
			self.close()
		finally:
			self.go_back()

	# 多个
	def mains(self,jss):
		for js in jss:
			# try:
			self.click_btn()
			self.get_nodes()
			self.get_div()
			self.set_dxminfo()
			self.set_info(**js)
			self.dxm_store()
			# self.brower.execute_script("arguments[0].click()",self.store_btn)
			WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModalLabel" and text()="消息提示"]')))
			# input('?')
			# else:
			self.close()
		# finally:
			self.go_back()



	#返回主页面
	def go_back0(self,_id:Union[int,str] = 0) -> None:
		if isinstance(_id,int):
			self.brower.switch_to.window(self.brower.window_handles[_id])
		elif isinstance(_id,str):
			self.brower.switch_to.window(_id)

	def go_back(self) -> None:
		if self.id['main'] == self.brower.window_handles[0]:
			self.brower.switch_to.window(self.id['main'])
			self.set_wid()
		else:
			self.go_back0()

	#保存
	def dxm_store(self):
		self.brower.execute_script("arguments[0].click()",self.store_btn)
		# self.store_btn.click()
		# 
	#获取运费
	def get_fee(self,weight:str) -> int:
		weight = int(float(weight))
		if weight == 0:
			weight = 500
		f = self.es(script %weight)
		if not f:
			return 200
		return f

	def finde(self,xpath:str,timeout=1) -> Union[WebElement,None]:
		try:
			node:WebElement = WebDriverWait(self.brower,timeout=timeout).until(EC.presence_of_element_located((By.XPATH,xpath)))
		except Exception as te:
			print(te)
			return None
		else:
			return node
		pass

	def xpath(self,xpath:str) -> Union[None,WebElement]:
		try:
			node:WebElement = self.brower.find_element_by_xpath(xpath)
		except NoSuchElementException as e:
			print(e)
			return None
		else:
			return node
	
	def esxpath(self,xpath):
		return self.brower.find_elements_by_xpath(xpath)
	

	#售价计算calculate
	def calc(self,x:str,y:str) -> str:
		x=float(x)
		print("x",x)
		y=self.get_fee(y)
		y=float(y)
		print("y",y)
		result = (x+y)/(1-0.2-0.15)/6.3
		print("result",result)
		return '%.1f9'%result
		
	def pro_info(self,kws):
		self.go_back0(-1)
		url = "https://www.dianxiaomi.com/dxmCommodityProduct/openAddModal.htm?id=&type=0&editOrCopy=0"
		# self.brower.get(url)
		option_name = 'jiazhichun'
		for kw in kws:
			ishidden = True
			self.brower.get(url)
			proid = self.xpath('//*[@id="proSku"]')
			namecn = self.xpath('//*[@id="proName"]')
			namen = self.xpath('//*[@id="proNameEn"]')
			img = self.xpath('//*[@id="webImgUrl"]')
			btn_img = self.xpath('//button[contains(@onclick,"addWebUrl")]')
			
			checkbox = self.xpath('//*[@name="warehouse"]')
			
			btn_st = self.xpath('//div[@class="pull-right"]//button[contains(text(),"保存")]')

			self.es("arguments[0].value='{}'".format(kw.get('_sku')),proid)
			self.es("arguments[0].value='{}'".format(kw.get('titlecn')),namecn)
			self.es("arguments[0].value='{}'".format(kw.get('title')),namen)
			self.es("arguments[0].value='{}'".format(kw.get('imgs')[0]),img)
			self.es("arguments[0].click()",btn_img)
			# self.es("arguments[0].checked='true'",checkbox)
			if not self.es("return arguments[0].checked",checkbox):
				self.es("arguments[0].click()",checkbox)
			# 保存
			self.es("arguments[0].click()",btn_st)
			WebDriverWait(self.brower,5).until(EC.presence_of_element_located((By.XPATH,'//*[@class="alert-successGreen"]//*[contains(text(),"保存成功")]')))

		



if __name__ == '__main__':
	print(cookies)
	#start steps
	br=webdriver.Chrome()
	dx=DXM(br)
	dx.get_in()