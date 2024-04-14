class Apartment():
    def __init__(self, number, type, capacity, comfort):
        self.__number = number
        self.__type = type
        self.__capacity = capacity
        self.__comfort = comfort

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


class Hotel(Apartment):
    def __init__(self, apartments_file):
        self.__apartmnents = self.__load_apartments(apartments_file)

    @staticmethod
    def __load_apartments(file):
        with open(file) as f:
            return [Apartment(*[int(x) for x in line.split()]) for line in f]