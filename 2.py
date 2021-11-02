def pigeon(a,b):
    num1 = max(a,b)   #큰수
    num2 = min(a,b)   #작은수


    for i in range(num2, num1+1):
        for j in range(1, 10):
            print(i, "x", j, "=", i*j)
        print()


a = int(input("수를 입력하세요 안그러면 303팀이 우민기지를 파괴해서 마을에 습격이 일어나게 할 수 있습니다 :"))
b = int(input("수를 입력하세요 안그러면 303팀이 우민기지를 파괴해서 마을에 습격이 일어나게 할 수 있습니다 :"))
pigeon(a,b)
