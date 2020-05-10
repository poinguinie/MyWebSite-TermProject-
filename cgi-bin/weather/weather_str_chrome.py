#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3

large_name = []
small_name = []
large_code = []
small_code =[]

con = sqlite3.connect("weather_local.db")
con.row_factory = sqlite3.Row
cursor = con.cursor()

cursor.execute('''
select * from all_local''')
rows = cursor.fetchall()

for row in rows:
    if row[1] not in large_name:
        large_name.append(row[1])

print("Content-type: text/html\n\n")
print('''
<html>
    <head>
    <title> CSDGD'S 전국 날씨 알리미 </title>
    </head>
    <body>
    <h2> 전국 날씨 알리미에 오신 것을 환영합니다! </h2>
    <p> 아래 빈칸을 입력해주세요! </p>
    <form method="post" action = "/cgi-bin/weather/weather.py">
        <input name = "large" list = "large" type = "text" placeholder = "--선택--">
        <datalist id = "large">''')
for info in large_name:
    print('''
		    <option value = "%s" label = "%s"></option>'''%(info,info))
print('''
        </datalist> <br><br>
        <input name = "small" list = "small" type = "text" placeholder = "--선택--">
        <datalist id = "small">''')
for info_2 in rows:
    print('''
            <option value = "%s" label = "%s"></option>'''%(info_2[2],info_2[1]))
print('''
        </datalist><br><br>
    <input type="submit" value="입력!"> <br>
    </form>
    <h5> 출처 : <a href = "weather.naver.com" > 네이버 날씨 </a> </h5>
    <b> <a href = "/CSEGDhomepage.html">로비로 돌아가기</a> </b>
    </body>
</html>''')