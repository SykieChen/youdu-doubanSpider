#!/usr/bin/python34
# coding=utf-8
import io
import sys
import json
#import urllib.parse
#import urllib.request
import pymysql
import time

#连接数据库
config = {
	'host':'localhost',
	'port':3306,
	'user':password.dbUsr,
	'password':password.dbPass,
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
print("Hi")


#sql = 'SELECT douban_book_id FROM books WHERE id>'

c.close()
connection.close()
