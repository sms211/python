cnt1 = 0
cnt2 = 0
num = list(map(int, input().split()))

for x in num :
    if x%2 == 0 :
        cnt1 += 1
    else :
        cnt2 += 1

print("짝수 : %d개"%cnt1)
print("홀수 : %d개"%cnt2)
