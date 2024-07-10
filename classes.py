#
# class Student:
#     """
#     Student class
#     """
#
#     def __init__(self, first_name, last_name, passport_id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.passport_id = passport_id
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name[0]}.'
#
#
# class Mentor:
#     """
#     Mentor class
#     """
#
#     def __init__(self, first_name, last_name, passport_id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.passport_id = passport_id
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name[0]}.'
#
#
# class Course:
#     """
#     Course class
#     """
#
#     def __init__(self, name, start_date, end_date):
#         self.name = name
#         self.start_date = start_date
#         self.end_date = end_date
#
#     def __str__(self):
#         return f'{self.name} ({self.start_date} - {self.end_date})'
#
#
# class Group:
#     """
#     Group class
#     """
#
#     def __init__(self, name: str, course: Course, mentor: Mentor):
#         self.name = name
#         self.course = course
#         self.mentor = mentor
#         self.__students = []
#
#     def add_student(self, student: Student):
#         """
#         Add student to the group.
#         :param student: Student object
#         :return: None
#         """
#         if not isinstance(student, Student):
#             raise TypeError('Invalid student object')
#
#         if student in self.__students:
#             raise ValueError('Student already in the group')
#
#         self.__students.append(student)
#
#     def remove_student(self, student: Student):
#         """
#         Remove student from the group.
#         :param student: Student object
#         :return: None
#         """
#         if student not in self.__students:
#             raise ValueError('Student not in the group')
#         self.__students.remove(student)
#
#     def __str__(self):
#         return f'{self.course}-{self.mentor}\nStudents:\n' + '\n'.join(map(str, self.__students))
#
#
# def main():
#     st_1 = Student('John', 'Doe', '12345')
#     st_2 = Student('Jane', 'Doe', '54321')
#     st_3 = Student('Alice', 'Smith', '67890')
#     st_4 = Student('Bob', 'Smith', '09876')
#
#     mentor_1 = Mentor('Jack', 'Black', '13579')
#     mentor_2 = Mentor('Jill', 'White', '97531')
#
#     course_1 = Course('Python', '01.01.2020', '01.02.2020')
#     course_2 = Course('Java', '01.03.2020', '01.04.2020')
#
#     group_1 = Group('Python Pro', course_1, mentor_1)
#     group_2 = Group('Java Pro', course_2, mentor_2)
#
#     group_1.add_student(st_1)
#     group_1.add_student(st_2)
#     group_1.add_student(st_3)
#
#     group_2.add_student(st_3)
#     group_2.add_student(st_4)
#     print(group_1)
#     print(group_2)
#
#
# if __name__ == '__main__':
#     main()



# class Products:
#     """
#     Student class
#     """
#
#     def __init__(self,name: str ,price: int | float):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'{self.name} : {self.price} $'
#
#
# class Cart:
#     def __init__(self):
#         self.__products = []
#         self.__quantities = []
#
#     def add_products(self, product: Products,quantity: int|float = 1):
#         if product in self.__products:
#             index = self.__products.index(product)
#             self.__quantities[index] += quantity
#         else:
#             self.__products.append(product)
#             self.__quantities.append(quantity)
#
#     def total(self):
#         res = 0
#         for product,quantity in zip(self.__products, self.__quantities):
#             res += product.price * quantity
#         return res
#
#     def __str__(self):
#         res = '\n'.join(map(lambda item: f'{item[0]} *  {item[1]} = {item[0].price * item[1]}$',zip(self.__products, self.__quantities)))
#         res += f'Total: {self.total()} $'
#         return res
#
# p1 = Products("apple",0.69)
# p2 = Products("banana",1.00)
# p3 = Products("orange",1.50)
#
# c1 = Cart()
# c1.add_products(p1,2)
# c1.add_products(p2,4)
# c1.add_products(p3,1)
# c1.add_products(p1,3)
# print(c1)
#
#
# class Cart:
#     def __init__(self):
#         self.__products = {}
#
#     def add_products(self, product: Products,quantity: int|float = 1):
#         self.__products[product] = self.__products.get(product,0) + quantity
#
#     def total(self):
#         res = 0
#         for product,quantity in self.__products.items():
#             res += product.price * quantity
#         return res

# TASK 2

