import requests
import os,time
from lxml import etree
from getuser import User_Agent

#from html.parser import HTMLParser  # t =  HTMLParser().unescapse("&amp;")

def getHTML(url):
    header0 = User_Agent.get_user_agent()
    header = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    #print('User-Agent: %s' %header['User-Agent'])
    try:
        r = requests.get(url,headers=header0,timeout=30)
        print('code:%s' %r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("failed to get!")
        return "failed to get!"

# def getFile(filename,text,encoding="utf-8"):
#     if not os.path.exists(filename):
#        #print(file)
#        fo = open(filename,'w',encoding=encoding)
#        fo.write(text)
#        fo.flush()
#        fo.close()

#     else:
#        os.remove(filename)
#        fo = open(filename,'w',encoding=encoding)
#        fo.write(text)
#        fo.flush()
#        fo.close()
#        print("ok")

def printCSV0(filename,list,encoding="utf-8"):
    if os.path.exists(filename):
        os.remove(file)
        with open(filename,'a+',encoding="utf-8") as fo:
            for text in list:
                fo.write(text+',\n')
                # list.remove(text)
            fo.flush()
            fo.close()
    else:
        with open(filename,'w',encoding="utf-8") as fo:
            for text in list:
                fo.write(text+',\n')
            fo.flush()
            fo.close()


def printCSV(filename,list,encoding="utf-8"):
    if os.path.exists(filename):
        with open(filename,'a+',encoding="utf-8") as fo:
            #fo.truncate() 清空文件 
            for text in list:
                fo.write(text+',\n')
                # list.remove(text)
            fo.flush()
            fo.close()
    else:
        with open(filename,'w',encoding="utf-8") as fo:
            for text in list:
                fo.write(text+',\n')
            fo.flush()
            fo.close()


def getNode(url,host):
    html0 = getHTML(url)
    html = etree.HTML(html0)
    list0 = []
    #html_data = html.xpath('//a[@class="a-link-normal" and @href!="#" and span < 100]')
    #html_data1 = html.xpath('//span[@class="a-size-base"]/..')
    #html_data2 = html.xpath('//a[@class="a-link-normal" and @href!="#" ]/span[@class="a-size-base"]/text()')
    
    html_data0 = html.xpath('//a[@class="a-link-normal" and @href!="#"]/span[@class="a-size-base"]/..')
    print("nod:",len(html_data0))
    for node in html_data0:
        # a = etree.tostring(node,encoding="utf-8")
        # print('<a>:%s'%a)
        strr = etree.tostring(node[0],encoding="utf-8")
        #print("node：%s" %strr)
        if node[0].text and int(''.join(node[0].text.split(','))) >= 100:
            #print(''.join([host,node.get("href").split('#')[0]]),node[0].text)
            # print(node[0].text)
            list0.append(''.join([host,node.get("href").split('#')[0]]))
    return list0

def main(url,start=1,page=None,sleep=5,host="https://www.amazon.co.uk",filename="foo.csv"):
    urls = []
    num = 0
    while start <= page:
        urls.append(url+str(start))
        start += 1
    for url in urls:
        print(url)
        l = getNode(url,host)
        num += len(l)
        printCSV(filename,l)
        print("num: %s" %num)
        time.sleep(sleep)


if __name__ == '__main__':
   
    host="https://www.amazon.co.uk"
    url="https://www.amazon.co.uk/s?k=Atomisers&i=beauty&rh=n%3A2799758031&page="
    file = "foo.csv"
    main(url,page=400)
    

    
    # list0 = getNode(url,host,headers)
    # print('=============================')
    # printCSV(file,list0)
    # l = getNode(url1,host,headers)
    # printCSV(file,l)