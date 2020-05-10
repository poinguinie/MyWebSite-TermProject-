#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3



con = sqlite3.connect("visitlog.db")   #방명록 DB 불러오기
con.row_factory = sqlite3.Row
cursor = con.cursor()

cursor.execute('''
select * from preview order by integar''')   #integar을 기준으로 정렬
rows = cursor.fetchall()

print("Content-type: text/html; \n\n")
print('''
<HTML>
<HEAD><TITLE>방명록</TITLE></HEAD>
<BODY>
    <h2>방명록</h2>
    <span>이 홈페이지에 들러서 그냥 가게? 한번 쓰고 가요!</span><br><br>
    <div class = "container">
        <table class = "table table-striped">
		    <thead>
		    <tr>
			     <th>작성자</th>
			     <th>내용</th>
			     <th>날짜</th>
		    </tr>
		    </thead>
		    <hr>
		<tbody>''')
for row in rows:    # 데이터베이스에 저장된 값을 출력
    print('''
    		<tr>
    		    <td>%s</td>
			    <td>%s</td>
			    <td>%s</td>
		    <tr>'''%(row[1],row[2],row[3]))
print('''
		</tbody>
	</table>
	<hr>
	<a class= "btn btn-default pull-right" href = "/visitlog_write.html">글쓰기</a>
  </div>
  <br> <b> <a href = "/CSEGDhomepage.html">로비로 돌아가기</a> </b>
</BODY>
</HTML>''')

con.close()