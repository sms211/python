class FishBread:
    def make_bread(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price

    def see_make(self):
        print(self.ingredients, self.price)

a = FishBread()
b = FishBread()


a.make_bread("버섯 스튜", 9000)
b.make_bread("꿀", 9000)

a.see_make()
b.see_make()
