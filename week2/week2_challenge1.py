print("BMI 계산기입니다")

height = input("신장 : ")
weight = input("몸무게 : ")
height = int(height)
weight = int(weight)

bmi = weight / (height ** 2) *10000
print("BMI : ", bmi)