class Human:
    default_name = "None"
    default_age = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self._money = 0
        self._house = None

    def info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Деньги:", self._money)
        print("Дом:", self._house)


    @staticmethod
    def default_info():
        print("Default Name:", Human.default_name)
        print("Default Age:", Human.default_age)

    def _make_deal(self, house, price):
        self._money -= price
        self._house = house

    def earn_money(self, value):
        self._money += value
        print("Получено:", value, "Рублей,", "Текущие деньги:", self._money)


    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self._money < final_price:
            print("Не хватает денег")
        else:
            self._make_deal(house, final_price)



class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print("Окончательная цена:", final_price)
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    Human.default_info()

    Ivan = Human('Иван', 70)
    Ivan.info()

    small_house = SmallHouse(10_500)

    Ivan.buy_house(small_house, 5)

    Ivan.earn_money(5_000)
    Ivan.buy_house(small_house, 5)

    Ivan.earn_money(100_000)
    Ivan.buy_house(small_house, 5)
    Ivan.info()