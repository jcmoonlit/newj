import requests
import os
from lxml import etree
from getuser import User_Agent

#from html.parser import HTMLParser  # t =  HTMLParser().unescapse("&amp;")


def getHTML(url,ua):
    header0 = User_Agent.get_user_agent()
    header={
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }

    try:
        r = requests.get(url,headers=header,timeout=30)
        print("code:%s" %r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("code:%s" %r.status_code)
        print("failed to get!")
        return "failed to get!"

file = "foo1.txt"
file0 = 'foo.html'
def writeFile(filename,text,encoding="utf-8"):
    if not os.path.exists(filename):
       #print(file)
       fo = open(filename,'w',encoding=encoding)
       fo.write(text)
       fo.flush()
       fo.close()

    else:
       os.remove(filename)
       fo = open(filename,'w',encoding=encoding)
       fo.write(text)
       fo.flush()
       fo.close()
       print("ok")




def printCSV(filename,list,encoding="utf-8"):
    if os.path.exists(filename):
        os.remove(file)
        with open(filename,'a+',encoding="utf-8") as fo:
            #fo.truncate() 清空文件 
            for text in list:
                fo.write(text+',\n')
            fo.flush()
            fo.close()
    else:
        with open(filename,'w',encoding="utf-8") as fo:
            for text in list:
                fo.write(text+',\n')
            fo.flush()
            fo.close()


if __name__ == '__main__':
    url0='https://www.amazon.co.uk/b/?node=118424031&ref_=Oct_s9_apbd_odnav_hd_bw_b80tEt_1&pf_rd_r=CXS9NP9QK3G5MV41YBC1&pf_rd_p=8c78711b-b171-5dbb-82a4-78ed9b688f14&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=118423031'
    url="https://www.amazon.co.uk/s?k=Eye+Make-up&i=beauty&rh=n%3A118424031&page="
    host="https://www.amazon.co.uk"
    ua = UserAgent()
    page = input('PLS enter URL: \n')
    url = '%s%s' %(url,page)
    #print(url)
    html0 = getHTML(url,ua)
    writeFile(file0,html0)
    html = etree.HTML(html0)
    print(html)
    list0 = []
    #jaco = etree.parse("C:/Users/Administrator/Desktop/new/jaco.html",etree.HTMLParser(encoding='utf-8'))
    
    #html_data = html.xpath('//a[@class="a-link-normal" and @href!="#" and span < 100]')
    #html_data1 = html.xpath('//a[@class="a-link-normal" and @href!="#" ]')
    #html_data2 = html.xpath('//a[@class="a-link-normal" and @href!="#" ]/span[@class="a-size-base"]/text()')
    html_data0 = html.xpath('//a[@class="a-link-normal" and @href!="#"]/span[@class="a-size-base"]/..')
    
    print(" jj:",len(html_data0))
    #print(html_data2)
    #print(html_data)
    for node in html_data0:
        n = node.xpath('.//span[@class="a-size-base"]')
        st = etree.tostring(n[0],encoding="utf-8")
        print("n: %s" %st)
        strr = etree.tostring(node,encoding="utf-8")
        print("node：%s" %strr)
        if int(''.join(node[0].text.split(','))) >= 100:
            #print(''.join([host,node.get("href").split('#')[0]]),node[0].text)
            print(node[0].text)
            list0.append(''.join([host,node.get("href").split('#')[0]]))

      #print(str(strr))
      
    #strr = etree.tostring(html_data[0],encoding="utf-8")
    # print('=============================')
    # printCSV(file,list0)