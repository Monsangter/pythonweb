#딕셔너리
#:사전형태의 자료형

stock_a = {"삼성전자":82000, "LG전자":150000}

#이런식 표기가 들여쓰기 자동으로 되면서 가시성 편함
#딕셔너리만들기
stock_b = {
    "삼성전자" : [10000,81500,82000,81500,82000],
    "LG전자" : (15000, 14900, 14800, 15100, 15200)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000,
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

#딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기

stock_a["삼성전자"] = 85000
print(stock_a)

#딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

#딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "하이닉스" : 82000,
    "네이버" : 82000,
    "카카오" : 82000,
}

#items(): 키와 데이터 쌍
print(stock_d.items())
#얘만의 자료형이 있기때문에 좀 특이하게 나옴.

for item in stock_d.items():
    print(item)

#시퀀스 자료형이기 떄문에 보통 이렇게 사용할 수 있다.

#keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터

for value in stock_d.values():
    print(value)







