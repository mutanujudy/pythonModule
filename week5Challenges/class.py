# Parent Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute to demonstrate encapsulation

    def get_price(self):
        """Getter for the private price attribute."""
        return self.__price

    def set_price(self, new_price):
        """Setter for the private price attribute."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def display_info(self):
        """Display smartphone details."""
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.__price}"

# Child Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)  # Initialize parent class attributes
        self.gpu = gpu  # Additional attribute for GamingSmartphone

    def display_info(self):
        """Override the display_info method for gaming-specific details."""
        return f"Gaming Smartphone: {self.brand} {self.model}, GPU: {self.gpu}, Price: ${self.get_price()}"

# Create instances
phone1 = Smartphone("Apple", "iPhone 14", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1099, "Adreno 730")

# Accessing methods and demonstrating polymorphism
print(phone1.display_info())  # Output: Smartphone: Apple iPhone 14, Price: $999
print(gaming_phone.display_info())  # Output: Gaming Smartphone: Asus ROG Phone 6, GPU: Adreno 730, Price: $1099

# Demonstrating encapsulation
print(phone1.get_price())  
phone1.set_price(899)      
print(phone1.get_price())  
