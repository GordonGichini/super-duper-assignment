import tkinter as tk

class SmartphoneGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Smartphone GUI")

        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        # Smartphone Section
        tk.Label(self.window, text="BnL Smartphone").pack()

        tk.Label(self.window, text="Storage Capacity: 512GB").pack()
        tk.Label(self.window, text="Battery: 75%").pack()
        tk.Label(self.window, text="Battery Saver Mode: Disabled").pack()
        tk.Label(self.window, text="Storage Left: 510.80GB").pack()

        tk.Button(self.window, text="Toggle Battery Saver Mode").pack()
        tk.Button(self.window, text="Charge Battery").pack()

        # Photos App Section
        tk.Label(self.window, text="Photos App").pack()

        tk.Label(self.window, text="Number of Photos: 42").pack()
        tk.Label(self.window, text="Storage Used: 0.98GB").pack()

        tk.Button(self.window, text="Take Photo").pack()
        tk.Button(self.window, text="Delete Photo").pack()

        # Pictagram App Section
        tk.Label(self.window, text="\nPictagram App").pack()

        tk.Label(self.window, text="Number of Posts: 15").pack()
        tk.Label(self.window, text="Storage Used: 0.22GB").pack()

        tk.Entry(self.window).pack()
        tk.Button(self.window, text="Create Post").pack()

        tk.Entry(self.window).pack()
        tk.Button(self.window, text="Delete Post").pack()


if __name__ == "__main__":
    SmartphoneGUI()