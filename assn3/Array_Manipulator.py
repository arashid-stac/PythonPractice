import random


class Array_Manipulator:
    """Class for manipulating arrays"""

    integers = []

    def __init__(self):
        for i in range(10):
            self.integers.append(random.randint(0, 50))

    def get_even_indices(self):
        even_indices = []
        for i in range(len(self.integers)):
            if self.integers[i] % 2 == 0:
                even_indices.append(i)

        return even_indices

    def get_even_elements(self):
        even_elements = []
        for el in self.integers:
            if el % 2 == 0:
                even_elements.append(el)

        return even_elements

    def get_first(self):
        return self.integers[0]

    def get_last(self):
        return self.integers[len(self.integers)-1]

    def add_five(self):
        modified_list = self.integers
        for i in range(len(modified_list)):
            modified_list[i] += 5

        return modified_list


a1 = Array_Manipulator()
print(a1.integers)
print(a1.get_even_indices())
print(a1.get_even_elements())
print(a1.add_five())
