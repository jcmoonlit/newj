import smtplib
from email.mime.text import MIMEText
import random
import csv,time

#邮件构建

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

link = 'https://www.amazon.com/dp/B08JYVM323?ref=myi_title_dp'
gold = 	17.99	#zhang
link0 = 'https://www.amazon.com/dp/B08JYN8BHX?ref=myi_title_dp'	
gold0 = 9.99	#main
text = '''Hello,
Nice to meet you...
Here just want to know do you have interest in testing and reviewing Flexible Cell Phone Tripod with Remote on Amazon.
It is the tripod link:
{}
If interest, pls firstly send us your Paypal account and we can firstly transfer the payment of the tripod (${}) to you for purchasing.
Thank you so much and Looking forward to your early reply..:)
I would really appreciate an honest review. Simply let me know where I can send you my product for free.
Best regards
'''
# content = text.format(link,gold)





class SendEm:
	def __init__(self,host,From,password,file,start,num,timesl=3):
		self.host = host
		self.From = From
		self.password = password
		self.file = file
		self.start = start
		self.num = num
		self.timesl = timesl


	def getMIMEText(self,To,subject,content,content_type="plain",charset="utf-8"):
		self.To = To
		msg = MIMEText(content,content_type,charset)
		msg['From'] = '\"%s\"<%s>'%(self.From,self.From)
		msg['To'] = '%s<%s>'%(To.split('@')[0],To)
		msg['Subject'] = subject
		msg['X-Mailer'] = 'Foxmail 7.2.17.57[cn]'
		#msg['Date'] = 'Fri, 21 May 2021 14:51:09 +0800'
		self.msg = msg
		#return msg.as_string()

	def getSMPT_SSL(self,port=465):
		try:
			self.server = smtplib.SMTP_SSL(host=self.host,port=port)
			print('#connected to host: %s' %self.host)
			#server.connect(host=host,port=port)
			res = self.server.login(self.From,self.password)
			print("#登录结果：{}".format(res))
			return self.server
		except Exception as e:
			print('#failed to connect to host: %S' %self.host)

	def sendMail(self):
		try:
			if isinstance(self.server,smtplib.SMTP_SSL):
				#print(self.msg.as_string())
				self.server.sendmail(self.From,self.To,self.msg.as_string())
				print('#Send a success!')
		except Exception as e:
			print(e)
			self.close()


	def close(self):
		try:
			self.server.close()
			print('#Server is closed!')
		except Exception as e:
			print(e)

	def toMail(self,subject,content,content_type="plain",charset="utf-8"):
		with open(self.file) as f:
			i = 1
			k = 1
			f_csv = csv.reader(f)
			for row in f_csv:
				if i>=self.start and i<=self.start+self.num-1:
					if i % 2 == 0:
						time.sleep(self.timesl)
					self.getMIMEText(row[0],random.choice(subject),content,content_type,charset)
					print('%s\tNo:%s\tnum:%s' %(row[0],i,k))
					self.sendMail()
					k+=1
				if k > self.num:
					#print("ok")
					break
				i+=1

if __name__ == '__main__':
	# good_163 = {
	# 	'host': 'smtp.163.com',
	# 	'From' :  'yanjcg@163.com',
	# 	'password': 'DFDZISPVRXXHKUBM', #授权码
	# 	'file': 'email.csv',
	# 	'start': 6675,
	# 	'num':	10
	# }

	good_dodohot = {
		'host': 'smtp.exmail.qq.com',
		'From': 'yanjaco@dodohot.com',
		'password': 'coJgPixCpFovaxyZ', #授权码
		'file': 'email.csv',
		'start': 8455,
		'num':	100
	}
	port = 465
	
	To = "yanjcg28@outlook.com"
	To0 = "jclovedove@icloud.com"
	# file = 'email.csv'
	# num = 10
	# start = 6675
	content = text.format(link,gold)
	se = SendEm(**good_dodohot)
	se.getSMPT_SSL()
	# se.getMIMEText(To0,random.choice(subject),content)
	# se.sendMail()
	se.toMail(subject,content,charset='us-ascii')
	se.close()
	
