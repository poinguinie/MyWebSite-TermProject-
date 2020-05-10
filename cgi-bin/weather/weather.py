#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#



import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import cgi
import cgitb; cgitb.enable()
import sqlite3

def find_place(code2find):
    con = sqlite3.connect("weather_local.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    cursor.execute("select * from all_local where large_name = ?",(code2find,))
    row = cursor.fetchone()
    if row != None:
        if code2find == row[1]:
            return(row[3])
        else:
            print("정보가 존재하지 않습니다!")
    else:
        print("정보가 존재하지 않습니다!")

def find_detail_place(code2find):
    con = sqlite3.connect("weather_local.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    cursor.execute("select * from all_local where small_name = ?", (code2find,))
    row = cursor.fetchone()
    if row != None:
        if code2find == row[2]:
            return (row[4])
        else:
            print("정보가 존재하지 않습니다!")
    else:
        print("정보가 존재하지 않습니다!")

def select_city(code2find):
    place_f = open("nomise.txt")
    for line in place_f:
        if code2find + "\n" == line:
            place_f.close()
            return 'no'
    place_f.close()
    return 'yes'

def get_weather(A,B,C):
    Page = ("http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT0%02d%03d"%(int(A),int(B)))
    weather_page = urllib.request.urlopen(Page)
    with urllib.request.urlopen(Page) as response:
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')
    weather = weather_page.read().decode("utf8")
    span_1 = soup.find('div', {'class' : 'fl'})
    span_2 = span_1.find('span').text
    print(span_2,"시 기준<br><br>")
    tem = soup.select('em')[2].text
    tem_1 = tem.split()
    NOW_A = tem_1[0]
    print("현재 날씨 :",NOW_A,"도<br>")
    cond = soup.select('em > strong')[0].text
    print("현재 상태 :" + cond +  "<br>")
    if C == 'yes':
        Mise = soup.select('dl > dt > span')[0].text
        print("현재 미세먼지 :" + Mise + "<br>")
        Mise_int = int(Mise.replace('㎍/㎥',' '))
        if Mise_int <= 30:
            print("미세먼지 수준 : 좋음<br><br>")
        elif Mise_int <= 80:
            print("미세먼지 수준 : 보통<br<br>")
        elif Mise_int <= 150:
            print("미세먼지 수준 : 나쁨<br><br>")
        else:
            print("미세먼지 수준 : 매우 나쁨<br><br>")
    else:
        print("해당도시는 미세먼지 측정을 지원하지 않습니다.<br><br>")


print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
Large = form.getvalue("large")
Small = form.getvalue("small")
lookup_place = "수도권"
lookup_detail_place = "서울"

print('''<html>
<head>
<title>전국 날씨 알리미 결과</title>
</head>''')
print("선택도시 : %s %s시/군<br><hr>"%(lookup_place,lookup_detail_place))
place_code = find_place(lookup_place)
large_code = int(place_code)
if place_code:
    place_detail_code = find_detail_place(lookup_detail_place)
    small_code = int(place_detail_code)
    if place_detail_code:
        C = select_city(lookup_detail_place)
        get_weather(large_code, small_code, C)
    else:
        print("제대로 입력하셨는지 확인하십시오.<br><br>")
else:
    print("제대로 입력하셨는지 확인하십시오.<br><br>")

print('''<hr><br> <a href = "/CSEGDhomepage.html">로비</a>로 돌아가기
</html>''')

