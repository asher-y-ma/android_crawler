#coding utf-8

import crawler

def ch_update():
    update_file = 'log_file/update.txt'
    crawer = crawler.Crawler('http://www.wandoujia.com/category/app',update_file)
    crawer.crow()
    past = open('log_file/urls.txt','r')
    now = open('log_file/update.txt','r')
    past_list = past.readlines()
    now_list = now.readlines()
    if len(now_list)>len(past_list):
        past.close()
        now.close()
        print u'有更新'
        return True
    else:
        past.close()
        now.close()
        print u'没有更新'
        return False
        

            
    
    