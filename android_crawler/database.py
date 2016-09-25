#coding:utf-8
import sqlite3



class db():
    def __init__(self):
        self.db_name = u"apk_information.db"
        conn = None
        conn = sqlite3.connect(self.db_name)
        self.conn =conn
        
        
    def create_db(self):
        self.conn.execute('''
            create table if not exists apk
                (apk_name nvarchar(40),
                apk_site nvarchar(500),
                apk_sort nchar(50),
                apk_introduce nvarchar(1000),
                apk_down_times char(20),
                apk_like char(20),
                apk_md5 char(32) primary key);
        '''
        )
    def data_memory(self,apk_name,apk_site,apk_sort,apk_introduce,apk_down_times,apk_score,apk_md5):
        self.conn.execute('''
            insert into apk
            values
            ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')'''.format(apk_name,apk_site,apk_sort,apk_introduce,apk_down_times,apk_score,apk_md5)
        )
        self.conn.commit()
        
    def data_select(self,sql):
        cursor = self.conn.execute('''
            {}
        '''.format(sql))
        return cursor
    def data_jud(self,md5):
        cursor = self.data_select('select count(*) from apk where apk_md5=\'{}\''.format(md5))
        rows = cursor.fetchone()
        return rows[0]
        
        
    def __del__(self):
        if self.conn:
            self.conn.close()