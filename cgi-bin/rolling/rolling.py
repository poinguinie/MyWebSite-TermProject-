#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import cgitb; cgitb.enable()

print('''
<html>
<head>
<title> 이상정 교수님께 드리는 롤링페이퍼 </title>
</head>
<body>
<h3>1학년을 대표하여</h3>
한 학기동안 많은 것을 배웠습니다!<br>
감사의 마음으로 이 롤링페이퍼를 남깁니다!<br>
각 링크를 따라가시면 1학년들의 롤링페이퍼를 보실 수 있습니다!<br>
정말 고마웠습니다!<br>

<ul>''')

for num in range(1,20):
	print('''
<li> <a href = "/rolling/%d.html"> %d </li>'''%(num,num))
print('''
</ul>
</body>
</html>''')