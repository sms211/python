import random
print("="*30)
print("made by 나는 주민이다")
print("님게임")
print("="*20)

number = 0
turn = 0

while True:
    if turn == 0:
        p1 = int(input("숫자를 입력하세요(1~3) : "))
        if p1 > 3:
            print("차단되었습니다")
            break
        for i in range(p1):
            number += 1
            print("you:", number)

        turn += 1
        turn %= 2

    elif turn ==1:    #컴퓨터순서
        p2 = random.randint(1, 3)
        for i in range(p2):
            number += 1
            print("컴퓨터:", number)

        turn += 1
        turn %= 2

    if number >= 31:
        break


if turn == 0:
    print("승")
else :
    print("패")  

    
