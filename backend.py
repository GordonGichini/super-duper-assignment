class Smartphone:
    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity
        self.battery = 100
        self.battery_saver_mode = False 

    def use_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0 

    def charge_battery(self):
        if self.battery_saver_mode:
            self.battery = 80
        else:
            self.battery = 100

    def __str__(self):
        if self.battery_saver_mode:
            mode = "Enabled"
        else:
            mode = "Disabled"

        return f"BnL Smartphone - Storage: {self.storage_capacity}GB, Battery: {self.battery}%, Battery Saver Mode: {mode}"
    

def test_smartphone():
    phone = Smartphone(512)
    phone.use_battery(30)
    print(phone)

    phone.battery_saver_mode = True
    phone.use_battery(30)
    print(phone)

    phone.battery_saver_mode = True
    phone.charge_battery()
    print(phone)


if __name__ == "__main__":
    test_smartphone()

    
    