#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/25 16:30
# @Author  : niuliangtao
# @Site    : 
# @File    : MachineLearninginAction.py
# @Software: PyCharm

import csv
import random
import socket
import time

import http.client
import http.client
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://github.com/apachecn/MachineLearning"

    req = requests.get(url)
    soup = BeautifulSoup(req.content.decode('gbk', 'ignore'), 'lxml')

    print req.text.encode("utf-8")
