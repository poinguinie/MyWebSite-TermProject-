#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import smtplib   #smpt 보안을 인증하기 위한 모듈
from email.message import EmailMessage   #메일 메시지 모듈
import cgi

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

name = form.getvalue("name")
htmlMessage = form.getvalue("main")

message = EmailMessage()
message['Subject'] = '과대에게 온 문의사항'
message['From'] = 'wlgh0206@naver.com'
message['To'] = 'wlgh0206@naver.com'
message.set_content("보낸 이 : " + str(name) + "\n\n" + "내용 : " + str(htmlMessage))

with smtplib.SMTP_SSL('smtp.naver.com',465) as server :   #SMTP 보안을 인증하기 위함
    server.ehlo()
    server.login('wlgh0206','voicejh3922')
    server.send_message(message)

print("과대에게 문의사항이 전달되었습니다!")