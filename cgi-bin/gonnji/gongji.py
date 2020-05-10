#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()
import sqlite3

con = sqlite3.connect("gongji.db")
con.row_factory = sqlite3.Row
cursor = con.cursor()

cursor.execute('''
select * from content order by num''')
rows = cursor.fetchall()

print("Content-type: text/html; \n\n")
print('''
<HTML>
<HEAD><TITLE>공지글</TITLE></HEAD>
<BODY>
    <h2>공지글 모아보기</h2>
    <span>공지 좀 읽고 물어봐줘요!</span><br><br>
		<thead>
		    <tr>
		        <th>번호</th>
			     <th>작성자</th>
			     <th>제목</th>
			     <th>조회수</th>
			     <th>날짜</th>
			     <th>자세히 보기</th>
		    </tr>
		    </thead>
		    <hr>
		<tbody>''')
for row in rows:
    print('''
    		<tr>
    		    <td>%s</td>
			    <td>%s</td>
			    <td>%s</td>
			    <td>%s</td>
			    <td>%s</td>
			    <td>%s</td>
		    <tr>'''%(row[0],row[1],row[2],row[4],row[5],"a href = "))
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