study_time = int(input("공부시간을 입력하세요(시간)"))

if study_time >= 10:
    print("휴대폰 잠금해제")
elif study_time >= 5:
    print("30분사용가능")
else:
    print("휴대폰 사용불능")