import datetime

class Apartment():
    def __init__(self, number, type, capacity, comfort):
        self.__number = number
        self.__type = type
        self.__capacity = capacity
        self.__comfort = comfort
        self.__price_per_person = 0.0
        self.__price_with_catering = {}
        self.__occupied = False
        self.__occupation_start = None
        self.__occupation_end = None

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

    @property
    def occupied(self):
        return self.__occupied
    
    @occupied.setter
    def occupied(self, value):
        if not isinstance(value, bool):
            raise ValueError("Occupied must be a boolean value")
        self.__occupied = value

    @property
    def occupation_start(self):
        return self.__occupation_start
    
    @occupation_start.setter
    def occupation_start(self, value):
        self.__occupation_start = datetime.date(value.split(".")[2], value.split(".")[1], value.split(".")[0])

    @property
    def occupation_end(self):
        return self.__occupation_end
    
    @occupation_end.setter
    def occupation_end(self, value):
        self.__occupation_end = datetime.date(value.split(".")[2], value.split(".")[1], value.split(".")[0])
    
    def __repr__(self) -> str:
        return ' '.join([self.number, self.capacity, self.comfort, self.type])

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
        self.__apartmnents = self.load_apartments(apartments_file)
        self.__booking = self.load_booking(booking_file)

        self.apart_hier = {}
        
        for key_type in Hotel.__type_price:
            for key_comfort in Hotel.__comfort_price_coefficient:
                result_key = key_type + ' ' + key_comfort
                self.apart_hier[result_key] = []
        
        for apart in self.__apartmnents:
            apart_type = apart.type + ' ' + apart.comfort
            self.apart_hier[apart_type].append(apart)
        
        for key in self.apart_hier.copy():
            if self.apart_hier[key] == []:
                del self.apart_hier[key]

    @property
    def apartments(self):
        return self.__apartmnents
    
    @staticmethod
    def load_apartments(file):
        with open(file, encoding='utf-8') as f:
            return [Apartment(*[x for x in line.split()]) for line in f]
    
    def set_price_per_person(self):
        for apartment in self.__apartmnents:
            apartment.__price_per_person = self.__type_price[apartment.type] * self.__comfort_price_coefficient[apartment.comfort]

            for catering in Hotel.__catering_price:
                apartment.__price_with_catering[catering] = apartment.price_per_person + Hotel.__catering_price[catering]

    @staticmethod
    def load_booking(file):
        with open(file, encoding='utf-8') as f:
            return [BookingApplic(*[x for x in line.split()]) for line in f]
    '''
    def calculate_price(self):
    '''  
    
