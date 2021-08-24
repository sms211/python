num1 = int(input("숫자 1을 입력하세요"))
num2 = int(input("숫자 2를 입력하세요"))

if num1 > num2 :
    result = num1 - num2
    print(result)
else :
    result = num2 - num1
    print(result)

#삼항연산자 사용
#result = num1-num2 if num1 > num2 else num2-num1

print("차이 : %d" %result)
