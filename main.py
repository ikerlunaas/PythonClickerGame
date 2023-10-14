import tkinter as tk
import pickle

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")

        root.protocol("WM_DELETE_WINDOW", self.save_data)  # Save data when closing the window

        self.load_data()  # Load data from a file

        # Click button
        self.click_button = tk.Button(root, text="Click Me", command=self.click)
        self.click_button.pack(pady=10)

        # Display click count
        self.click_label = tk.Label(root, text=f"Clicks: {self.click_count}")
        self.click_label.pack()

        # Shop
        self.shop_label = tk.Label(root, text="Shop:")
        self.shop_label.pack()

        # Multiplier button
        self.multiplier_button = tk.Button(root, text=f"Buy Multiplier ({self.multiplier_cost} clicks)", command=self.buy_multiplier)
        self.multiplier_button.pack()

        # Display the number of multipliers and current multiplier
        self.multiplier_count_label = tk.Label(root, text=f"Multipliers: {self.multiplier}")
        self.multiplier_count_label.pack()

        self.update_labels()

        root.protocol("WM_DELETE_WINDOW", self.save_data)  # Save data when closing the window

    def click(self):
        self.click_count += self.multiplier
        self.update_labels()

    def buy_multiplier(self):
        if self.click_count >= self.multiplier_cost:
            self.multiplier += 1
            self.click_count -= self.multiplier_cost
            self.multiplier_cost *= 2
            self.update_labels()

    def update_labels(self):
        self.click_label.config(text=f"Clicks: {self.click_count}")
        self.multiplier_button.config(text=f"Buy Multiplier ({self.multiplier_cost} clicks)")
        self.multiplier_count_label.config(text=f"Multipliers: {self.multiplier}")

    def load_data(self):
        try:
            with open("clicker_data.pkl", "rb") as file:
                data = pickle.load(file)
                self.click_count = data['click_count']
                self.multiplier = data['multiplier']
                self.multiplier_cost = data['multiplier_cost']
        except FileNotFoundError:
            self.click_count = 0
            self.multiplier = 1
            self.multiplier_cost = 10

    def save_data(self):
        data = {'click_count': self.click_count, 'multiplier': self.multiplier, 'multiplier_cost': self.multiplier_cost}
        try:
            with open("clicker_data.pkl", "wb") as file:
                pickle.dump(data, file)
        except Exception as e:
            print(f"An error occurred while saving data: {str(e)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerGame(root)
    root.mainloop()