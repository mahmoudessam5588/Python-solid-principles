from persistance_manager_SRP_1 import Persistance_Manager
from solid_DIP import *
from solid_lsp import Rectangle, Square, use_it
from solid_ocp import *
from solid_SRP_0 import Journal


def main(args):
    Journal_func_call()
    ocp_call()
    lsp_call()
    Person
    parent = Person('John')
    child1 = Person('matt')
    child2 = Person('leroy')
    Relationships
    relate = Relationships()
    relate.add_parent_child(parent,child1)
    relate.add_parent_child(parent,child2)
    Research(relate)
    return 0

def lsp_call():
    Rectangle
    rc = Rectangle(2, 3)
    use_it(rc)
    Square
    square = Square(5)
    use_it(square)


def ocp_call():
    Product
    apple = Product("APPLE", Color.GREEN, Size.SMALL)
    tree = Product("TREE", Color.GREEN, Size.LARGE)
    house = Product("HOUSE", Color.RED, Size.MEDIUM)
    products = [apple, tree, house]
    Better_Filter
    better_filter = Better_Filter()
    Color_Specification
    green = Color_Specification(Color.GREEN)
    for p in better_filter.filter(products, green):
        print(p.name)
    print('-------------')
    large = Size_Specification(Size.LARGE)
    for i in better_filter.filter(products, large):
        print(i.name)
    print('--------')

    large_green = large & Color_Specification(Color.GREEN)
    for p in better_filter.filter(products, large_green):
        print(p.name)


def Journal_func_call():
    Journal
    j = Journal([])
    j.add_entry('I CRIED TODAY')
    j.add_entry('I ATE BUG')
    print(f'journal entries :\n{j}')
    file = r'./journal.txt'
    Persistance_Manager.save_to_file(j, file)
    with open(file) as fh:
        print(fh.read())


if __name__ == '__main__':
    import sys
    main(sys.argv)
