# dianxiaomi

# 账号密码

    #	gzqupdate
	#	Abc123321.

# 创建产品

``` xpath

//button[contains(@class,"btn btn-primary btn-block")]
//button[@class="btn btn-primary btn-block"]
//button[contains(text(),"创建产品")]
//button[contains(@class,"btn btn-primary btn-block")]
//button[@class="btn btn-primary btn-block"]
//button[contains(text(),"创建产品")]
//button[contains(@class,"btn btn-primary btn-block")]
//button[@class="btn btn-primary btn-block"]
//button[contains(text(),"创建产品")]

```

# div = //div[@class="product-info-module-content onlineProductInfo"]

0-6
# divv = //div[contains(@class,"product-info-module-content onlineProductInfo")

0-7
# div[0] divv[0]店铺信息
	#店铺账号	.//select[@id="shopId"]
	#站点选择	.//select[@id="site"]
	#产品分类	.//select[@id="categoryHistoryId"]
	#产品类型	.//select[@id="feed_product_type"]
#div[1] divv[1]属性信息 ？

# divv[2]图片信息	//div[@class="product-info-module-content onlineProductInfo amazon-img-info"]
	#
	#	网络图片 	.//button[contains(@onclick,"netUpload")]
	#	输入框		//div[@id="imgModal"]//textarea[@id="netImgUrl"]
	#	添加			//div[@id="imgModal"]//button[contains(@onclick,"downImgFromUrl")]
#div[2] divv[3]变种信息？

#div[3]	divv[4]价格与运输
	#价格 	.//input[@id="standardPriceId"]
	#数量	.//input[@id="quantityId"]
	#时间	.//input[@id="fulfillment_latency"]
#div[4]	divv[5]描述信息 和 5点
	#iframe	.//div[@id="cke_1_contents"]/iframe

	#5点		.//textarea[@name="bulletPoints"][0-4]
			.//textarea[@id="bulletPointOneId"]
			.//textarea[@id="bulletPointTwoId"]
			.//textarea[@id="bulletPointThreeId"]
			.//textarea[@id="bulletPointFourId"]
			.//textarea[@id="bulletPointFiveId"]
#div[5]	divv[6]关键词信息
	#	.//textarea[@id="searchTermsOneId"]
	#




# div = //div[@class="product-info-module-content"]
0-1
#div[0] 店小秘信息（注：下列信息，仅在店小秘系统生效）
	#店小秘分类	.//button[@data-names="treeSelectBtn"]
	#户外用品  	.//ul[@data-names="treeSelect"]/li[@groupid="2753455"]
	#			.//ul[@data-names="treeSelect"]/li[@groupname="户外用品"]
#div[1] 产品信息

#SKU			.//input[@id="skuId"]
#产品标题		.//input[@id="productName"]
#产品ID(upc)		.//input[@id="standardProductId"]
	#	输入框	.//input[@id="standardProductId"]
	#	自动获取	.//button[@class="button btn-determine m-left10"]
	#	upc选择	.//select[@id="upcSelect"]
	#	
#品牌			.//input[@id="brandId"]
#制造商			.//input[@id="designerId"]


#保存		
	# self.brower.switch_to_frame()                   切换到iframe上(过时了)
	# self.brower.switch_to.frame()                   切换到iframe上（推荐）
	# self.brower.switch_to.parent_frame()			  切换回父级页面
	# self.brower.switch_to.default_content()         切换回原主页面
