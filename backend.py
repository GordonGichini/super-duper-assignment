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

class PhotosApp:
    def __init__(self):
        self.number_of_photos = 0

    def take_photo(self):
        self.number_of_photos += 1
        print("Photo taken!")

    def delete_photo(self):
        if self.number_of_photos > 0:
            self.number_of_photos -= 1
            print("Photo deleted!")

    def calculate_storage_used(self):
        total_mb = self.number_of_photos * 24
        total_gb = total_mb / 1024
        return total_gb 
    
    def __str__(self):
        storage = self.calculate_storage_used()
        return f"Photos App - Photos: {self.number_of_photos}, Storage Used: {storage:.2f}GB"
    
def test_photos_app():
    app = PhotosApp()

    # Take 5 photos
    for i in range(5):
        app.take_photo()

    print(app)

    # Delete 2 photos
    for i in range(1):
        app.delete_photo()

    print(app)


class PictagramApp:
    def __init__(self):
        self.posts = []

    def create_post(self, caption):
        self.posts.append(caption)
        print("Post created!")

    def delete_post(self):
        if len(self.posts) > 0:
            self.posts.pop()
            print("Post deleted!")

    def calculate_storage_used(self):
        total_mb = len(self.posts) * 15
        total_gb = total_mb / 1024
        return total_gb   
    
    def __str__(self):
        storage = self.calculate_storage_used()
        return f"Pictagram App - Posts: {len(self.posts)}, Storage Used: {storage:.2f}GB"
    
def test_pictagram_app():
        app = PictagramApp()

        # Create posts
        app.create_post(" My Uno Post!")
        app.create_post(" Having Fun with my Dos post!")
        app.create_post(" Tres is the best post!")

        # Print storage used
        print("Storage used:", app.calculate_storage_used(), "GB")
        print(app)

        app.delete_post()

        print(app)


if __name__ == "__main__":
    test_smartphone()
    test_photos_app()
    test_pictagram_app()

    