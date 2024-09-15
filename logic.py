# -*- coding: utf-8 -*-
"""
文件描述：图片下载器
作者：wangxiaoyu
日期：2024 年 9 月 15 日]
"""
import time

import setting
import function as fun


def get_page_link(r):
    save_path=setting.setting["save_path"]
    fun.Make_os_dir(save_path)

    if r=='1':
        url=setting.setting["singel_url"]
        if url:
            print(f'正在爬取的网页：{url}')
            xplaw1 = setting.setting["src_xpath"]
            lst=response(url,xplaw1)
            title=lst[0][0]
            print(f'获取到标题{title}')
            time.sleep(2)
            print('开始下载图片……')
            srcs=lst[1]
            fun.download_images_in_threads(url_list=srcs,folder_name=f'{save_path}/{title}',x=2)
            print('图片下载完成')
            input('任意键返回菜单')
            menu()

    elif r=='2':
        url=setting.setting["page_url"]
        if url:
            xplaw2 = setting.setting["mult_page_lst_xpath"]
            lst=response(url,xplaw2)
            page_lst=lst[1]
            add_str=setting.setting["add_website"]
            if 'http' in add_str:
                end_url_lst=fun.add_str_front(lst=page_lst,add_str=add_str)
                xplaw3 = setting.setting["src_xpath"]
                for i in end_url_lst:
                    print(f'正在爬取的网页：{i}')
                    ti_src=response(i,xplaw3)
                    title=ti_src[0][0]
                    print(f'获取到标题{title}')
                    srcs=ti_src[1]
                    time.sleep(2)
                    print('开始下载图片……')
                    fun.download_images_in_threads(url_list=srcs, folder_name=f'{save_path}/{title}', x=2)

                print('图片下载完成')
                input('任意键返回菜单')
                menu()

            else:
                print(f'您的链接为：{str(page_lst)}')
                print('错误：非http网页，或网页无法访问！')
                input('任意键回到菜单')
                menu()

    else:
        print('请输入正确的菜单')
        menu()

def response(url,xplaw):
    resp = fun.get_html_by_requests(url=url, timeout=20, timedelay=2, referer=None, cookie=None).text
    lst = fun.xpath(resp, xplaw=xplaw)
    title=fun.xpath(resp,xplaw=setting.setting["file_name_xpath"])
    return title,lst

def menu():
    r = input('菜单：\n1.爬取单网页内的图片\n2.爬取单网页内多个网页链接内的图片\n>>')
    return r

