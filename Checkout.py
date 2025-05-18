class Checkout:
    class Discount:
        def __init__(self, numberItems, price):
            self.numberItems = numberItems
            self.price = price

    def __init__(self):
        self.items = {}
        self.prices = {}
        self.discounts = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.numberItems:
                    numb = cnt / discount.numberItems
                    total += numb * discount.price
                    remaining = cnt % discount.numberItems
                    total += self.prices[item] * remaining
                else:
                    total += self.prices[item] * cnt
            else:
                total += cnt * self.prices[item]
        return total

    def addDiscount(self, item, numberItems, price):
        discount = self.Discount(numberItems, price)
        self.discounts[item] = discount
