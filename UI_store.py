import file
import shop
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Создаем основное окно
root = Tk()
root.title("Online Store")
root.geometry("800x600")
root.configure(bg="#ffffff")

# Стилизация ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="#ffffff", background="#5f9ea0", padding=10)
style.map("TButton", background=[("active", "#4682b4")])  # Цвет при наведении
style.configure("TLabel", font=("Helvetica", 12), background="#ffffff")
style.configure("TFrame", background="#ffffff")
style.configure("TEntry", font=("Helvetica", 12))


def owner_window():
    admin_screen = Toplevel(root)
    admin_screen.title("Owner Window")
    admin_screen.geometry("600x500")
    admin_screen.configure(bg="#ffffff")

    def show_balance():
        balance = shop.store.display_balance()
        messagebox.showinfo("Balance", f"Your Balance: {balance}")

    display_balance = ttk.Button(admin_screen, text="Display Balance", command=show_balance)
    display_balance.pack(ipadx=20, ipady=10, anchor=N, pady=15)

    def add_balance():
        balance_screen = Toplevel(admin_screen)
        balance_screen.title("Increase Balance")
        balance_screen.geometry("300x200")
        balance_screen.configure(bg="#ffffff")

        amount_label = ttk.Label(balance_screen, text="Enter amount:")
        amount_label.pack(pady=5)

        amount_entry = ttk.Entry(balance_screen)
        amount_entry.pack(pady=5)

        def submit_balance():
            try:
                amount = int(amount_entry.get())
                shop.store.add_balance(amount)
                messagebox.showinfo("Success",
                                    f"Added {amount} to balance. New balance: {shop.store.display_balance()}")
                balance_screen.destroy()
            except ValueError:
                messagebox.showerror('Error', 'Please enter a valid number')

        submit_button = ttk.Button(balance_screen, text="OK", command=submit_balance)
        submit_button.pack(pady=10)

    add_balance = ttk.Button(admin_screen, text="Increase Balance", command=add_balance)
    add_balance.pack(ipadx=20, ipady=10, pady=15)

    def restock_product():
        restock_screen = Toplevel(admin_screen)
        restock_screen.title("Restock")
        restock_screen.geometry("400x300")
        restock_screen.configure(bg="#ffffff")

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
        warehouse_screen.geometry("700x500")
        warehouse_screen.configure(bg="#ffffff")

        products = shop.warehouse.product_list

        header_frame = ttk.Frame(warehouse_screen)
        header_frame.pack(pady=10)

        header_name = Label(header_frame, text="Product Name", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_name.pack(side=LEFT, padx=10)

        header_quantity = Label(header_frame, text="Quantity", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_quantity.pack(side=LEFT, padx=10)

        header_price = Label(header_frame, text="Price", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_price.pack(side=LEFT, padx=10)

        products_frame = ttk.Frame(warehouse_screen)
        products_frame.pack(pady=10)

        for product in products:
            product_frame = ttk.Frame(products_frame)
            product_frame.pack(fill=X, pady=5)

            name_label = Label(product_frame, text=product.name_product, width=20, borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            name_label.pack(side=LEFT, padx=10)

            quantity_label = Label(product_frame, text=product.quantity, width=20, borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            quantity_label.pack(side=LEFT, padx=10)

            price_label = Label(product_frame, text=product.price, width=20, borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            price_label.pack(side=LEFT, padx=10)

    btn_display_warehouse = ttk.Button(admin_screen, text='Display Warehouse', command=display_warehouse)
    btn_display_warehouse.pack(ipadx=15, ipady=10, pady=15)


def user_window():
    user_screen = Toplevel(root)
    user_screen.title("User Screen")
    user_screen.geometry("700x500")
    user_screen.configure(bg="#ffffff")

    def display_warehouse_client():
        warehouse_screen = Toplevel(user_screen)
        warehouse_screen.title("Warehouse")
        warehouse_screen.geometry("700x500")
        warehouse_screen.configure(bg="#ffffff")

        products = shop.warehouse.product_list

        header_frame = ttk.Frame(warehouse_screen)
        header_frame.pack(pady=10)

        header_name = Label(header_frame, text="Product Name", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_name.grid(row=0, column=0, padx=5, pady=5)

        header_quantity = Label(header_frame, text="Quantity", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_quantity.grid(row=0, column=1, padx=5, pady=5)

        header_price = Label(header_frame, text="Price", width=20, borderwidth=1, relief="solid", bg="#d3d3d3", font=("Helvetica", 10, "bold"))
        header_price.grid(row=0, column=2, padx=5, pady=5)

        header_action = Label(header_frame, text="      ", width=10, borderwidth=0, relief="solid", bg="#ffffff", font=("Helvetica", 10, "bold"))
        header_action.grid(row=0, column=3, padx=5, pady=5)

        products_frame = ttk.Frame(warehouse_screen)
        products_frame.pack(pady=10)

        for i, product in enumerate(products):
            name_label = Label(products_frame, text=product.name_product, width=20, height=2,  borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            name_label.grid(row=i+1, column=0, padx=5, pady=5)

            quantity_label = Label(products_frame, text=product.quantity, width=20, height=2, borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            quantity_label.grid(row=i+1, column=1, padx=5, pady=5)

            price_label = Label(products_frame, text=product.price, width=20, height=2, borderwidth=1, relief="solid", bg="#f5f5f5", font=("Helvetica", 10))
            price_label.grid(row=i+1, column=2, padx=5, pady=5)

            buy_button = ttk.Button(products_frame, text='BUY', width=6,
                                    command=lambda p=product: shop.basket.add_product(p.name_product, 1))
            buy_button.grid(row=i + 1, column=3, padx=5, pady=5)

    btn_goods = ttk.Button(user_screen, text="Goods", command=display_warehouse_client)
    btn_goods.pack(pady=30)

    btn_basket = ttk.Button(user_screen, text="Basket")
    btn_basket.pack(pady=20)


def exit_app():
    file.save_file(shop.warehouse.product_list)
    root.destroy()


btn_own = ttk.Button(root, text="Owner", command=owner_window)
btn_usr = ttk.Button(root, text="Customer", command=user_window)
btn_exit = ttk.Button(root, text="Exit", command=exit_app)

btn_own.pack(expand=True, ipadx=30, ipady=20, anchor=N, pady=20)
btn_usr.pack(expand=True, ipadx=30, ipady=20, anchor=N, padx=20)
btn_exit.pack(expand=True, ipadx=30, ipady=20, pady=100, padx=100)

btn_own.configure(style="TButton")
btn_usr.configure(style="TButton")
btn_exit.configure(style="TButton")

shop.warehouse.product_list = file.loading_file()

root.mainloop()
