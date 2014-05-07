# -*- coding: utf-8 -*-
from WeiboCN import Fetcher

from lxml import etree
import lxml.html.soupparser as sper

import yaml
import os
import sys

def LoginInfo():
    #From yaml file import login info.
    if os.path.isfile('WeiboCN.yaml'):
        abspathfilename = os.path.abspath('WeiboCN.yaml')
        abspath,filename = os.path.split(abspathfilename)
        f_yaml = open(abspathfilename,'r')
        dic_yaml = yaml.load(f_yaml)
        username = dic_yaml['job']['login'][0]['username']
        password = dic_yaml['job']['login'][0]['password']
        return username,password
    else:
        print "Cannot find file 'WeiboCN.yaml'!"
        sys.exit()

def UserContentParser(uid):
    #Call 'ContentPageParser()' to crawl contents from one page to another.
    #Maintaining a name list to crawl in both memory and mysql.
    firstpage = LogIner.fetch('http://weibo.cn/' + str(uid))
    root = etree.HTML(firstpage)
    
def ContentPageParser():
    
LogIner = Fetcher()
LogIner.login('fuck@sina.com', 'fucksina', 'cookies.lwp')
content = LogIner.fetch('http://weibo.cn/cqdx?page=2')

root = etree.HTML(content)
