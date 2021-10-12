print("-" *25)
print("영어 단어 맞추기 게임")
print("-" *25)

dic ={"auditorium":"강당", "exhibition":"전시회", "diamond":"다이아몬드",
        "aircraft":"항공기", "expensive":"비싸다", "diamond sword":"다이아몬드 검"}


for word in dic.keys() :
    korean = dic[word]
    guess = input("{}단어를 번역하세요".format(word))

    if guess == korean :
        print("정답")
    else :
        print("오답")

print("프로그램 종료")
