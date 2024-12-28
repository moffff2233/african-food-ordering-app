from tkinter import *
from tkinter import messagebox

class FoodOrderingApp:
    def __init__(self, master):
        self.master = master
        master.title("African Food Ordering App")

        self.food_items = {
            "Jollof Rice": 10,
            "Egusi Soup": 12,
            "Pounded Yam": 8,
            "Suya": 15,
            "Fried Plantain": 5
        }

        self.beverages = {
            "Zobo": 3,
            "Chapman": 4,
            "Palm Wine": 6
        }

        self.order = {}

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="Select Food Items").grid(row=0, column=0, padx=10, pady=10)
        self.food_var = StringVar()
        self.food_menu = OptionMenu(self.master, self.food_var, *self.food_items.keys())
        self.food_menu.grid(row=1, column=0)

        Label(self.master, text="Select Beverages").grid(row=2, column=0, padx=10, pady=10)
        self.beverage_var = StringVar()
        self.beverage_menu = OptionMenu(self.master, self.beverage_var, *self.beverages.keys())
        self.beverage_menu.grid(row=3, column=0)

        Button(self.master, text="Add to Order", command=self.add_to_order).grid(row=4, column=0, padx=10, pady=10)
        Button(self.master, text="Calculate Total", command=self.calculate_total).grid(row=5, column=0, padx=10, pady=10)

        self.total_label = Label(self.master, text="Total: $0")
        self.total_label.grid(row=6, column=0, padx=10, pady=10)

    def add_to_order(self):
        food_item = self.food_var.get()
        beverage_item = self.beverage_var.get()

        if food_item:
            self.order[food_item] = self.food_items[food_item]
        if beverage_item:
            self.order[beverage_item] = self.beverages[beverage_item]

        messagebox.showinfo("Order Update", f"Added to order: {food_item} and {beverage_item}")

    def calculate_total(self):
        total = sum(self.order.values())
        self.total_label.config(text=f"Total: ${total}")

if __name__ == "__main__":
    root = Tk()
    app = FoodOrderingApp(root)
    root.mainloop()