import shop
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Online Store")
root.geometry("600x500")


def owner_window():
    admin_screen = Toplevel(root)
    admin_screen.title("Owner Window")
    admin_screen.geometry("500x400")

    def show_balance():
        balance = shop.store.display_balance()
        messagebox.showinfo("Balance", f"Your Balance: {balance}")

    display_balance = ttk.Button(admin_screen, text=f"Display Balance", command=show_balance)
    display_balance.pack(ipadx=20, ipady=10, anchor=N, pady=15)

    def add_balance():
        balance_screen = Toplevel(admin_screen)
        balance_screen.title("Increase Balance")
        balance_screen.geometry("250x200")

        amount_label = ttk.Label(balance_screen, text="Enter amount:")
        amount_label.pack(pady=5)

        amount_entry = ttk.Entry(balance_screen)
        amount_entry.pack(pady=5)

        def submit_balance():
            amount = int(amount_entry.get())
            shop.store.add_balance(amount)
            messagebox.showinfo("Success", f"Added {amount} to balance. New balance: {shop.store.display_balance()}")
            balance_screen.destroy()  # Закрыть окно после успешного добавления

        submit_button = ttk.Button(balance_screen, text="OK", command=submit_balance)
        submit_button.pack(pady=10)

    add_balance = ttk.Button(admin_screen, text="Increase Balance", command=add_balance)
    add_balance.pack(ipadx=20, ipady=10, pady=15)

    def restock_product():
        restock_screen = Toplevel(admin_screen)
        restock_screen.title("Restock")
        restock_screen.geometry("400x300")

        product_name_label = ttk.Label(restock_screen, text="Enter name product:")
        product_name_label.pack(pady=10)

        name_entry = ttk.Entry(restock_screen)
        name_entry.pack()

        product_quantity_label = ttk.Label(restock_screen, text="Enter amount of Product")
        product_quantity_label.pack(pady=10)

        quantity_entry = ttk.Entry(restock_screen)
        quantity_entry.pack(pady=10)

        product_price_label = ttk.Label(restock_screen, text="Enter cost of Product")
        product_price_label.pack()

        price_entry = ttk.Entry(restock_screen)
        price_entry.pack(pady=10)

        def submit_product():
            name_product = name_entry.get()
            quantity = int(quantity_entry.get())
            price = int(price_entry.get())

            new_product = shop.Product(name_product, quantity, price)
            shop.warehouse.add_product(new_product)
            messagebox.showinfo("Success!", f"Product {name_product} added to warehouse")
            restock_screen.destroy()

        submit_button = ttk.Button(restock_screen, text="OK", command=submit_product)
        submit_button.pack(pady=15)

    btn_restock = ttk.Button(admin_screen, text='Restock Product', command=restock_product)
    btn_restock.pack(ipadx=20, ipady=10, pady=15)

    def display_warehouse():
        warehouse_screen = Toplevel(admin_screen)
        warehouse_screen.title("Warehouse")
        warehouse_screen.geometry("600x800")

        products = shop.warehouse.product_list

        header_frame = Frame(warehouse_screen)
        header_frame.pack(pady=10)

        header_name = Label(header_frame, text="Product Name", width=20, borderwidth=1, relief="solid")
        header_name.pack(side=LEFT, padx=10)

        header_quantity = Label(header_frame, text="Quantity", width=20, borderwidth=1, relief="solid")
        header_quantity.pack(side=LEFT, padx=10)

        header_price = Label(header_frame, text="Price", width=20, borderwidth=1, relief="solid")
        header_price.pack(side=LEFT, padx=10)

        products_frame = Frame(warehouse_screen)
        products_frame.pack(pady=10)

        for product in products:
            product_frame = Frame(products_frame)
            product_frame.pack(fill=X, pady=5)

            name_label = Label(product_frame, text=product.name_product, width=20, borderwidth=1, relief="solid")
            name_label.pack(side=LEFT, padx=10)

            quantity_label = Label(product_frame, text=product.quantity, width=20, borderwidth=1, relief="solid")
            quantity_label.pack(side=LEFT, padx=10)

            price_label = Label(product_frame, text=product.price, width=20, borderwidth=1, relief="solid")
            price_label.pack(side=LEFT, padx=10)

    btn_display_warehouse = ttk.Button(admin_screen, text='Display Warehouse', command=display_warehouse)
    btn_display_warehouse.pack(ipadx=15, ipady=10, pady=15)


def user_window():
    user_screen = Toplevel(root)
    user_screen.title("Add_Balance")
    user_screen.geometry("500x400")

    btn_basket = ttk.Button(user_screen, text="Basket")
    btn_basket.pack(pady=20)

    btn_goods = ttk.Button(user_screen, text="Goods")
    btn_goods.pack(pady=30)


btn_own = ttk.Button(root, text="Owner", command=owner_window)
btn_usr = ttk.Button(root, text="Customer", command=user_window)
btn_exit = ttk.Button(root, text="Exit", command=root.destroy)

btn_own.pack(expand=True, ipadx=30, ipady=20, anchor=N, pady=50)
btn_usr.pack(expand=True, ipadx=30, ipady=20, pady=10, padx=100)
btn_exit.pack(expand=True, ipadx=30, ipady=20, pady=100, padx=100)

root.mainloop()
