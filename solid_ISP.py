"""Interface Segregation Principle:you don't want to stick many elements to many methods it might be a good idea to define a single interface and let it be implemented whatever it's needed """
# bad way
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass
# solution


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class My_printer(Printer):
    def print(self, document):
        print(document)


class My_Photocoper(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print(document)
