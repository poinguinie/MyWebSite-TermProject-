#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3
import datetime

con = sqlite3.connect("visitlog.db")
cursor = con.cursor()

print("Content-type: text/html")

form = cgi.FieldStorage()
name = form.getvalue('name')
cont = form.getvalue('content')
time = datetime.datetime.now()
time_1 = str(time)
time_2 = time_1[0:16]  #연/월/일/시/분 까지만 출력을 위해

conn = sqlite3.connect('visitlog.db')
cursor = conn.cursor()
cursor.execute('''
insert into preview (name, content, time) values(?,?,?)''',(name,cont,time_2))

conn.commit()
conn.close()

print("Location: http://localhost/cgi-bin/visitlog/visitlog_1.py\n\n")