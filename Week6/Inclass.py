class Smartphone:
    price = 20000000
    weight = 0.2

    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color

    def print_information(self):
        # print(f"Name of smartphone: {self.name}")
        # print(f"Color of smartphone: {self.color}")
        print(f"Price of smartphone: {self.price}")
        print(f"Weight of smartphone: {self.weight}")

    @staticmethod
    def print_weight(weight):
        print(f"Weight of smartphone: {weight}")

    def get_price(self):
        print(f"Price of smartphone: {self.price}")

    @classmethod
    def increase_weight(cls):
        cls.weight += 0.1


# NewSmartphone = Smartphone("Iphone 17", "blue")
# NewSmartphone.print_information()
# OldSmartphone = Smartphone("Iphone 17", "red")
# OldSmartphone.print_information()
#
# Smartphone.price = 20
print(Smartphone.price)

# Smartphone.print_weight(2)
# smartphone = Smartphone()
# smartphone.print_weight(8)

new_smartphone = Smartphone()
old_smartphone = Smartphone()
old_smartphone.increase_weight()
new_smartphone.print_information()
Smartphone.increase_weight()
old_smartphone.print_information()
print(Smartphone.weight)
