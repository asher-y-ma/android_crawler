#coding:utf-8:
import urllib
import re
import download
import socket
socket.setdefaulttimeout(10.0)
def get_information(url):
    list = []
    try:
        response = urllib.urlopen(url)
        test = response.read()
    except Exception,e:
        test = ''
        pass
        
    m1 = re.search('data-name="(.*?)"',test)
    try:
        name = m1.group(1) #apk文件名
    except Exception, e:
        name = '0'
    
    
    m2 = re.search('href="(.*?)".*?下载 APK 文件',test)
    try:
        down_url = m2.group(1)
    except Exception,e:
        down_url = '0'
   
    url = down_url #下载url    
    
    m3 = re.search('data-install="(.*?)"',test)
    try:
        install_num = m3.group(1) #安装次数
    except Exception,e:
        install_num='0'
    
    
    m4 = re.search('data-like="(.*?)"',test)
    try:
        likes = m4.group(1) #喜欢次数
    except Exception,e:
        likes='0'
        
    m5 = re.findall('SoftwareApplicationCategory.*?>(.*?)<',test)

    category = ''
    for categ in m5:
        category+=categ+' '  #分类
    
    m6 = re.search('itemprop="description">(.*?)</div',test)
    try:
        description = m6.group(1)
    except Exception,e:
        description = '0'
    description = description.replace('<br />',' ')
    if len(description)>1000:
        description = description[0:1000] #apk描述
    
    md5 = download.down(down_url) # md5 值
    list.append(name)
    list.append(url)
    list.append(category)
    list.append(description)
    list.append(install_num)
    list.append(likes)
    list.append(md5)
    return list
if __name__=='__main__':
    url = 'http://www.wandoujia.com/apps/com.wandoujia.roshan'
    get_information(url)