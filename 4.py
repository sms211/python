import random

print("영어 단어 알파벳 찾기 게임")
print("=====made by villager=====")

words = ["creeper", "roblox", "herobrine", "microsoft", "google", "auditorium", "suspicious", "axolotl", "java", "mojang"]
word = random.choice(words)

guesses = []

for _ in range(10):
    for char in word:
        if char in guesses:
          print(char, end=" ")
        else:
            print("_", end=" ")
    print()


    guess = input("알파벳을 입력하세요 :")
    guesses.append(guess)


    found_all = True
    for char in word:
        if char not in guesses:
            found_all = False
    if found_all:
        print("성공!")
        break
