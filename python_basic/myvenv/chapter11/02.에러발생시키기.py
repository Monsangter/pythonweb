# raise 구문을 사용해 에러를 강제로 발생시켜 보자.

try:
    num = int(input("음수를 입력해주세요>>>"))
    if num>= 0:
        raise Exception("양수는 입력 불가")
except Exception as e: #위에서 raise로 만든 exception을 가져올 수 있다.
    print("에러 발생!", e)
