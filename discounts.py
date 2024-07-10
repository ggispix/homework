class Discount:
    def discount(self):
        return 0


class RegularDiscount(Discount):
    def discount(self):
        return 0.1


class ChristmasDiscount(Discount):
    def discount(self):
        return 0.2


class SilverDiscount(Discount):
    def discount(self):
        return 0.15
