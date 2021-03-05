birth = input("생년월일을 6자리로 입력해주시요.(yymmdd): ")

year = birth[0:2]
month = birth[2:4]
day = birth[4:6]

year = str(year)
month = str(month)
day = str(day)

print("당신의 생일은 : " + year + "년" + month + "월" + day + "일입니다.")