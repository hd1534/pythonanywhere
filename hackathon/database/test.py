# from . import DB as db
import os

# from datetime import datetime
# from sqlalchemy.sql import expression
# from enum import Enum
'''
conn = sqlite3.connect("test.db")

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL 쿼리 실행
cur.execute("select * from customer")

# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)

# Connection 닫기
conn.close()
'''


def write(data):
    f = open('test.txt', 'w')
    f.write(data)
    print(data)
    f.close()


def read():
    f = open('test.txt', 'r')
    data = f.read()
    print(data)
    return data
