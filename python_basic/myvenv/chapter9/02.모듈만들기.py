import pay_module
#방금만든 pay모듈을 쓰고 싶은데, 임포트 해올 수 없다. 루트폴더 바로 아래 있는 애들만 가능.
# 설정 바꿔줘야함 preference settings 에서 창모양 클릭 json 파일 열어
#"python.analysis.extraPaths": ["./myvenv/Chapter9"], 넣어줌

#변수 사용
print(pay_module.version)

#함수 사용
pay_module.printAuthor()

#클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2021-06-13")
pay_info.get_pay_info()

pay_module.__name__