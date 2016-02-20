#coding=utf-8
import MySQLdb

host_ip = ''
usr_name = ""
password = ''
db = ''

def insert(sql, parms):
    try:
        conn=MySQLdb.connect(host=host_ip,user=usr_name,passwd=password,db=db,charset="utf8")
        cursor = conn.cursor()
        for parm in parms:
            n = cursor.execute(sql, parm)
        conn.commit()
        cursor.close()
    except Exception, msg:
        print(msg)
        return
    finally:
        conn.close()