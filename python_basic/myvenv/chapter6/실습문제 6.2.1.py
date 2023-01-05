#docstring: 설명문
#함수 시작부분에 따옴표 주석으로 함수설명을 달아놓을 수 있다.
#이제 함수에 커서 올려놓으면 설명이 나온다.

def printSumAvg(x,y,z):
    """
    섬과 에버리지를 프린트 하는 함수
    매개변수 x : 숫자
    매개변수 y : 숫자
    """
    sum = x+y+z
    avg = sum/3
    print(f"합계: {sum} 평균: {avg}")


multiply