#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql

class Db(object):

    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'root'
    database = 'spider'
    charset = 'utf8'

    def __init__(self,config=[]):
        if config:
            for conf in config:
                self.conf = config[conf]
        self.connect = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.database,
            charset=self.charset
        )
        # print(self.db.cursor())
        self.cursor = self.connect.cursor()

    def insert(self, table, param: object):
        cloumn = []
        value = []
        for var in param:
            cloumn.append(var)
            value.append(str(param[var]))
        sql = "INSERT INTO %s (%s) VALUES ('%s')" % ( table ,','.join(cloumn),"','".join(value) )

        execRes = self.exec(sql)
        if execRes:
            return self.cursor.rowcount
        else:
            return execRes


    def select(self,param: object={}):
        sql = "SELECT * FROM lottery_info";
        execRes = self.exec(sql)
        if execRes:
            return self.cursor.fetchall()
        else:
            return False

    def exec(self,sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            return True
        except:
            self.connect.rollback()
            return False

    def __del__(self):
        self.cursor.close()
        self.connect.close()

if __name__=='__main__':
    db = Db()
    param = [{'stage': 1, 'one': 2, 'two': 3, 'three': 4, 'four': 5, 'five': 6, 'six': 7, 'seven': 8, 'time': 9,
             'create_time': 10}]
    db.insert(param)
# db = Db()
# param = {'stage':1,'one':2,'two':3,'three':4,'four':5,'five':6,'six':7,'seven':8,'time':9,'create_time':10}
# print(db.insert(param))
# print(db.select())