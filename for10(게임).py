import random

secretNumber = random.randint(1, 11111)
print("1부터 11111까지의 숫자가 있어요")

for x in range(20) :
    print("하나 때려맞히세요")

    guess = int(input("숫자:"))

    if guess > secretNumber :
        print("더 작다")
    elif guess < secretNumber :
        print("더 크다")
    else :
        break

if guess == secretNumber :
     print("정답입니다")
else :
    print("틀렸습니다")
