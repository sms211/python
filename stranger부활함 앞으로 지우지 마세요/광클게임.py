from tkinter import *
from tkinter import messagebox
import threading, time

root = Tk()
root.title("10초동안 버튼 광클")
root.geometry("200x200+500+100")


count = 0 #클릭한 횟수 저장공간
Stime = 10 #남은시간(초)


def play():
    btn2.place(x=60, y=80)
    btn.place(x=-1000, y=-1000)
    global Stime
    global count
    if Stime > 0:
        root.after(1000, play)
        Stime -= 1
        timebox.config(text=f'남은 시간 {Stime}초')
    else:
        Stime = 0
        if count < 10:
            point = str(count) + "점입니다...못하네요"
        elif 11 < count < 45:
            point = str(count) + "점입니다.보통이네요"
        else:
            point = str(count) + "fnf bf is sus?or creeper is sus?"

        messagebox.showinfo("점수", point)
        btn3.place(x=60, y=80)

def score():
    global Stime
    global count
    if Stime > 0:
        count += 1
        pointbox.config(text=count)

def replay():
    global Stime
    global count
    Stime = 10
    count = 0
    btn3.place(x=-1000, y=-1000)
    btn.place(x=60, y=80)

#타이틀
title = Label(root, text = "마우스 광클 게임")
title.pack()

#시간
timebox = Label(root, text=f'남은 시간{Stime}')
timebox.pack()

#점수
pointbox = Label(root, text=count)
pointbox.pack()

#버튼
btn2 = Button(root, text="누르세요",width=10, height=2, command=score)
btn = Button(root, text="시작",width=10, height=2, command=play)
btn3 = Button(root, text="다시하기",width=10, height=2, command=replay)
btn.place(x=60, y=80)
btn2.place(x=-1000, y=-100)

root.mainloop()
