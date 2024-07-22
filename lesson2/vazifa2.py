class Phone:
    def __init__(self, model, ram, price, color) -> None:
        self.model = model
        self.ram = ram
        self.price = price
        self.color = color

    def user_info(self):
        print(f"model: {self.model} \nram: {self.ram} \nnarxi:{self.price} \nrangi: {self.price}")
        

phone1 = Phone("Samsung Galaxy S24", "8GB", 999, "Black")
phone2 = Phone("iPhone 11", "4GB", 699, "White")
phone3 = Phone("Google Pixel 5", "6GB", 799, "Just Black")

phone1.user_info()
phone2.user_info()
phone3.user_info()
