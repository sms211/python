def sum_func(n):
    hap = 0
    for i in range(1, n+1):
        hap += i
    return hap

num = int(input("수를 입력"))
sum_hap = sum_func(num)
print("결과", sum_hap)


def factorial(n):
    hap = 1
    for i in range(1, n+1):
        hap *= i
    return hap

num = int(input("값 입력"))
print("1부터 n까지의 합은", factorial(num))
