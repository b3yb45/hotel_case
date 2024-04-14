import datetime

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

class BookingApplic:
    def __init__(self, booking_date, last_name, first_name, family_name, people_count, accomod_date, accomod_days, max_spend_per_person):
        self.__booking_date = booking_date
        self.__last_name = last_name
        self.__first_name = first_name
        self.__family_name = family_name
        self.__people_count = people_count
        self.__accomod_date = accomod_date
        self.__accomod_days = accomod_days
        self.__max_spend_per_person = max_spend_per_person
        self.__price_per_person = 0.0

    @property
    def booking_date(self):
        return self.__booking_date

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def family_name(self):
        return self.__family_name

    @property
    def people_count(self):
        return self.__people_count
    
    @people_count.setter
    def people_count(self, value):
        self.__people_count = int(value)

    @property
    def accomod_date(self):
        return self.__accomod_date
    
    @accomod_date.setter
    def accomod_date(self, value):
        self.__accomod_date = datetime.date(value.split(".")[2], value.split(".")[1], value.split(".")[0])

    @property
    def accomod_days(self):
        return self.__accomod_days

    @accomod_days.setter
    def accomod_days(self, value):
        self.__accomod_days = int(value)

    @property
    def max_spend_per_person(self):
        return self.__max_spend_per_person

    @max_spend_per_person.setter
    def max_spend_per_person(self, value):
        self.__max_spend_per_person = int(value)

    @property
    def price_per_person(self):
        return self.__price_per_person

class Hotel:
    __type_price = {
        "одноместный": 2900.00,
        "двухместный": 2300.00,
        "полулюкс": 3200.00,
        "люкс": 4100.00
    }

    __comfort_price_coefficient = {
        "стандарт": 1.0,
        "стандарт_улучшенный": 1.2,
        "апартамент": 1.5
    }

    __catering_price = {
        "без питания": 0.0,
        "завтрак": 280.0,
        "полупансион": 1000.0,
    }

    def __init__(self, apartments_file, booking_file):
        self.__apartmnents = self.__load_apartments(apartments_file)
        self.__booking = self.__load_booking

    @staticmethod
    def __load_apartments(file):
        with open(file) as f:
            return [Apartment(*[int(x) for x in line.split()]) for line in f]
    
    def set_price_per_person(self):
        for apartment in self.__apartmnents:
            apartment.price_per_person = self.__type_price[apartment.type] * self.__comfort_price_coefficient[apartment.comfort]

    @staticmethod
    def booking_input(file):
        with open(file) as f:
            return [BookingApplic(*[x for x in line.split()]) for line in f]

