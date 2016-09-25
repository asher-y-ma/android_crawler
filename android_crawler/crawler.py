#coding:utf-8

import threading
import urllib
import re
import os
import time
import socket
socket.setdefaulttimeout(10.0)
g_mutex=threading.Condition()
g_pages=[] #从中解析所有url链接
g_queueURL=[] #等待爬取的url链接列表
g_existURL=[] #已经爬取过的url链接列表
g_failedURL=[] #下载失败的url链接列表
g_targetURL = []#目标页面
g_nowUrlList = [] #新的页面
class Crawler:
    def __init__(self,url,file_path):
        self.file_path = file_path
        self.url = url
        self.threadpool = []
        self.logfile = open('log_file/log.txt','w')
        self.failfile = open('log_file/failurls.txt','w')
        self.targetfile = open(self.file_path,'w')
        
    def crow(self):
        global g_targetURL
        global g_queueURL
        global g_failedURL
        g_queueURL.append(self.url)
        while(len(g_queueURL)!=0):
            for i in range(0,len(g_queueURL)):
                self.logfile.write(g_queueURL[i]+'\n')
            self.downloadall()
        self.logfile.close()
        for url in g_failedURL:
            g_queueURL.append(url)
        self.downloadall()
        for url in g_failedURL:
            self.failfile.write(url+'\n')
        self.failfile.close()
        for url in g_targetURL:
            self.targetfile.write(url+'\n')
        self.targetfile.close()
            
            
    def downloadall(self):
        global g_nowUrlList
        global g_queueURL
        global g_existURL
        i=0
        while i<len(g_queueURL):
            j = 0
            print u'已爬取：%d页'%len(g_targetURL)
            while j<10 and i+j<len(g_queueURL):
                threadresult = self.download(g_queueURL[i+j])
                j+=1
            i+=j
            for thread in self.threadpool:
                thread.join(2)
            self.threadpool = []
        g_queueURL = []
        g_queueURL = list(set(g_nowUrlList)-set(g_existURL))
        g_nowUrlList = []
        
    def download(self,url):
        crawer = crawThread(url)
        self.threadpool.append(crawer)
        crawer.start()
    # def updateQueueURL(self):
        # global g_queueURL
        # global g_existURL
        # global g_pages
        # g_nowUrlList = []
        # for context in g_pages:
            # g_nowUrlList+= self.getUrl(context)
        # g_queueURL = list(set(g_nowUrlList)-set(g_existURL))
    # def getUrl(self,context):
        # global g_targetURL
        # m1 = re.findall('(http://www.wandoujia.com/apps/[^/]*?)"',context)
        # m2 = re.findall('href="(.*?)"',context,re.X)
        # for url in m1:
            # if url not in g_targetURL:
                # g_targetURL.append(url)
        # list2 = []
        # for url in m2:
            # if ('http://www.wandoujia.com/'  in url) and (url not in g_targetURL) and (url not in g_existURL) and (url not in list2) and ('binding' not in url) and ('download' not in url):
                # list2.append(url)
        # return list2
class crawThread(threading.Thread):
        global g_targetURL
        global g_mutex
        global g_nowUrlList
        global g_failedURL
        global g_queueURL
        def __init__(self,url):
            threading.Thread.__init__(self)
            self.url = url
        def run(self):
            try:
                response = urllib.urlopen(self.url)
                html = response.read()
            except Exception,e:
                g_mutex.acquire()
                g_existURL.append(self.url)
                g_failedURL.append(self.url)
                g_mutex.release()
                return None
            g_mutex.acquire()
            g_existURL.append(self.url)
            g_mutex.release()
            global g_targetURL
            m1 = re.findall('(http://www.wandoujia.com/apps/[^/]*?\.[^/]*?)"',html)
            m2 = re.findall('href="(.*?)"',html,re.X)
            for url in m1:
                g_mutex.acquire()
                if url not in g_targetURL:
                    g_targetURL.append(url)
                g_mutex.release()
            list2 = []
            for url in m2:
                g_mutex.acquire()
                if ('http://www.wandoujia.com/category'  in url) and (url not in g_targetURL) and (url not in g_existURL) and (url not in g_nowUrlList) and ('binding' not in url) and ('download' not in url):
                    g_nowUrlList.append(url)
                g_mutex.release()
def start(file_path):
    if os.path.exists('log_file/urls.txt'):
        urls = open('log_file/urls.txt','r')
        bool = urls.readline()
        if bool:
            judge = raw_input('是否检查更新(y/n)：\n'.decode('utf-8').encode('gbk'))
            while True:
                judge.lower()
                if judge == 'y':
                    return True
                elif judge == 'n':
                    return False
                else:
                    judge = raw_input('输入错误，请重新输入(y/n)：\n'.decode('utf-8').encode('gbk'))
        else:
            print u'开始爬取所有app的单独页'
            crawer = Crawler('http://www.wandoujia.com/category/app',file_path)
            crawer.crow()
            return False
    else :
        print u'开始爬取所有app的单独页'
        crawer = Crawler('http://www.wandoujia.com/category/app',file_path)
        crawer.crow()
        return False
if __name__ == '__main__':
    crawer =Crawler('http://www.wandoujia.com/category/app','urls.txt')
    crawer.crow()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    