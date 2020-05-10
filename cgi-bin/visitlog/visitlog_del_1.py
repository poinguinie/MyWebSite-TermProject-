#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3

print("Content-type: text/html")

con = sqlite3.connect("visitlog.db")
cursor = con.cursor()

form = cgi.FieldStorage()
num = form.getvalue('del_num')

if num:
    cursor.execute("delete from preview where integar = ?",(int(num),))
    con.commit()
    con.close()
    print("Location: http://localhost/admin.html\n\n")
else:
    print("에러!!")