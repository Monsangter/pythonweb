#원화를 입력, 환율 입력 -> 달러 값

won = input("원화 금액을 입력하세요>>>")
dollar = input("환율을 입력하세요>>>")

try:#예외가 발생할 수 있는 코드
    print(int(won)/int(dollar))
except ValueError as e:#예외 발생시 실행되는 코드, 앨리아스를 지정해 출력해줄 수도 있다.
    #구체적으로 에러를 지정해줄 수도 있다. 밸류에러는 인트인데 문자열을 입력했을떄 발생하는 오류
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.", e)
else:
    print("예외가 발생하지 않았을떄 실행되는 코드")
finally: # 파일 닫기
    print("예외 발생하든 아니든 항상 실행되는 코드")

print("프로그램이 끝났나요?")