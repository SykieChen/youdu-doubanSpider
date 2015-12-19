#!/usr/bin/python34
# coding=utf-8
import io
import sys
import json
#import urllib.parse
#import urllib.request
import pymysql
import time
import password

#连接数据库
config = {
	'host':'localhost',
	'port':3306,
	'user':password.dbPUsr,
	'password':password.dbPPass,
	'db':'youdu',
	'charset':'utf8',
	'cursorclass':pymysql.cursors.DictCursor,
}
connection = pymysql.connect(**config)
c = connection.cursor()
sql='SELECT rating_numRaters FROM c17_douban_data WHERE id=1;'
c.execute(sql)
idR=c.fetchall()
print(idR[0]["rating_numRaters"])

# try to get new records
sql='SELECT douban_book_id FROM books WHERE id>%s'
v=(idR[0]["rating_numRaters"])
c.execute(sql,v)
idR=c.fetchall()
print(len(idR))



#sql = 'SELECT douban_book_id FROM books WHERE id>'

c.close()
connection.close()
