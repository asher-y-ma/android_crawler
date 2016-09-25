#coding:utf-8
import database
import crawler
import download
import downjudge
import check_update
import context
success_num=0
fail_num=0
def is_unique(md5,db):
    return db.data_jud(md5)
def update(db):
    global success_num
    global fail_num
    success_num=0
    fail_num = 0
    print u'开始更新'
    past = open('log_file/urls.txt','r+')
    now = open('log_file/update.txt','r')
    past_list = past.readlines()
    now_list = now.readlines()
    exist_num = 0
    totle_num = len(now_list) - len(past_list)
    for url in now_list:
        if url not in now_list and url:
            
            print u'已下载:'+'%d'%exist_num +'/' +'%d'%totle_num + u'  成功个数:'+'%d'%success_num + u'  失败个数:' +'%d'%fail_num
            exist_num+=1
            date = context.get_information(url[0:-1])
            if date[6]==0:
                fail_num+=1
            else:
                success_num+=1
                try:
                    print '\n'+u'%s下载完成'%date[0].decode('utf-8')
                except Exception,e:
                    pass
                if not(is_unique(date[6],db)):
                    db.data_memory(date[0],date[1],date[2],date[3],date[4],date[5],date[6])
                past.write(url)
    past.close()
    now.close()
    print u'更新完成！'
        
def continue_downall(db):
    global success_num
    global fail_num
    success_num=0
    fail_num = 0
    downd = open('log_file/downed.txt','r+')
    urls = open('log_file/urls.txt','r')
    g_exist = downd.readlines()
    
    g_totle = urls.readlines()
    totle_num = len(g_totle)
    exist_num = len(g_exist)
    for url in g_totle:
        if url not in g_exist and url:
            
            print u'已下载:'+'%d'%exist_num +'/' +'%d'%totle_num + u'  成功个数:'+'%d'%success_num + u'  失败个数:' +'%d'%fail_num
            exist_num+=1
            date = context.get_information(url[0:-1])
            if date[6]==0:
                fail_num+=1
            else :
                success_num+=1
                try:
                    print '\n'+u'%s下载完成'%date[0].decode('utf-8')
                except Exception,e:
                    pass
                if not(is_unique(date[6],db)):
                    db.data_memory(date[0],date[1],date[2],date[3],date[4],date[5],date[6])
                downd.write(url)
    print u'所有应用下载完毕'
    downd.close()
    urls.close()
def downall(db):
    global success_num
    global fail_num
    success_num=0
    fail_num = 0
    
    downd = open('log_file/downed.txt','w')
    urls = open('log_file/urls.txt','r')
    
    g_totle = urls.readlines()
    totle_num = len(g_totle)
    exist_num = 0
    for url in g_totle:
        if url:
            
            print u'已下载:'+'%d'%exist_num +'/' +'%d'%totle_num + u'  成功个数:'+'%d'%success_num + u'  失败个数:' +'%d'%fail_num
            exist_num+=1
            date = context.get_information(url[0:-1])
            if  date[6]==0:
                fail_num+=1
            else:
                success_num+=1
                try:
                    print '\n'+u'%s下载完成'%date[0].decode('utf-8')
                except Exception,e:
                    pass
                if not(is_unique(date[6],db)):
                    db.data_memory(date[0],date[1],date[2],date[3],date[4],date[5],date[6])
                downd.write(url)
    print u'所有应用下载完毕'
    downd.close()
    urls.close()
                
db = database.db()               
db.create_db()
                
bool_check_update = crawler.start('log_file/urls.txt')
bool_continue_down = downjudge.judge_cont()
if bool_continue_down:
    continue_downall(db)
else:
    downall(db)
    
if bool_check_update:
    bool_update = check_update.ch_update()
    if bool_update:
        judge = raw_input('是否更新(y/n)：\n'.decode('utf-8').encode('gbk'))
        while True:
            judge.lower()
            if judge == 'y':
                update(db)
                break
            elif judge == 'n':
                break
            else:
                judge = raw_input('输入错误，请重新输入(y/n)：\n'.decode('utf-8').encode('gbk'))

        








