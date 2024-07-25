import sqlite3 as sql

con = sql.connect('data.db')
cur = con.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS warehouse (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT UNIQUE,
        quantity INTEGER,
        price INTEGER
    )
    '''
)

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS basket (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT UNIQUE,
        quantity INTEGER,
        price INTEGER
    )
    '''
)


def insert_product_warehouse(product_name, quantity, price):
    with sql.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(
            '''
            INSERT OR REPLACE INTO warehouse (product_name, quantity, price)
            VALUES (?, ?, ?)
            ''', (product_name, quantity, price)
        )
        con.commit()


def insert_product_basket_and_update_warehouse(product_name, price):
    con = sql.connect('data.db')
    cur = con.cursor()

    # Проверка наличия товара на складе
    cur.execute("SELECT quantity FROM warehouse WHERE product_name = ?", (product_name,))
    warehouse_result = cur.fetchone()

    if warehouse_result and warehouse_result[0] > 0:
        # Товар есть на складе, уменьшаем количество на складе
        new_warehouse_quantity = warehouse_result[0] - 1
        cur.execute("UPDATE warehouse SET quantity = ? WHERE product_name = ?",
                    (new_warehouse_quantity, product_name))

        # Проверка наличия товара в корзине
        cur.execute("SELECT quantity FROM basket WHERE product_name = ?", (product_name,))
        basket_result = cur.fetchone()

        if basket_result:
            # Товар уже есть в корзине, увеличиваем количество на 1
            new_basket_quantity = basket_result[0] + 1
            cur.execute("UPDATE basket SET quantity = ? WHERE product_name = ?",
                        (new_basket_quantity, product_name))
        else:
            # Товара нет в корзине, добавляем его с количеством 1
            cur.execute("INSERT INTO basket (product_name, quantity, price) VALUES (?, ?, ?)",
                        (product_name, 1, price))
        # Фиксация изменений
        con.commit()
        con.close()
    else:
        print("Товар отсутствует на складе или его количество равно нулю.")
        con.close()


def get_product_from_warehouse():
    with sql.connect('data.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM warehouse")
        products = cur.fetchall()
    return products


def get_product_from_basket():
    with sql.connect('data.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM basket")
        products = cur.fetchall()
    return products


def delete_product_from_basket(name):
    with sql.connect('data.db') as con:
        cur = con.cursor()
        old_quantity = cur.execute("SELECT quantity FROM basket WHERE product_name=?", (name,))
        cur.execute("UPDATE warehouse SET quantity = quantity + 1")
        cur.execute("DELETE FROM basket WHERE product_name=?", (name,))
        con.commit()


# Закрытие соединения
con.close()
