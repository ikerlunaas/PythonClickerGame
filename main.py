import tkinter
import tkinter as tk
import random

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.multiplier = 1

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.check_console_label = tk.Label(root, text="Check the console, if there's an error or something to see.")
        self.check_console_label.pack()

        self.click_button = tk.Button(root, text="Click Me!", command=self.click)
        self.click_button.pack()


    def click(self):
        self.score += 1 * self.multiplier

        if self.score >= 20:
            self.multiplier = 2
            print(f'Current multiplier value: {self.multiplier}')

        if self.score >= 40:
            self.multiplier = 3
            print(f'Current multiplier value: {self.multiplier}')

        if self.score >= 60:
            self.multiplier = 5
            print(f'Current multiplier value: {self.multiplier}')

        if self.score >= 100:
            self.multiplier = 9
            print(f'Current multiplier value: {self.multiplier}')

        # Easter egg
        if self.score > 1000:
            self.multiplier = random.randrange(50, 100+1)
            print(f'Current easteregg random multiplier value: {self.multiplier}')

        self.update_score()

    def update_score(self):
        self.score_label.config(text="Score: {}".format(self.score))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clicker Game")

    game = ClickerGame(root)

    root.mainloop()
