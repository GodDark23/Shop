import shop

path = "./Shopping App.txt"


def save_file(product_list):
    with open(path, "w", encoding='utf-8') as file:
        for product in product_list:
            file.write(f'{product.name_product};{product.price};{product.quantity}\n')
    print('File Saved')


def loading_file():
    product_list = []
    try:
        with open(path, "r", encoding='utf-8') as file:
            for line in file:
                # Разбиваем строку по разделителю ";" и преобразуем данные в соответствующие типы
                name_product, price_str, quantity_str = line.strip().split(";")
                price = int(price_str)
                quantity = int(quantity_str)
                # Создаем объект Product и добавляем его в список
                product = shop.Product(name_product, quantity, price)
                product_list.append(product)
    except FileNotFoundError:
        print(f"File {path} not found. Creating new file...")
        # Создаем пустой список продуктов и сохраняем его в файл
        save_file(product_list)
    return product_list
