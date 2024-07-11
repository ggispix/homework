import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class PriceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Product:
    """
    Class for product
    """
    def __init__(self, name: str, price: int | float):
        """
        Initialize the product
        :param name: name of the product
        :param price: price of the product
        """
        if not isinstance(price, int | float):
            logger.error("Price must be an integer or float")
            raise TypeError("Price must be an integer or float")
        if price <= 0:
            logger.error("Price must be greater than 0")
            raise PriceError("Price must be greater than 0")

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


class Cart:
    def __init__(self):
        self.__products = {}

    def add_product(self, product: Product, quantity: int | float):
        """
        Add product to the cart
        :param product: product to add
        :param quantity: quantity of the product
        :return: None
        """
        if not isinstance(quantity, int | float):
            logger.error("Quantity must be an integer or float")
            raise TypeError("Quantity must be an integer or float")
        if quantity <= 0:
            logger.error("Quantity must be greater than 0")
            raise ValueError("Quantity must be greater than 0")
        if not isinstance(product, Product):
            logger.error("Product must be an instance of Product class")
            raise TypeError("Product must be an instance of Product class")
        logger.info(f"Added {product} x {quantity}")
        self.__products[product] = self.__products.get(product, 0) + quantity

    def total(self):
        """
        Calculate total price of the cart
        :return: sum of the prices of all products in the cart
        """
        return sum(product.price * quantity for product, quantity in self.__products.items())

    def __str__(self):
        return "\n".join(f"{product} x {quantity} = {quantity * product.price}"
                         for product, quantity in self.__products.items()) + f"\nTotal: {self.total()} UAH"


if __name__ == "__main__":
    try:
        x1 = Product("Bread", 10)
        x2 = Product("Milk", 20)
        x3 = Product("Butter", 30)
        x4 = Product("Cheese", 40)
        cart = Cart()
        logger.info("Cart created")
        cart.add_product(x1, -2)
        cart.add_product(x2, 3)
        cart.add_product(x3, 4)
        cart.add_product(x4, 5)
        print(cart)
    except ValueError as e:
        print(e)
print(e)
