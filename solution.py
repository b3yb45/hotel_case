class Apartment():
    def __init__(self, number, type, capacity, comfort):
        self.__number = number
        self.__type = type
        self.__capacity = capacity
        self.__comfort = comfort
        self.__price_per_person = 0.0

    @property
    def number(self):
        return self.__number

    @property
    def type(self):
        return self.__type

    @property
    def capacity(self):
        return self.__capacity

    @property
    def comfort(self):
        return self.__comfort
    
    @property
    def price_per_person(self):
        return self.__price_per_person

    @price_per_person.setter
    def price_per_person(self, value):
        self.__price_per_person = value

class Hotel(Apartment):
    __type_price_per_person = {
        "одноместный": 2900.00,
        "двухместный": 2300.00,
        "полулюкс": 3200.00,
        "люкс": 4100.00
    }

    def __init__(self, apartments_file):
        self.__apartmnents = self.__load_apartments(apartments_file)

    @staticmethod
    def __load_apartments(file):
        with open(file) as f:
            return [Apartment(*[int(x) for x in line.split()]) for line in f]
    
    def set_price_per_person(self):
        for apartment in self.__apartmnents:
            apartment.price_per_person = self.__type_price_per_person[apartment.type]