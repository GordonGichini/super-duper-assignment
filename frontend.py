import tkinter as tk
from tkinter import messagebox
from backend import Smartphone

class SmartphoneGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Smartphone GUI")

        self.phone = Smartphone(512) 

        self.create_widgets()
        self.update_display()

        self.window.mainloop()

    def create_widgets(self):
        # Smartphone Section
        tk.Label(self.window, text="BnL Smartphone").pack()

        self.battery_label = tk.Label(self.window)
        self.battery_label.pack()

        self.storage_label = tk.Label(self.window)
        self.storage_label.pack()


        tk.Button(self.window, text="Toggle Battery Saver Mode", command=self.toggle_battery_saver).pack()
        tk.Button(self.window, text="Charge Battery", command=self.charge_battery).pack()

        # Photos App Section
        tk.Label(self.window, text="\nPhotos App").pack()

        tk.Button(self.window, text="Take Photo", command=self.take_photo).pack()
        tk.Button(self.window, text="Delete Photo", command=self.delete_photo).pack()

        # Pictagram App Section
        tk.Label(self.window, text="\nPictagram App").pack()

        tk.Button(self.window, text="Create Post", command=self.open_create_post_window).pack()
        tk.Button(self.window, text="Delete Post", command=self.delete_post).pack()

        

    def update_display(self):
        if self.phone.battery_saver_mode:
            mode = "Enabled"
        else:
            mode = "Disabled"

        self.battery_label.config(
            text=f"Battery: {self.phone.battery}% ({mode})"
        )

        self.storage_label.config(
            text=f"Storage Left: {self.phone.get_storage_left():.2f}GB"
        )

    def toggle_battery_saver(self):
        self.phone.battery_saver_mode = not self.phone.battery_saver_mode
        self.update_display()

    def charge_battery(self):
        self.phone.charge_battery()
        self.update_display()

    def take_photo(self):
        try: 
            self.phone.take_photo()
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_photo(self):
        try:
            self.phone.delete_photo()
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_create_post_window(self):
        window = tk.Toplevel(self.window)
        window.title("Create Post")

        entry = tk.Entry(window)
        entry.pack()

        def submit():
            try:
                caption = entry.get()
                self.phone.create_post(caption)
                self.update_display()
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(window, text="Post", command=submit).pack()

    def delete_post(self):
            try:
                self.phone.delete_post()
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    SmartphoneGUI()