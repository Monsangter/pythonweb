kor_sco = int(input("국어 >>>"))
eng_sco = int(input("영어 >>>"))
math_sco = int(input("수학 >>>"))

avg = kor_sco+eng_sco+math_sco/3

if 0 <= korean <= 100 and 0 <= math <= 100 and 0<= english <= 100:
    if avg >= 60:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")

#방법 2
#if kor <0 or kor > 100 eng < 0 or eng> 100 ...
# 이런식으로 or연산으로 처리할 수도 있다.