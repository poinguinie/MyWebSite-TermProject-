#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3

print("Content-type: text/html\n\n")

print('''<head><title>번호입력</title></head>''')

con = sqlite3.connect("visitlog.db")
cursor = con.cursor()
con.row_factory = sqlite3.Row
cursor.execute("select * from preview")
rows = cursor.fetchall()
for row in rows:
    print("번호 : %s / 내용 : %s <br><hr>"%(row[0],row[2]))
con.close()

print('''<form method = "post" action = "visitlog_del_1.py">
<input name = "del_num" type = "text" placeholder = "번호입력">
<input type = "submit" value = "전송">
</form>''')