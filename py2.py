class student:
    def __init__(self, name, school, age):
        self.name = name
        self.school = school
        self.age = age


name = input("name?")
school = input("school?")
age = int(input("grade?"))
st = student(name, school, age)


print("Name:%s"%name)
print("School:%s"%school)
print("Grade:%d"%age)
