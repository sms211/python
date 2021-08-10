#몸무게를 입력받아 체급을 출력하는 프로그램
print("복싱 체급 안내 프로그램입니다")
weight = float(input("몸무게를 입력하세요"))
if weight <= 50.8 :
    print("Flyweight")
elif weight <= 61.23 :
    print("Lightweight")
elif weight <= 72.57 :
    print("Middleweight")
elif weight <=  88.45 :
    print("Cruiserweight")
else :
    print("HeaveyWight")
