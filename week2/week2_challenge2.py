data = ["조회수: 1,500",
        "조회수: 1,002",
        "조회수: 300",
        "조회수: 251",
        "조회수: 13,432",
        "조회수: 998"]
sum = 0

for i in range(len(data)):
    aaa = data[i][5:].replace(",","")
    print(aaa)
    aaa = int(aaa)
    sum = sum + aaa

print("sum : ",sum)