cur_tem = 20

def set_temp(des_tem):
    global cur_tem

    if (cur_tem <des_tem):
        while (cur_tem < des_tem):
            cur_tem +=1
            print("현재온도는 %d도 입니다"%cur_tem)
    else:
        while (cur_tem > des_tem):
            cur_tem -=1
            print("현재온도는 %d도 입니다"%cur_tem)


while True:
    put = input("원하는 온도를 설정해 주세요")
    if (put == "종료"):
        print("종료")
        break
    elif (put <= "30" and put >= "18"):
        print("현재 온도는 %d도 입니다"%cur_tem)
        set_temp(int(put))
    else:
        print("입력을 확인해주세요")
set_temp(25)
