import random
import time

w = ["anti-aircraft guns", "python", "snake", "exhibition", "mine", "diamond", "a", "creeper", "arrow", "lucky"]
n = 1
print("타자 게임을 시작합니다.준비되면 엔터")
input()
start = time.time()
q = random.choice(w)

while n <= 5 :
    print("*문제", n)
    print(q)
    x = input()

    if q == x :
      print("통과")
      n += 1
      q = random.choice(w)
    else :
          print("오타")

end = time.time()
et = end - start
et = format(et, ".2f")
print("걸린 시간:", et, "초")
