class sport:
    def buy_ticket(self, sport_name, price):
        self.sport_name = sport_name
        self.price= price


    def show_ticket(self):
        print(self.sport_name, self.price)


    def __add__(self, other):
        return self.price + other.price


a = sport()
b = sport()

a.buy_ticket("축구", 10000)
b.buy_ticket("야구", 15000)


print("두 경기 가격은 %d원"% int(a + b))
