import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 32],
]

file = open("./myvenv/chapter10/studnet.csv", "w")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()