# -*- coding: utf-8 -*-
"""
文件描述：图片下载器
作者：wangxiaoyu
日期：2024 年 9 月 15 日]
"""

import random
import time
from threading import Thread
from lxml import etree
import requests
import os
import re
#获取随机headers
def random_headers():
    # with open('headers.txt', 'r') as f:
    #     resp = f.read()
    #     result_list = re.findall('"User-Agent": "(.*?)"', resp)
    #     print(result_list)
    headers_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/15A372 Safari/602.1',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36']
    headers = random.choice(headers_list)
    return headers

def time_delay(t):
    time.sleep(t)
#获取随机ip
def random_proxy():
    # with open('proxies.txt', 'r') as f:
    #     resp = f.read()
    #     list = re.findall('[0-9]+.[0-9]+.[0-9]+.[0-9]+[:][0-9]+', resp)
    #     print(list)
    iplist = ['154.203.132.55:8080', '112.19.241.37:19999', '123.233.245.158:9080', '122.116.150.2:9000',
              '8.134.166.102:8080', '120.197.40.219:9002', '103.118.46.61:8080', '154.203.132.49:8090',
              '221.231.13.198:1080', '120.197.160.2:9002', '183.234.215.11:8443', '111.59.4.88:9002',
              '47.243.177.210:8088', '112.19.241.37:19999', '120.197.40.219:9002', '8.219.97.248:80',
              '125.77.25.177:8080', '111.160.204.146:9091', '60.12.168.114:9002', '125.77.25.177:8090',
              '39.105.27.30:3128', '183.221.221.149:9091', '120.197.40.219:9002', '154.203.132.49:8090',
              '203.19.38.114:1080', '112.51.96.118:9091', '122.116.150.2:9000', '222.88.167.22:9002',
              '183.234.215.11:8443', '122.116.150.2:9000', '111.59.4.88:9002', '103.118.46.61:8080',
              '8.213.151.128:3128', '123.13.218.68:9002', '122.116.150.2:9000', '112.118.60.145:80',
              '183.234.215.11:8443', '103.118.46.61:8080', '36.134.91.82:8888', '47.243.92.199:3128',
              '183.247.211.41:30001', '8.213.151.128:3128', '203.19.38.114:1080', '52.82.123.144:3128',
              '223.113.80.158:9091', '58.20.248.139:9002', '58.20.248.139:9002', '116.63.129.202:6000',
              '116.63.129.202:6000', '154.203.132.49:8090', '47.243.92.199:3128', '122.114.232.137:808',
              '120.197.40.219:9002', '154.85.58.149:80', '125.77.25.177:8080', '52.82.123.144:3128',
              '183.60.141.41:443', '125.77.25.177:8090', '125.77.25.178:8080', '125.77.25.178:8090']
    ipproxy = random.choice(iplist)
    return ipproxy
#requests访问
def get_html_by_requests(url, cookie, timeout, timedelay, referer):
    heaer = random_headers()
    proxy = random_proxy()
    headers = {
        "User-Agent": f"{heaer}",
        "Cookie": f"{cookie}",
        "referer": f"{referer}",

    }
    proxies = {
        'http': f'{proxy}'
    }
    try:
        resp = requests.get(url=url, timeout=timeout, headers=headers, proxies=proxies, stream=True)
        time_delay(t=timedelay)
        return resp
    except TimeoutError:
        resp = requests.get(url=url, timeout=timeout, headers=headers, proxies=proxies, stream=True)
        time_delay(t=timedelay)
        return resp
    except Exception:
        resp = requests.get(url=url, timeout=timeout, headers=headers, stream=True)
        time_delay(t=timedelay)
        return resp
    except:
        print(f'{url}--页面无响应！')

'''下载函数'''

def Make_os_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"创建目录 {directory} 成功")
    else:
        pass

def download_image(url, folder_name, file_name):
    """
    下载图片并保存到指定文件夹
    :param url: 图片的URL
    :param folder_name: 保存图片的文件夹名
    :param file_name: 保存图片的文件名
    """
    if 'http' in url:
        try:
            response = get_html_by_requests(url=url, timeout=20, timedelay=2, cookie=None, referer=None)
            if response.status_code == 200:
                with open(os.path.join(folder_name, file_name), 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print(f'代理下载：{file_name}下载成功！')
        except:
            response = requests.get(url=url, headers=random_headers())
            with open(os.path.join(folder_name, file_name), 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f'本机下载：{file_name}下载成功！')
    else:
        print(f'图片链接为：{url},非http网址无法下载，已跳过')
        pass

def set_file_name(url, x, index):
    if x == 1:
        file_name = re.findall('/([0-9A-z]+.jpg|jpeg|png)', url)[0]
        return file_name
    elif x == 2:
        index = int(index) - 3
        file_name = f'image_{str(index)}.jpg'
        return file_name
    else:
        print('设置文件名出错！')

def download_images_in_threads(url_list, folder_name, x):
    """
    使用多线程下载图片
    :param url_list: 图片URL的列表
    :param folder_name: 保存图片的文件夹名
    """

    Make_os_dir(directory=folder_name)

    threads = []
    for index, url in enumerate(url_list, x):
        # 假设每个文件名为 url 的最后一部分（去除了可能的查询字符串和片段）
        file_name = set_file_name(url=url, x=x, index=index)
        # 创建线程
        thread = Thread(target=download_image, args=(url, folder_name, file_name))
        threads.append(thread)
        thread.start()

        # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 示例链接列表


'''解析函数'''
def xpath(resp, xplaw):
    tree=etree.HTML(resp)
    lst=tree.xpath(f"{xplaw}")
    return lst

def add_str_front(lst, add_str):
    new_lst = [f'{add_str}' + str(item) for item in lst]
    return new_lst
