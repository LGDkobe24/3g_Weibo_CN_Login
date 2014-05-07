# -*- coding: utf-8 -*-
from WeiboCN import Fetcher

from lxml import etree
import lxml
import lxml.html.soupparser as sper

import re
import time
from datetime import *
import os

LogIner = Fetcher()
LogIner.login('fuck@sina.com', 'fucksina', 'cookies.lwp')
#content = LogIner.fetch('http://weibo.cn/cqdx?page=1')
content = LogIner.fetch('http://weibo.cn/xiena?page=1')
#content = LogIner.fetch('http://weibo.cn/pku?page=400')

tree = etree.HTML(content)
subtree = tree.xpath("//p/text()|//p/a")

path = os.path.abspath('.')
filename = 'ParserSave.txt'
f = open(path+filename,'a+')

contentFlag = False
sectionFlag = True
section = ''
print len(subtree)

for node in subtree:
    '''
    if isinstance(node,lxml.etree._ElementUnicodeResult):
        print "Current node is:",node.strip().replace(u'\xa0','')
    elif isinstance(node,lxml.etree._ElementStringResult):
        print "Current node is:",node
    else:
        print "Current node is:",node.text
    print "Current contents are:", section
    '''
    if contentFlag == True:
        if sectionFlag == True:
            if isinstance(node,lxml.etree._Element):
                if node.text is not None:
                    shortnode = node.text.strip()
                if isinstance(shortnode,unicode):
                    utftext = shortnode.encode('utf-8')
                    if not (re.match(r'\B赞\[[0-9]*\]\B',utftext) or re.match(r'\B转发\[[0-9]*\]\B',utftext) or re.match(r'\B评论\[[0-9]*\]\B',utftext) or re.match(r'\B收藏\B',utftext) or re.match(r'\B原图\B',utftext)):  #剔除掉“赞，转发，评论，收藏”
                        section = section + utftext
                elif not (re.match(r'\B赞\[[0-9]*\]\B',shortnode) or re.match(r'\B转发\[[0-9]*\]\B',shortnode) or re.match(r'\B评论\[[0-9]*\]\B',shortnode) or re.match(r'\B收藏\B',shortnode) or re.match(r'\B原图\B',shortnode)):
                    section = section + shortnode
            elif isinstance(node,lxml.etree._ElementStringResult):
                shortnode = node.strip().replace(u'\xa0','')
                reresult_otherday = re.search(r'[0-9]*月[0-9]*日\s[0-9]*:[0-9]*来自[\S]*',shortnode.encode('utf-8'))    #本年内，只有日期
                reresult_today = re.search(r'今天\s[0-9]*:[0-9]*来自[\S]*',shortnode.encode('utf-8'))   #今天内
                reresult_minutesago = re.search(r'[0-9]+分钟前来自',shortnode.encode('utf-8')) #本小时内
                reresult_otheryear = re.search(r'[0-9]+-[0-9]+-[0-9]+\s[0-9]+:[0-9]+:[0-9]+来自[\S]*',shortnode.encode('utf-8'))  #非本年内
                if reresult_otherday:
                    #print "The time is ",reresult_otherday.group()
                    section = section + reresult_otherday.group() 
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''               
                elif reresult_today:
                    moment = re.search(r'[0-9]*:[0-9]*',shortnode.encode('utf-8')).group()
                    #machinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                    daynow = datetime.now().strftime('%Y-%m-%d ')
                    date = daynow + moment
                    section = section + date
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif reresult_minutesago:
                    timegap = re.search(r'[0-9]+',shortnode.encode('utf-8')).group()
                    timenow = datetime.now()
                    timeposter = timenow + timedelta(seconds=(timegap*60))
                    date = timeposter.strftime('%Y-%m-%d %H:%M')
                    section = section + date
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif reresult_otheryear:
                    section = section + shortnode.encode('utf-8')
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif not re.match(r'[-]+',shortnode.encode('utf-8')):
                    section = section + shortnode.encode('utf-8')
            elif isinstance(node,lxml.etree._ElementUnicodeResult):
                shortnode = node.strip().replace(u'\xa0','')
                reresult_otherday = re.search(r'[0-9]*月[0-9]*日\s[0-9]*:[0-9]*来自[\S]*',shortnode.encode('utf-8'))  #本年内，只有日期
                reresult_today = re.search(r'今天\s[0-9]*:[0-9]*来自[\S]*',shortnode.encode('utf-8')) #今天内
                reresult_minutesago = re.search(r'[0-9]+分钟前来自',shortnode.encode('utf-8')) #本小时内
                reresult_otheryear = re.search(r'[0-9]+-[0-9]+-[0-9]+\s[0-9]+:[0-9]+:[0-9]+来自[\S]*',shortnode.encode('utf-8'))  #非本年内
                if reresult_otherday:
                    #print "The time is ",reresult_otherday.group()
                    section = section + reresult_otherday.group() 
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''               
                elif reresult_today:
                    moment = re.search(r'[0-9]*:[0-9]*',shortnode.encode('utf-8')).group()
                    #machinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                    daynow = datetime.now().strftime('%Y-%m-%d ')
                    date = daynow + moment
                    section = section + date
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif reresult_minutesago:
                    timegap = re.search(r'[0-9]+',shortnode.encode('utf-8')).group()
                    timenow = datetime.now()
                    timeposter = timenow + timedelta(seconds=(int(timegap)*60))
                    date = timeposter.strftime('%Y-%m-%d %H:%M')
                    section = section + date
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif reresult_otheryear:
                    section = section + shortnode.encode('utf-8')
                    f.write(section+'\n')
                    f.write('-------------------------\n')
                    section = ''
                elif not re.match(r'[-]+',shortnode.encode('utf-8')):
                    section = section + shortnode.encode('utf-8')

    if contentFlag == False:
        if isinstance(node,lxml.etree._Element) and node.text:
            if isinstance(node.text,unicode):
                if  re.match(r'筛选',node.text.encode('utf-8')):
                    contentFlag = True  #Content start.
                    sectionFlag = True  #Section record start.
            elif re.match(r'筛选',node.text):
                contentFlag = True  #Content start.
                sectionFlag = True  #Section record start.
f.close()
