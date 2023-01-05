# #1. 파일 쓰기
# #기준이 루트디렉토리 바로 아래에 잡히기 때문에
# #python_basic 폴더아래에 바로 생기게된다.
# #file = open("data.txt", "w")
# file = open("./myvenv/chapter10/data.txt", "w", encoding="utf8")
# #맥은 비스코안꺠지는데. 윈도우는꺠지는듯. 인코딩 사용.
# file.write("1. 스타트코딩")
# file.close()
#2. 파일 추가
# file = open("./myvenv/chapter10/data.txt", "a", encoding="utf8")
# file.write("2. 비전공자")
# file.close()
# 3. 파일 전체읽기
file = open("./myvenv/chapter10/data.txt", "r", encoding="utf8")
# data = file.read()
# file.close()

# 3.2 파일 한줄 읽기. 마지막을 찾아 브레이크 해주는 로직
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()
