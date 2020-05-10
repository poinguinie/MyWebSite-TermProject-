#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3
import time

print("Content-type: text/html")

con = sqlite3.connect("visitlog.db")
cursor = con.cursor()
cursor.execute("delete from preview")

con.commit()
con.close()

print("Location: http://localhost/admin.html\n\n")