#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
# @Author: Jeay 
# @Date: 2018-05-20 10:29:02 
# @Last Modified by:   Jeay 
# @Last Modified time: 2018-05-20 10:29:02 
'''
""" 
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('CREATE TABLE lm_server (id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR (120), ip CHAR (50));')
print("Table created successfully")
conn.commit()

conn.close()


"""

import sqlite

# sqllite数据库测试
db = sqlite.mysqlite({
    'db': 'test.db',
    'prefix': 'lm_'
})
datalist = db.table('server').getarr()
print(datalist)
# 创建表
""" db.query('CREATE TABLE article(id INTEGER primary key, title text)')
result = db.table('article').add({'title': '测试标题'})
datalist = db.table('article').getarr()
num = db.table('article').where('id=3').delete()
res = db.table('article').where('id=1').save({'title': '更新数据'})
resul = db.table('article').setinc('views')
print(datalist) """
db.close()