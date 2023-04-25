class Part:
    """Part class for the APO"""

    def __init__(self, description, code, price):
        self.description = description
        self.code = code
        self.price = price

    def get_description(self):
        return self.description

    def get_code(self):
        return self.code

    def get_price(self):
        return self.price

    def __str__(self):
        return "Part {}: {} ${}".format(self.get_code(), self.get_description(), self.get_price())


p = Part("d", "c", 1.0)
print(p)