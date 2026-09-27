# Topic: Instance Methods and Class Attributes
# Advanced Back-End Development - Lecture 2

class Phone:
    # Class attribute: Shared by all instances of this class
    device_type = "Smartphone"
    total_phones = 0

    def __init__(self, brand, model, storage_gb, price):
        # Instance attributes: Unique to each object
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.price = price
        Phone.total_phones += 1

    # Instance method: Operates on instance attributes and can access class attributes
    def full_specs(self):
        print(f"Device: {self.device_type} | Brand: {self.brand} | Model: {self.model} | Storage: {self.storage_gb} GB | Price: Rs. {self.price}")

    # Instance method: Modifies instance state
    def apply_discount(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price -= discount_amount
        print(f"Applied {discount_percent}% discount on {self.brand} {self.model}. New Price: Rs. {self.price}")


if __name__ == '__main__':
    print("--- Phone Specifications ---")
    phone1 = Phone("Samsung", "Galaxy S24", 256, 280000)
    phone2 = Phone("Apple", "iPhone 15", 128, 320000)
    phone3 = Phone("Xiaomi", "Redmi Note 13", 128, 55000)

    phone1.full_specs()
    phone2.full_specs()
    phone3.full_specs()

    print(f"\nTotal phones created: {Phone.total_phones}")

    print("\n--- Applying Discount ---")
    phone1.apply_discount(10)
    phone1.full_specs()
