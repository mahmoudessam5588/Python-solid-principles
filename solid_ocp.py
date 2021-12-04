"""open close principles: when you add new functionality you add it by extension not by modification"""
from enum import Enum


class Color (Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size (Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.size = size
        self.color = color


class product_filter:
    # #     #ocp = open for extension closed by modification
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

# #     #add new functionality filter by size (ocp violation) doesn't scale well if we add more functionality like filter by color and / or size etc
    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product
# #     #solution u make 2 classes specification class and filter class
# #     #where specification class is a base class meant to be overridden


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return And_Specification(self, other)
# filter class where we add items we want to filter and specification related of the class above


class Filter:
    def filter(self, items, spec):
        pass
# the idea to inherit from these classes and extend functionality
# for example we have color specification


class Color_Specification(Specification):
    # we initialize color by constructor
    def __init__(self, color):
        self.color = color

    # we override the method to check if it satisfy the condition by returning it
    def is_satisfied(self, item):
        return item.color == self.color
    # similarly we do the same with size specification


class Size_Specification(Specification, Filter):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class And_Specification(Filter, Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class Better_Filter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
