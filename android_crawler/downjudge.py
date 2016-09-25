#coding:utf-8
import os
import context
def judge_cont():
    if os.path.exists('log_file/downed.txt'):
        post = open('log_file/urls.txt','r')
        now = open('log_file/downed.txt','r')
        post_list = post.readlines()
        now_list = now.readlines()
        if len(post_list)>len(now_list):
            judge = raw_input('是否继续(y/n)：\n'.decode('utf-8').encode('gbk'))
            while True:
                judge = judge.lower()
                if judge == 'y':
                    return True
                elif judge == 'n':
                    return False
                else:
                    judge = raw_input('输入错误，请重新输入(y/n)：\n'.decode('utf-8').encode('gbk'))
    else:
        return False

                