# 조건문
# : 조건에 따라 실행할 명령이 달라지는 것

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass: 
    #조건이 참이라면
    print("로그인 성공!")
elif input_pass == "":
    #조건 a 거짓, 조건 b참
    print("아무것도 입력하지 않았습니다.")
else:
    # 조건 A 거짓
    print("로그인 실패!")