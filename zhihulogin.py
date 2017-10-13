# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':  'gzip, deflate, br',
        'Accept-Language':  'en-US,en;q=0.5',
        'Cache-Control':  'max-age=0', #每次都会访问
        'Connection':  'keep-alive',
        'User-Agent':  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
    }
    session = requests.session()
    res = session.get('http://www.zhihu.com',headers = header).content    #bytes型的数据
    _xsrf = BeautifulSoup(res, "html.parser").find('input', attrs={'name': '_xsrf'})['value']

    login_data = {
        '_xsrf':_xsrf,                                      #跨站请求伪造
        'password':'549897521@qq.com',
        'remember_me':'true',
        'email':'dao1youdao'
    }
    session.post('https://www.zhihu.com/#signin',data = login_data,headers = header)
    res = session.get('http://www.zhihu.com')
    print(res.text)

if __name__ == '__main__':
    login()