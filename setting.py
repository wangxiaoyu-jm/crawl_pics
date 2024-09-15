# -*- coding: utf-8 -*-
"""
文件描述：图片下载器
作者：wangxiaoyu
日期：2024 年 9 月 15 日]
"""

setting={
    #图片链接必须是png/jpg/jpeg结尾
    #单网页A内爬取图片，可传入该网页的链接
    'singel_url':'https://88188.meitu.lol/artdetail70909a.html',

    # 单网页A内有多个网页链接b/c/d……，每个网页链接b/c/d……内含有你需要爬取的图片，可传入网页A的链接
    'page_url':'https://88188.meitu.lol/arttype/22b.html',
    #单网页A内有多个网页链接b/c/d……，获取多个网页链接的xpath法则
    'mult_page_lst_xpath': '//*[@class="thumbnail"]/@href',
    #如果获得的page_url列表需要在前方拼接网站域名
    'add_website':'https://88188.meitu.lol',

    # 图片链接的xpath法则
    'src_xpath': '//*[@class="ttnr"]/img/@src',
    'file_name_xpath':'//*[@class="nrtitle"]/h1/text()',
    # 保存路径
    'save_path': 'images',
}
