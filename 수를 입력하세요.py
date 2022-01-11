def sum_func(n):
    hap = 0
    for i in range(1, n+1):
        hap += i
    return hap

num = int(input("수 입력"))
sum_hap = sum_func(num)
print(sum_hap)
