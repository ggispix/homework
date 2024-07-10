# import cart,discounts
#
# class Order:
#     def __init__(self, cart: cart.Cart, discount: discounts.Discount):
#         self.cart = cart
#         self.discount = discount
#
#     def total(self):
#         return self.cart.total() * (1 - self.discount.discount())
