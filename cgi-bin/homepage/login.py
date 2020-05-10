#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3

print("Content-type: text/html")
form = cgi.FieldStorage()
id = form.getvalue('id')
pwd = form.getvalue('pw')

con = sqlite3.connect('admin.db')
con.row_factory = sqlite3.Row
cursor = con.cursor()
cursor.execute('''select * from mem where id = ?''',(id,))
row = cursor.fetchone()
if row != None:
    if id == row[0] and pwd == row[1]:
        print("Location: http://localhost/admin.html\n\n")
    else:
        print("\n\n")
        print("<h2>아이디와 비밀번호가 일치하지 않습니다!<h2>")
else:
    print("\n\n")
    print("<h2>아이디가 존재하지 않습니다!<h2>")

con.close()