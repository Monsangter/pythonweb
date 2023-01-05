import csv

data = [
    ["종목","매입가","수량","목표가"],
    ["삼성전자","85000","10","90000"],
    ["NAVER","380000","5","400000"],
]

file = open("./myvenv/chapter10/mystock.csv","w")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()

file = open("./myvenv/chapter10/mystock.csv","r")
reader = list(csv.reader(file))#순회가능한 시퀀스자료형의 객체가 나온다.

for data in reader[1:]:
    print(data[0], (int(data[3])-int(data[1]))*int(data[2]), (int(data[3])/int(data[1])-1)*100)


