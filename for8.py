num1 = 0
num2 = list(map(int, input("5명의 성적을 입력하세요").split()))

for x in range(5):
      num1 += num2[x]

avg = num1/5


print("총점 : %d"%num1)
print("평균 : %.1f"%avg)
