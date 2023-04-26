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


class Order:
    """Order class for APO"""
    unique_id = 0

    def __init__(self):
        self.unique_id = Order.unique_id
        Order.unique_id += 1
        self.part_list = []

    def add_part(self, part):
        self.part_list.append(part)

    def get_total(self):
        cost = 0.0
        for part in self.part_list:
            cost += part.get_price()

        return cost

    def sort(self):
        sorted_list = sorted(self.part_list, key=lambda x: x.price, reverse=True)
        return sorted_list

    def print_order(self):
        sorted_list = self.sort()
        print("Order {}: {} parts - total: ${}\n".format(self.unique_id, len(self.part_list), self.get_total()))
        for part in sorted_list:
            print(part)
        print("\n")


p1 = Part("QS Board", "LPC1343", 15.0)
p2 = Part("QSB Base Board", "LPC4088", 30.0)
order1 = Order()
order1.add_part(p1)
order1.add_part(p2)
order1.print_order()

order2 = Order()
order2.add_part(p2)
order2.add_part(p1)
order2.add_part(p2)
order2.print_order()
