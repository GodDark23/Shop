from datetime import datetime


class Store:
    def __init__(self):
        self.balance = 10000
        self.orders = []

    def add_balance(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f'Your balance: {self.balance}')
        return self.balance

    # def add_order(self, order):
    # self.orders.append(order)

    def display_orders(self):
        for order in self.orders:
            print(f'Name: {order.user_name} Basket: {order.basket}  Total price {order.total} Data: {order.date}')


class Product:
    def __init__(self, name_product, quantity, price):
        self.name_product = name_product
        self.quantity = quantity
        self.price = price


class Warehouse:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def get_quantity(self, product_name):
        for product in self.product_list:
            if product.name_product == product_name:
                return product.quantity
        return 0  # Возвращаем 0, если продукт не найден

    def reduce_quantity(self, product_name, quantity):
        for product in self.product_list:
            if product.name_product == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    return True
                else:
                    return False
        return False

    def delete_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)

    def display_product_list(self):
        for product in self.product_list:
            print(f"product: {product.name_product}, quantity: {product.quantity}, price: {product.price}")

    def find_product(self, product_name):
        for product in self.product_list:
            if product.name_product == product_name:
                return product


class Basket:
    def __init__(self):
        self.basket_list = []

    def calculate_price(self):  # Не работает нужно починить. Скорее всего ошибка в распаковке
        pass

    def add_product(self, product): # возможно ли доработать?
        if warehouse.get_quantity(product.name_product) > 0:
            if warehouse.reduce_quantity(product.name_product, 1):
                # Проверка, есть ли уже этот продукт в корзине
                for item in self.basket_list:
                    if item.name_product == product.name_product:
                        item.quantity += 1
                        print(f'Added {item.quantity} of {item.name_product} to basket. Total price: {item.quantity * item.price}')
                        return
                # Если продукта еще нет в корзине, добавляем его
                self.basket_list.append(Product(product.name_product, 1, product.price))
                print(f'Added {product.name_product} to basket. Total price: {product.price}')
            else:
                print(f'Insufficient quantity of {product.name_product} in warehouse')
        else:
            print(f'Insufficient quantity of {product.name_product} in warehouse')

    def delete_product(self, prod):  # скорее всего косяк
        for index, product in enumerate(self.basket_list):
            if product.name_product == prod:
                product.quantity += 1
                del self.basket_list[index]
                return
        print(f"Product {prod} not found in basket")

    def display_basket(self):
        if len(self.basket_list) != 0:
            for product, quantity in self.basket_list:
                print(
                    f"That's your Basket \n product: {product.name_product}, quantity: {quantity}, "
                    f"price: {product.price * quantity}")
        else:
            print(f'Basket is empty')

    def clear_basket(self):
        self.basket_list = []

    def add_basket_to_order(self, client_name):
        order = Order(client_name, self.basket_list, self.calculate_price())
        store.add_order(order)
        store.add_balance(order.total)
        self.clear_basket()


class Client:
    def __init__(self, client_name):
        self.client_name = client_name

    def place_order(self):
        basket.add_basket_to_order(self.client_name)

    def view_warehouse(self):
        warehouse.display_product_list()

    def view_orders(self):
        basket.display_basket()


class Order:
    def __init__(self, user_name, user_basket, total):
        self.date = datetime.now()
        self.user_name = user_name
        self.basket = user_basket
        self.total = total


store = Store()
warehouse = Warehouse()
basket = Basket()
