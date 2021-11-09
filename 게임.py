import random


words = ["herobrine", "arrow", "amogus", "meme", "diamond"]
random.shuffle(words)

count = 0
for word in words:
    characters = list(word)
    random.shuffle(characters)
    shuffled_word = "".join(characters)


    guess = input("{}의 원래 단어를 맞추세요 :".format(shuffled_word))

    if guess == word:
        print("정답")
        count += 1
    else:
        print("오답")

score = count / len(words) * 100
print("100점 만점 {:.2f} 점입니다.".format(score))
