#!usr/bin/env python
# coding:utf-8

import sqlite3



def catchClass(obj):
    catch = {}
    def _catch(*args,**kwargs):
        if obj not in catch:
            catch[obj] = obj(*args,**kwargs)
        return catch[obj]
    return _catch
#如果使用这个装饰器,只能操作一个database
@catchClass
class SqllitUtils(object):

    def __init__(self,dbName):
        self.conn = sqlite3.connect(dbName)
        self.cur = self.conn.cursor()


    def create(self,tableName,charset=["ID INT PRIMARY KEY  NOT NULL"]):
        try:
            if not isinstance(charset,(list,tuple)):
                raise TypeError,"字段类型错误"
            sql = "CREATE TABLE {table_name} ({char};)".format(table_name=tableName,char=",".join(charset))
            self.cur.execute(sql)
            self.commit()
        except Exception:
            print Exception

    def insert(self,tableName,cha=[],value=[]):
        try:
            if not isinstance(cha,(list,tuple)) and not isinstance(value,(list,tuple)):
                raise TypeError, "字段和值类型错误"
            sql = "INSERT INTO {tablel_name} ({chr}) VALUES ({value})".format(tablel_name=tableName,
                                                                              chr=",".join(chr),
                                                                              value=','.join(value))
            self.cur.execute(sql)
            self.commit()
        except Exception:
            print Exception

    def update(self,tableName,value,flag):
        try:

            sql = "UPDATE {table_name} SET {value} WHERE {flag}".format(table_name=tableName,value=value, flag=flag)
            self.cur.execute(sql)
            self.commit()
        except Exception:
            print Exception

    def delete(self,tableName,flag):
        try:

            sql = "DELETE {table_name}  WHERE {flag}".format(table_name=tableName,flag=flag)
            self.cur.execute(sql)
            self.commit()
        except Exception:
            print Exception
