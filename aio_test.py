import asyncio
import random
import time
 
import aiohttp
import aiofiles
import requests
from lxml import etree
import os
import re
from fake_useragent import UserAgent
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport
 
 
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
 
    return wrapper
 
 
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
ua = UserAgent()
headers = {'User-Agent': ua.random, 'Referer': 'http://www.tulishe.com'}
 
 
class tulishe:
    def __init__(self):
        self.title = None
        self.num = 1
        self.write_num = 1
        # self.proxy = requests.get("http://127.0.0.1:5010/all/").json()
 
    async def get_url(self, url):
        async with aiohttp.ClientSession() as client:
            async with client.get(url, headers=headers) as resp:
                if resp.status == 200:
                    # print(await resp.text())
                    return await resp.text()
 
    async def html_parse(self, html):
        semaphore = asyncio.Semaphore(5)
        html_parse = etree.HTML(html)
        # title_list = html_parse.xpath('//div[@class="img"]//a[@rel="bookmark"]/@title')
        url_list = html_parse.xpath('//div[@class="img"]//a[@rel="bookmark"]/@href')
        tasks = [asyncio.create_task(self.img_parse(url, semaphore)) for url in url_list]
        await asyncio.wait(tasks)
 
    async def img_parse(self, h_url, sem):
        async with sem:
            semaphore = asyncio.Semaphore(7)
            h_html = await self.get_url(h_url)
            h_html_parse = etree.HTML(h_html)
            self.title = h_html_parse.xpath('//h1[@class="article-title"]/text()')[0]
            # print(self.title)
            # print(self.proxy)
            # print(random.choice(self.proxy)['proxy'])
            img_demo_url = h_html_parse.xpath(
                '//*[@id="gallery-2"]/div[@class="gallery-item gallery-blur-item"]/img/@src')
            img_url_list = []
            for d_url in img_demo_url:
                img_url = d_url.split('=')[1].split('&')[0]
                img_url_list.append(img_url)
            tasks = [asyncio.create_task(self.img_con(i_url, semaphore)) for i_url in img_url_list]
            await asyncio.wait(tasks)
            self.num = 1
 
    async def img_con(self, url, semaphore):
        # print(url)
        async with semaphore:
            async with aiohttp.ClientSession() as client:
                async with client.get(url, headers=headers) as resp:
                    if resp.status == 200:
                        img_con = await resp.read()
                        await self.write_img(img_con)
                        self.num += 1
 
    async def write_img(self, img_con):
        if not os.path.exists(self.title):
            os.makedirs(self.title)
            async with aiofiles.open(self.title + '/' + f'{self.num}.jpg', 'wb') as f:
                print(f'正在下载{self.title}/{self.num}.jpg')
                await f.write(img_con)
                self.write_num += 1
        else:
            async with aiofiles.open(self.title + '/' + f'{self.num}.jpg', 'wb') as f:
                print(f'正在下载{self.title}/{self.num}.jpg')
                await f.write(img_con)
                self.write_num += 1
 
    async def main(self, ):
        total_num = int(input('请输入要下载的页数：'))
        print('*'*74)
        start_time = time.time()
        for num in range(1, total_num + 1):
            url = f'http://www.tulishe.com/all/page/{num}'
            html = await self.get_url(url)
            print('开始解析下载>>>')
            await self.html_parse(html)
        end_time = time.time()
        print(f'本次共下载写真图片{self.write_num}张，共耗时{end_time - start_time}秒。')
 
 
a = tulishe()
# url = 'http://www.tulishe.com/wanghong'
asyncio.run(a.main())