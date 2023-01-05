#1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치", "메뚜기"]

# - 데이터 없는 리스트
empty = []

# 2. ㅣㄹ스트 조작

# - 데이터 접근하기
# 인덱스는 0부터시작
print(animals[1])
print(animals[-1])# 가장 마지막 데이터 반환

# - 데이터 추가하기 
animals.append("고라니")
print(animals)

# - 데이터 할당
animals[1] = "청개구리"
print(animals)

# - 데이터 삭제하기
del animals[0]
print(animals)

# -리스트 슬라이싱
animals[0:2]
animals[:]# 전체
print(animals[:3])#인덱스 생략시 가장 첫번째 값이 자동으로
#끝인덱스 생략시 가장 마지막 값이 자동으로

# - 리스트 길이
print(len(animals))

# - 정렬
animals.sort()
animals.sort(reverse=True)
#원본을 바꿈.