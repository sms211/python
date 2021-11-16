class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input("이름은?")
age = int(input("나이는?"))
st = student(name, age)


print("당신의 이름은 %s이고"%st.name, end=' ')
print("나이는 %d 이군요"%st.age)
