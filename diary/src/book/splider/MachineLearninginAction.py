#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/25 16:30
# @Author  : niuliangtao
# @Site    : 
# @File    : MachineLearninginAction.py
# @Software: PyCharm

import re
import urllib

import requests
from bs4 import BeautifulSoup

github_root = "https://github.com"
github_raw = "https://raw.githubusercontent.com"

s1 = "https://raw.githubusercontent.com/apachecn/MachineLearning/python-2.7/LICENSE"
s2 = "https://raw.githubusercontent.com/apachecn/MachineLearning/blob/python-2.7/LICENSE"


def downLoadFile(url, title):
    url = url.replace("/blob", "")
    print("download file FROM \t" + url + "\t to \t" + title)

    if re.search("(jpg|png|jpeg)", title):
        urllib.urlretrieve(github_raw + url, title)
        #
        # r = requests.get(github_raw + url)
        # with open(title, 'wb') as f:
        #     f.write(r.content)
    else:
        url = github_raw + url
        print (url)
        req = requests.get(url)
        soup = BeautifulSoup(req.content.decode("gbk", "ignore"), 'lxml')

        with open(title, 'wb') as f:
            f.write(soup.find("p").text.decode("utf8", "ignore"))


def getPath(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content.decode('gbk', 'ignore'), 'lxml')
    # soup = BeautifulSoup(req.content, 'lxml')

    tables = soup.find("table", "files js-navigation-container js-active-navigation-container")

    for file_wrap in tables.find_all("tr", "js-navigation-item"):
        context = file_wrap.find("a", "js-navigation-open")
        path = context.attrs["href"]
        title = context.text
        print (path + "\t" + title)

        if 'octicon-file-directory' in file_wrap.find("td", "icon").find("svg").attrs["class"]:
            print "directory"

        elif 'octicon-file' in file_wrap.find("svg").attrs["class"]:
            print "file"
            downLoadFile(path, title)


if __name__ == '__main__':
    url = "https://github.com/apachecn/MachineLearning"
    getPath(url=url)