# class Dish:
#     def __init__(self, name: str, price: int | float):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name} - {self.price} UAH"
#
#
# class Category:
#     def __init__(self, name: str):
#         self.name = name
#         self.__dishes = []
#
#     def add_dish(self, dish: Dish):
#         self.__dishes.append(dish)
#
#     def __str__(self):
#         dishes = "\n".join(map(str, self.__dishes))
#         return f"{self.name}\n{dishes}"
#
#
# class Menu:
#     def __init__(self):
#         self.__categories = []
#
#     def add_category(self, category: Category):
#         self.__categories.append(category)
#
#     def __str__(self):
#         return "\n".join(map(str, self.__categories))
#
#
# dish_1 = Dish("Pizza", 10)
# dish_2 = Dish("Pasta", 15)
# dish_3 = Dish("Salad", 5)
# dish_4 = Dish("Soup", 3)
# dish_5 = Dish("Steak", 20)
# dish_6 = Dish("Burger", 7)
#
#
# category_1 = Category("Main Course")
# category_1.add_dish(dish_1)
# category_1.add_dish(dish_2)
# category_1.add_dish(dish_3)
#
# category_2 = Category("Appetizer")
# category_2.add_dish(dish_4)
# category_2.add_dish(dish_5)
# category_2.add_dish(dish_6)
#
# menu = Menu()
# menu.add_category(category_1)
# menu.add_category(category_2)
#
# print(menu)

# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name[0]}.'
# class Student(Person):
#     """
#     Student class
#     """
#     def __init__(self,first_name, last_name, passport_id):
#         super().__init__(first_name, last_name)
#         self.passport_id = passport_id


# st_1 = Student("John","Doe",'12345')
# print(st_1)
#
# class Mentor(Person):
#     def __init__(self,first_name, last_name):
#         super().__init__()


# class Discount:
#     def discount(self):
#         pass
#
#
# class RegularDiscount(Discount):
#     def discount(self):
#         disccount= 10
#         retutn
#         f'{discount}%'
#
#
# class SilverDiscount(Discount):
#     def discount(self):
#         discount = 20
#
#
# class GoldDiscount(Discount):
#     def discount(self):
#         discount = 30
# def disc(name: Discount):
#     return  name.discount()
#
# class Client:
#     def __init__(self, name, discount):
#         self.name = name
#         self.discount = discount
#
#     def get_total_price(self, order):
#         while True:
#             order = input("Enter your order:").lower
#             cupon = input("Enter name of your cupon:").lower
#             cup_disc = None
#             if cupon == 'regulardiscount':
#                 cup_disc = RegularDiscount()
#                 total = (cup_disc/100)*order
#             elif cupon == 'silverdiscount':
#                 cup_disc = SilverDiscount()
#             elif cupon == 'golddiscount':
#                 cup_disc = GoldDiscount()
#             else:
#                 print('Invalid cupon')
#                 continue
#     total = order * (cup_disc.discount()/100)
#     print(total)
#
# if __name__ == '__get_total_price__':
#     get_total_price()
#
# print(total.__dict__)

# # class Discount:
# #     def discount(self):
# #         pass
# #
# # class RegularDiscount(Discount):
# #     def discount(self):
# #         return 0.1
# #
# # class SilverDiscount(Discount):
# #     def discount(self):
# #         return 0.2
#
# class GoldDiscount(Discount):
#     def discount(self):
#         return 0.3
#
# class Client:
#     def __init__(self, name, discount):
#         self.name = name
#         self.discount = discount
#
#     def get_total_price(self, order):
#         # Calculate the total price after applying the discount
#         discount_factor = self.discount.discount()
#         total_price = sum(order) * (1 - discount_factor)
#         return total_price
#
# # Example usage:
# regular_client = Client("John", RegularDiscount())
# order_items = [10, 20, 30]  # Example order items
# total_price = regular_client.get_total_price(order_items)
# print(f"Total price for {regular_client.name}: ${total_price:.2f}")

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name[0]}.'
#
#
# class Group:
#     def __init__(self, name,group_limit = 5):
#         self.name = name
#         self.students = []
#         self.group_limit = group_limit
#
#     def add_student(self, student: Student):
#         if len(self.students) >= self.group_limit:
#             raise ValueError('The group is full')
#         if not isinstance(student, Student):
#             raise TypeError('You can add only Student object')
#         if student in self.students:
#             raise ValueError('Student already in the group')
#
#         self.students.append(student)
#
#     def __str__(self):
#         if not self.students:
#             return 'No students in the group'
#         return '\n'.join(map(str, self.students))
#
#
# st_1 = Student('John', 'Doe')
# st_2 = Student('Jane', 'Doe')
# st_3 = Student('Hope', 'Brown')
# st_4 = Student('Nancy', 'Smith')
# st_5 = Student('Erika', 'Trachuk')
# st_6 = Student('Lily', 'Blue')
#
# x = Group('Python Pro')

# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('main.log')
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# stream_handler.setLevel(logging.DEBUG
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
# class NegativeValueError(Exception):
#     """exception for negative or zero product price"""
# class Product:
#
#     def __init__(self, price: int | float, name: str):
#         if not isinstance(price,int | float):
#             logger.error('ptice must be int or float')
#             raise TypeError('Please enter integer number')
#         if price <= 0:
#             logger.error('An invalid number was entered')
#             raise NegativeValueError("Price is invalid")
#         self.price = price
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name} - {self.price} UAH"
#
#
# class Cart:
#
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add(self, product: Product, quantity: int):
#         if not isinstance(product, Product):
#             logger.error("entered product is not instance of specified class")
#             raise TypeError('You can add only Product object')
#         if quantity <= 0:
#             logger.error('quantity must be greater than zero')
#             raise ValueError('Quantity must be greater than 0')
#         if not isinstance(quantity,int):
#             logger.error("Quantity must be integer type")
#             raise TypeError('Please enter integer number')
#         logger.info(f'added {product} x {quantity}')
#         self.products.append(product)
#         self.quantities.append(quantity)
#
#     def total(self):
#         return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))
# class LimitError(Exception):
#     """ Exception for discounts out of range from 0 to 100"""
# class Discount:
#     def discount(self):
#         disc = 0
#         if not 0 <= disc <= 1:
#             logger.error("invalid value")
#             raise LimitError("Discount must be between 0 and 1")
#         return disc
#
#
# class RegularDiscount(Discount):
#     def discount(self):
#         disc = 0.1
#         if not 0<=disc<=1:
#             logger.error("invalid value")
#             raise LimitError("Discount must be between 0 and 1")
#         return disc
#
# class ChristmasDiscount(Discount):
#     def discount(self):
#         disc = 0.2
#         if not 0 <= disc <= 1:
#             logger.error("invalid value")
#             raise LimitError("Discount must be between 0 and 1")
#         return disc
#
# class SilverDiscount(Discount):
#     def discount(self):
#         disc = 0.15
#         if not 0 <= disc <= 1:
#             logger.error("invalid value")
#             raise LimitError("Discount must be between 0 and 1")
#         return disc
#
#
# class Order:
#     def __init__(self, cart: Cart, discount: Discount):
#         self.cart = cart
#         self.discount = discount
#
#     def total(self):
#         return self.cart.total() * (1 - self.discount.discount())
#
#
# if __name__ == '__main__':
#     pr_1 = Product(100, "apple")
#     pr_2 = Product(-200, "banana")
#     pr_3 = Product(300, "orange")
#
#     cart = Cart()
#     logger.info("cart was created")
#     cart.add(pr_1, -2)
#     cart.add(pr_2, 3)
#     cart.add(pr_3, 4)
#
#     type_discount = input("Enter discount type: ").lower()
#     if not type_discount.isalpha():
#         logger.error("Invalid value")
#         raise ValueError('Please enter name of the coupon')
#     if type_discount == "regular":
#         discount = RegularDiscount()
#     elif type_discount == "christmas":
#         discount = ChristmasDiscount()
#     elif type_discount == "silver":
#         discount = SilverDiscount()
#     else:
#         discount = Discount()
#
#     order = Order(cart, discount)
#     print(order.total())

