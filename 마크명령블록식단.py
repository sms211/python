import random

menus = ["스테이크", "케이크", "꿀", "빵", "사탕무 스튜", "수상한 스튜", "황금 사과", "우유", "익힌 돼지고기", "익힌 닭고기", "익힌 대구", "익힌 연어", "구운 감자", "수박 조각"]
prices = [9000, 10000, 1000, 5000, 6000, 8000, 100000, 1000, 7000, 6000, 20000, 30000, 2000, 3000]

print("메뉴")
for menu, price in zip(menus,prices) :
    print(menu,price)
print()

days = ["아침", "점심", "저녁"]

for day in days :
    i = random.randint(0, len(menus)-1)
    print(day, "의 추천 메뉴")
    print("추천 메뉴 : ", menus[i])
    print("메뉴 가격 : ", prices[i])
    print()

