from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

#ERP-分销市场-产品信息
brand_new = 'Crazedigi'
un="lifutang"
pd="Aa1234567"
url="http://erp.mambacart.com/distribution/productList"
#产品列表
lis=brower.find_elements_by_xpath('//*[@id="page-wrapper"]//*[@class="mzt-card-grid_list"]/li[@class="mzt-card-grid_product"]') 
lis[1].click()

#关闭产品信息
brower.find_element_by_xpath('//*[@id="el-drawer__title"]/button').click()

#标题
title = brower.find_element_by_xpath('//*[@id="el-drawer__title"]/*[@role="heading"]').get_attribute('title')

#获取产品信息详情
node=brower.find_element_by_xpath('//*[@class="el-drawer__body"]')

#获取产品信息的图片
imgs=node.find_elements_by_xpath('.//div[@class="mzt-product-con"]//div[@class="mzt-uploader"]/ul//li')

#图片链接
imgs[0].find_element_by_xpath('.//img').get_attribute("src")

#产品编码
id_number=node.find_element_by_xpath('.//*[@class="mzt-detail-number"]/span[2]').text

#价格
picer = node.find_element_by_xpath('.//*[@class="mzt-skupicer"]').text

#选择英文描述信息
node.find_element_by_xpath('.//*[@id="tab-en_US"]').click()
pps=node.find_elements_by_xpath('.//*[@id="pane-en_US"]//div[@class="el-textarea"]/textarea')
#标题
title = pps[0].get_attribute("value")
#关键词
point=pps[1].get_attribute("value")

#五点 bullet point
search_terms=pps[2-6].get_attribute("value")

#描述
#iframe
iframe=node.find_element_by_xpath('.//*[@id="pane-en_US"]//iframe')
#转换到内
brower.switch_to_frame(iframe)


#brower.switch_to_frame()                   切换到iframe上(过时了)
#brower.switch_to.frame()                   切换到iframe上（推荐）
#brower.switch_to.default_content()         切换回原主页面


description = brower.find_element_by_xpath('//body').text

dianxiaomi

gzqupdate
Abc123321.

创建产品
//button[contains(@class,"btn btn-primary btn-block")]
//button[@class="btn btn-primary btn-block"]
//button[contains(text(),"创建产品")]



//div[@class="product-info-module-content onlineProductInfo"]
有6个
#1店铺信息
#
#2属性信息 （请勾选要展示的信息）
#3图片信息
#4价格与运输
#5描述信息
#6关键词信息
js=er.get_all()
dx.main(js)


reload(dxm)
dx=dxm.DXM(br)