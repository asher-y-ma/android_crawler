#coding:utf-8
from hashlib import md5

def md5_file(name):
    m = md5()
    a_file = open(name,'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
        
if __name__=='__main__':
    print md5_file('1.apk')
     
        