# class NegativeValueError(Exception):
#     """Custom exception for negative or zero product price."""
#
# class Product:
#     def __init__(self, price: float, name: str):
#         if price <= 0:
#             raise NegativeValueError("Product price must be positive")
#         self.price = price
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name} - {self.price} UAH"
#
# class Cart:
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add(self, product: Product, quantity: int = 1):
#         if not isinstance(product, Product):
#             raise TypeError('You can add only Product object')
#         if not isinstance(quantity,int):
#             raise TypeError('Please enter integer number')
#         self.products.append(product)
#         self.quantities.append(quantity)
#
#     def total(self):
#         return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))
#
# # Example usage:
#
# pr_1 = Product(100, "apple")
# pr_2 = Product(200, 'banana')  # This will raise NegativePriceError
# pr_3 = Product(300, "orange")
#
#
# cart = Cart()
# cart.add(pr_2, 7)
# cart.add(pr_3, 4)
# print(cart.total())
#
# import logging
# logger = logging.getLogger(__nam)
#
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('main.log')
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# stream_handler.setLevel(logging.DEBUG)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
#
# class PriceError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# class Product:
#     """
#     Class for product
#     """
#     def __init__(self, name: str, price: int | float):
#         """
#         Initialize the product
#         :param name: name of the product
#         :param price: price of the product
#         """
#         if not isinstance(price, int | float):
#             logger.error("Price must be an integer or float")
#             raise TypeError("Price must be an integer or float")
#         if price <= 0:
#             logger.error("Price must be greater than 0")
#             raise PriceError("Price must be greater than 0")
#
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}: {self.price} UAH"
#
#
# class Cart:
#     def __init__(self):
#         self.__products = {}
#
#     def add_product(self, product: Product, quantity: int | float):
#         """
#         Add product to the cart
#         :param product: product to add
#         :param quantity: quantity of the product
#         :return: None
#         """
#         if not isinstance(quantity, int | float):
#             logger.error("Quantity must be an integer or float")
#             raise TypeError("Quantity must be an integer or float")
#         if quantity <= 0:
#             logger.error("Quantity must be greater than 0")
#             raise ValueError("Quantity must be greater than 0")
#         if not isinstance(product, Product):
#             logger.error("Product must be an instance of Product class")
#             raise TypeError("Product must be an instance of Product class")
#         logger.info(f"Added {product} x {quantity}")
#         self.__products[product] = self.__products.get(product, 0) + quantity
#
#     def total(self):
#         """
#         Calculate total price of the cart
#         :return: sum of the prices of all products in the cart
#         """
#         return sum(product.price * quantity for product, quantity in self.__products.items())
#
#     def __str__(self):
#         return "\n".join(f"{product} x {quantity} = {quantity * product.price}"
#                          for product, quantity in self.__products.items()) + f"\nTotal: {self.total()} UAH"
#
#
# if __name__ == "__main__":
#     try:
#         x1 = Product("Bread", 10)
#         x2 = Product("Milk", 20)
#         x3 = Product("Butter", 30)
#         x4 = Product("Cheese", 40)
#         cart = Cart()
#         logger.info("Cart created")
#         cart.add_product(x1, -2)
#         cart.add_product(x2, 3)
#         cart.add_product(x3, 4)
#         cart.add_product(x4, 5)
#         print(cart)
#     except ValueError as e:
#         print(e)
# import products, cart, discounts, order
#
#
# if __name__ == '__main__':
#     pr_1 = products.Product(100, "apple")
#     pr_2 = products.Product(200, "banana")
#     pr_3 = products.Product(300, "orange")
#
#     ct = cart.Cart()
#     ct.add(product= pr_1, quantity = 2)
#     ct.add(product= pr_2, quantity = 3)
#     ct.add(product= pr_3, quantity = 4)
#
#     type_discount = input("Enter discount type: ")
#     if type_discount == "regular":
#         discount = discounts.RegularDiscount()
#     elif type_discount == "christmas":
#         discount = discounts.ChristmasDiscount()
#     elif type_discount == "silver":
#         discount = discounts.SilverDiscount()
#     else:
#         discount = discounts.Discount()
#     order1 = order.Order(ct, discount)
#     print(order1.total())
import random as rnd
# class Circle:
#     def __init__(self, point: tuple, r: int):
#         self.point = point
#         self.r = r
#     def __mul__(self,other):
#         return Circle(self.point,self.r * other)
#
#     def radius(self):
#         return self.r
#
#     def __eq__(self, other):
#         return self.radius() == other.radius()
#
#     def __ne__(self, other):
#         return self.radius() != other.radius()
#
#     def __lt__(self, other):
#         return self.radius() < other.radius()
#
#     def __le__(self, other):
#         return self.radius() <= other.radius()
#
#     def __gt__(self, other):
#         return self.radius() > other.radius()
#
#     def __ge__(self, other):
#         return self.radius() >= other.radius()
#
#     def __str__(self):
#         x,y = self.point
#         return f'Circle with center: {x},{y}, Radius = {self.r} '
#
# circ_1 = Circle((2,3),4)
# circ_2 = Circle((2,3),5)
# print(circ_1 < circ_2)


# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name[0]}.'
#
#
# class Group:
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#
#     def __iadd__(self, student: Student):
#         if not isinstance(student, Student):
#             raise TypeError('You can add only Student object')
#         if student in self.students:
#             raise ValueError('Student already in the group')
#
#         self.students.append(student)
#         return self
#
#     def __str__(self):
#         if not self.students:
#             return 'No students in the group'
#         return '\n'.join(map(str, self.students))
#
#
# st_1 = Student('John', 'Doe')
# st_2 = Student('Jane', 'Doe')
#
# x = Group('Python Pro')
# x += st_1
# x += st_2
# print(x)