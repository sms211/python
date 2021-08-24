num1 = int(input("정수 1을 입력하세요"))
num2 = int(input("정수 2를 입력하세요"))
num3 = int(input("정수 3을 입력하세요"))

min_data = num1 if num1 < num2 else num2
min_data = min_data if min_data < num3 else num3

print(min_data)
