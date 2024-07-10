class Product:

    def __init__(self, price: int | float, name: str):
        self.price = price
        self.name = name

    def __str__(self):
        return f"{self.name} - {self.price} UAH"