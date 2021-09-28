coffee = 5
money = 300
while money :
    print("커피를 드릴게요")
    coffee -= 1
    print("남은 커피의 잔수는 %d 입니다"%coffee)

    if coffee == 0 :
        print("sold out sorry")
        break
