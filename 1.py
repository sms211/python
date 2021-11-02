def inp(): #입력
    global a,b
    a = int(input("수를 입력하세요 아니면 히로빈이 당신의 집으로 찾아갈수도 있습니다"))
    b = int(input("다시 수를 입력하세요 아니면 히로빈이 당신의 집으로 찾아갈수도 있습니다"))

def clac():   #계산
    global plus, multi
    plus = a + b
    multi = a * b

def outp():   #출력
    print("합:%d"%plus)
    print("곱:%d"%multi)


inp()
clac()
outp()
