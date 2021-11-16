class score:
    def __init__(self, name, english, korean):
        self.name = name
        self.english = english
        self.korean = korean

    def prn(self):
        print("%s %d %d"%(self.name, self.english, self.korean))


name, english, korean = input().split()
st1 = score(name, int(english), int(korean))

name, english,korean = input().split()
st2 = score(name, int(english), int(korean))

hap = score("합계", st1.english + st2.english, st1.korean + st2.korean)

st1.prn()
st2.prn()
hap.prn()
