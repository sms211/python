from tkinter import *
from tkinter import ttk


operation = "" #연산자 저장함수 (+, -, *, /)
temp_number = 0 #이진갚 저장변수

#숫자버튼 처리 함수
def button_pressed(value):
    #만약 입력값이 AC라면
    if value == "AC":
        num_entry.delete(0, "end")
        print("AC pressed")
    else:       #그 외에 0부터 9까지 수
        num_entry.insert("end", value)
        print(value, "pressed")
#사칙연산 처리
def math_button_pressed(value):
    global operation
    global temp_number
    if not num_entry.get() == "":
        operation = value
        temp_number = int(num_entry.get())
        num_entry.delete(0, "end")
        print(temp_number,operation)


def equal_button_pressed():
    global operation
    global temp_number
    if not (operation =="" and num_entry.get()==""):
        number = int(num_entry.get())

        if operation == "/":
            solution = temp-number/number
        elif operation == "*":
            solution = temp_number*number
        elif operation == "+":
            solution = temp_number+number
        else:
            solution = temp_number-number


        #계산 후, 숫자표시칸을 비우고 계산결과를 표시

        num_entry.delete(0, "end")
        num_entry.insert(0, solution)
        print(temp_number, operation, number, "=", solution)
        operation =""
        temp_number = 0
        
root = Tk()
root.title("Calculator")
root.geometry("300x300")

#텍스트창의 값을 저장할 변수
entry_value = StringVar(root, value="")

#textvariable 속성의로 함수 설정
num_entry = ttk.Entry(root, textvariable = entry_value, width=20)
num_entry.grid(row=0, columnspan=3)

#숫자 버튼
button7 = ttk.Button(root, text="7", command=lambda:button_pressed("7"))
button7.grid(row=1, column=0)
button8 = ttk.Button(root, text="8", command=lambda:button_pressed("8"))
button8.grid(row=1, column=1)
button9 = ttk.Button(root, text="9", command=lambda:button_pressed("9"))
button9.grid(row=1, column=2)
#사칙연산 버튼 -> math_button_pressed()
button_div = ttk.Button(root, text="/", command = lambda:math_button_pressed("/"))
button_div.grid(row=1, column=3)

button_mult = ttk.Button(root, text="*", command = lambda:math_button_pressed("*"))
button_mult.grid(row=2, column=3)

button_add = ttk.Button(root, text="+", command = lambda:math_button_pressed("+"))
button_add.grid(row=3, column=3)

button_minus = ttk.Button(root, text="-", command = lambda:math_button_pressed("-"))
button_minus.grid(row=4, column=3)

button4 = ttk.Button(root, text="4", command=lambda:button_pressed("4"))
button4.grid(row=2, column=0)
button5 = ttk.Button(root, text="5", command=lambda:button_pressed("5"))
button5.grid(row=2, column=1)
button6 = ttk.Button(root, text="6", command=lambda:button_pressed("6"))
button6.grid(row=2, column=2)

button1 = ttk.Button(root, text="1", command=lambda:button_pressed("1"))
button1.grid(row=3, column=0)
button2 = ttk.Button(root, text="2", command=lambda:button_pressed("2"))
button2.grid(row=3, column=1)
button2 = ttk.Button(root, text="3", command=lambda:button_pressed("3"))
button2.grid(row=3, column=2)

button0 = ttk.Button(root, text="0", command=lambda:button_pressed("0"))
button0.grid(row=4, column=1)
button_ac = ttk.Button(root,text="AC", command = lambda:button_pressed("AC"))
button_ac.grid(row=4, column=0)
button_equal = ttk.Button(root, text="=", command = lambda:equal_button_pressed())
button_equal.grid(row=4, column=2)



root.mainloop()

