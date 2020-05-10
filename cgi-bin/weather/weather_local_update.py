#20184070 컴퓨터공학과 이지호
#임의의 프로그램

import sqlite3

con = sqlite3.connect('weather_local.db')
con.row_factory = sqlite3.Row
cursor = con.cursor()

weather_large = open("place_code.txt")

location_list = {}
locations = []

for line_1 in weather_large:
    (name_1, code_1) = line_1.split()
    weather_small = open("place_detail_code.txt")
    for line_2 in weather_small:
        (name_2,code_large,code_small) = line_2.split()
        if code_1 == code_large:
            cursor.execute('''
            insert into all_local (large_name, small_name, large_code, small_code) values(?,?,?,?)   
            ''',(name_1,name_2,code_large,code_small))   #원래 메모장에 있던 지역 정보들을 데이터베이스에 옮기는 과정을 파이썬으로
                                                           #하였습니다.
            if name_1 == "수도권":                       #여기서 부터는 각 해당하는 넓은 지역에 세부 지역을 옮기는 과정
                cursor.execute('''
                insert into sudo (name) values(?)''',(name_2,))
            elif name_1 == "서해안":
                cursor.execute('''
                insert into suhae (name) values(?)''', (name_2,))
            elif name_1 == "영서":
                cursor.execute('''
                insert into youngseo (name) values(?)''', (name_2,))
            elif name_1 == "영동":
                cursor.execute('''
                insert into youngdong (name) values(?)''', (name_2,))
            elif name_1 == "충북":
                cursor.execute('''
                insert into chungbuk (name) values(?)''', (name_2,))
            elif name_1 == "충남":
                cursor.execute('''
                insert into chungnam (name) values(?)''', (name_2,))
            elif name_1 == "경북":
                cursor.execute('''
                insert into gyungbuk (name) values(?)''', (name_2,))
            elif name_1 == "경남":
                cursor.execute('''
                insert into gyoungnam (name) values(?)''', (name_2,))
            elif name_1 == "울릉":
                cursor.execute('''
                insert into ull (name) values(?)''', (name_2,))
            elif name_1 == "전북":
                cursor.execute('''
                insert into junbuk (name) values(?)''', (name_2,))
            elif name_1 == "전남":
                cursor.execute('''
                insert into junnam (name) values(?)''', (name_2,))
            elif name_1 == "제주":
                cursor.execute('''
                insert into jaeju (name) values(?)''', (name_2,))

con.commit()
con.close()

weather_large.close()
weather_small.close()
