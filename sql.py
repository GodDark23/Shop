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
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute(
        '''
        INSERT OR REPLACE INTO warehouse (product_name, quantity, price)
        VALUES (?, ?, ?)
        ''', (product_name, quantity, price)
    )
    con.commit()


def insert_product_basket(product_name, quantity, price):
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute(
        '''
        INSERT OR REPLACE INTO basket (product_name, quantity, price)
        VALUES (?, ?, ?)
        ''', (product_name, quantity, price)
    )
    con.commit()


def get_product_from_warehouse():
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM warehouse")
    products = cur.fetchall()

    con.close()
    return products


def get_product_from_basket():
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM basket")
    products = cur.fetchall()

    con.close()
    return products


def delete_product_from_basket(x_id):
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute("DELETE FROM basket WHERE id=?", (x_id,))
    con.commit()


# можно удалить
cur.execute("SELECT * FROM warehouse")
rows = cur.fetchall()
for row in rows:
    print(row)

# Закрытие соединения
con.close()
