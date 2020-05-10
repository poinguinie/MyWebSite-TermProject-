#!/Users/user/AppData/Local/Programs/Python/Python36-32/python
#

import cgi
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

lookup_place = form.getvalue("large_place")   #수도권,충남 등의 정보
lookup_detail_place = form.getvalue("small_place")    #세부지역 정보

def find_place(code2find):   #수도권,충남 등의 정보를 수치로 변환하는 함수
    place_f = open("place_code.txt")
    for line in place_f:
        (place_name,place_code) = line.split()
        if code2find == place_name:
            place_f.close
            return (place_code)
    place_f.close()
    return({})

def find_detail_place(code2find):    #세부 지역 정보를 수치로 변환하는 함수
    place_f = open("place_detail_code.txt")
    for line in place_f:
        (place_name,place_huge_code,place_code) = line.split()
        if code2find == place_name:
            place_f.close
            return (place_code)
    place_f.close()
    return({})

def select_city(code2find):   #미세먼지 정도를 지원하지 않는 지역 선별
    place_f = open("nomise.txt")
    for line in place_f:
        if code2find + "\n" == line:
            place_f.close()
            return 'no'
    place_f.close()
    return 'yes'

def get_weather(A,B,C):    #url로 부터 날씨 불러오고 출력하는 함수
    AD = ("http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT0")
    Page = AD + str(A) + str(B)
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
    print("현재 날씨 :",NOW_A,"도<br><br>")
    cond = soup.select('em > strong')[0].text
    print("현재 상태 :" + cond +  "<br><br>")
    if C == 'yes':
        Mise = soup.select('dl > dt > span')[0].text
        print("현재 미세먼지 :" + Mise + "<br><br>")
        Mise_int = int(Mise.replace('㎍/㎥',' '))
        if Mise_int <= 30:
            print("미세먼지 수준 : 좋음")
        elif Mise_int <= 80:
            print("미세먼지 수준 : 보통")
        elif Mise_int <= 150:
            print("미세먼지 수준 : 나쁨")
        else:
            print("미세먼지 수준 : 매우 나쁨")
    else:
        print("해당도시는 미세먼지 측정을 지원하지 않습니다.")


      #실행 하는 곳

print("""
<html>
	<head>
		<title>전국 날씨 알리미</title>
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Arimo:400,700' rel='stylesheet' type='text/css'>
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel-noscript.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-desktop.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="css/ie/v9.css" /><![endif]-->
	</head>
	<body>

		<div id="header">
			<div class="container"> 
				<div id="logo">
					<h1><a href="#">전국 날씨 알리미</a></h1>
					<span>알고 싶은 지역의 날씨를 검색해보아요!</span>
				</div>
				
				<nav id="nav">
					<ul>
						<li><a href="NGDH.html">로비</a></li>
						<li class="active"><a href="weather_GD.html">전국 날씨 알리미</a></li>
						<li><a href="right-sidebar.html">방명록</a></li>
						<li><a href="no-sidebar.html">문의하기</a></li>
					</ul>
				</nav>
			</div>
		</div>

		<!-- Main -->
		<div id="main">
			<div class="container">
				<div class="row"> 

					<!-- Sidebar -->
					<div id="sidebar" class="4u">
						<section>
							<header>
								<a href = "http://weather.naver.com/"><h2>출처 : 네이버 날씨(클릭시 이동)</h2></a>
							</header>
						</section>
					</div>
					
					<!-- Content -->
					<div id="content" class="8u skel-cell-important">
						<section>
							<header>
								<h2>전국 날씨 알리미 (결과)</h2>
							</header>
							<p>선택도시 : """ + str(lookup_place) + " " + str(lookup_detail_place) + "시/군 <p>" + "<br><br>")
                        place_code = find_place(str(lookup_place))
                        if place_code:
                            place_detail_code = find_detail_place(str(lookup_detail_place))
                            if place_detail_code:
                                C = select_city(str(lookup_detail_place))
                                get_weather(place_code, place_detail_code, C)
                            else:
                                print("<p>제대로 입력하셨는지 확인하십시오.<p><br><br>")
                        else:
                            print("<p>제대로 입력하셨는지 확인하십시오.<p><br><br>")
                            print("""<a href="#" class="image full"><img src="star.jpg" alt="" /></a>
						</section>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
""")

    




