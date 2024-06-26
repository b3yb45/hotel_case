import datetime
import random
import ru_local as ru

class Apartment:
    '''
    The Apartment class represents an apartment with various attributes such as number, type, capacity, comfort, price per person, and occupation details.

    Attributes:
    ------------
    - __number (str): The number of the apartment.
    - __type (str): The type of the apartment.
    - __capacity (int): The capacity of the apartment.
    - __comfort (str): The comfort level of the apartment.
    - __price_per_person (float): The price per person for the apartment.
    - price_with_catering (dict): A dictionary to store prices with catering options.
    - occupied_set (set): A set to store occupied apartments.

    Properties:
    ------------
    - number: Getter for the apartment number.
    - type: Getter for the apartment type.
    - capacity: Getter for the apartment capacity.
    - comfort: Getter for the apartment comfort level.
    - price_per_person: Getter and setter for the price per person.
    '''

    def __init__(self, number, type, capacity, comfort):
        self.__number = number
        self.__type = type
        self.__capacity = int(capacity)
        self.__comfort = comfort
        self.__price_per_person = 0.0
        self.price_with_catering = {}
        self.occupied_set = set()
    
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
    
    def __repr__(self) -> str:
        return '№' + ' '.join([self.number, str(self.capacity), self.comfort, self.type])

class BookingApplic:
    '''
    The BookingApplic class represents a booking application with attributes related to booking details such as booking date, last name, first name, family name, number of people, accommodation date, accommodation days, maximum spend per person, and price per person.

    Attributes:
    ------------
    - __booking_date (str): The date of the booking.
    - __last_name (str): The last name of the person making the booking.
    - __first_name (str): The first name of the person making the booking.
    - __family_name (str): The family name of the person making the booking.
    - __people_count (int): The number of people in the booking.
    - __accomod_date (list): The date of accommodation split into day, month, and year.
    - __accomod_days (int): The number of days for accommodation.
    - __max_spend_per_person (int): The maximum spend allowed per person.
    - __price_per_person (float): The price per person for the booking.

    Properties:
    ------------
    - booking_date: Getter for the booking date.
    - last_name: Getter for the last name.
    - first_name: Getter for the first name.
    - family_name: Getter for the family name.
    - people_count: Getter and setter for the number of people.
    - accomod_date: Getter and setter for the accommodation date.
    - accomod_days: Getter and setter for the number of accommodation days.
    - max_spend_per_person: Getter and setter for the maximum spend per person.
    - price_per_person: Getter for the price per person.
    '''

    def __init__(self, booking_date, last_name, first_name, family_name, people_count, accomod_date, accomod_days, max_spend_per_person):
        self.__last_name = last_name
        self.__booking_date = booking_date
        self.__first_name = first_name
        self.__family_name = family_name
        self.__people_count = int(people_count)
        self.__accomod_date = []
        self.__accomod_days = int(accomod_days)
        self.__max_spend_per_person = int(max_spend_per_person)
        self.__price_per_person = 0.0

        for elem in accomod_date.split('.'):
            self.__accomod_date.append(int(elem))

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

    def __str__(self):
        accom_date = '.'.join([f'{x:02d}' for x in self.accomod_date])
        return self.booking_date + ' ' +  self.last_name + ' ' + self.first_name + ' ' + self.family_name + ' ' + \
            accom_date

class Hotel:
    '''
    The Hotel class represents a hotel with attributes and methods related to managing hotel apartments and bookings.

    Attributes:
    ------------
    - __type_price (dict): A dictionary mapping apartment types to their base prices.
    - __comfort_price_coefficient (dict): A dictionary mapping comfort levels to price coefficients.
    - __catering_price (dict): A dictionary mapping catering options to their prices.

    Methods:
    ---------
    - load_apartments(file): Static method to load apartment data from a file and return a list of Apartment objects.
    - calculate_price(booking: BookingApplic): Calculates the price for a booking based on available apartments and booking details.

    Properties:
    ------------
    - apartments: Getter for the list of apartments in the hotel.
    '''

    __type_price = {
        ru.lux: 4100.00,
        ru.semilux: 3200.00,
        ru.double: 2300.00, 
        ru.single: 2900.00
    }

    __comfort_price_coefficient = {
        ru.apart: 1.5,
        ru.std_improved: 1.2,
        ru.std: 1.0
    }

    __catering_price = {
        ru.half_board: 1000.0,
        ru.breakfast: 280.0,
        ru.no_catering: 0.0
    }

    def __init__(self, apartments_file):
        self.__apartments = self.load_apartments(apartments_file)
        self.total_profit = 0
        self.loss_profit = 0
        self.free_aparts = len(self.__apartments)
        self.apart_hier = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}
        
        for capacity in self.apart_hier:
            for key_type in Hotel.__type_price:
                for key_comfort in Hotel.__comfort_price_coefficient:
                    result_key = key_type + ' ' + key_comfort
                    self.apart_hier[capacity][result_key] = []
        
        for apart in self.__apartments:
            apart_type = apart.type + ' ' + apart.comfort
            self.apart_hier[apart.capacity][apart_type].append(apart)
        
        for key in self.apart_hier.copy():
            for apart_type in self.apart_hier[key].copy():
                if self.apart_hier[key][apart_type] == []:
                    del self.apart_hier[key][apart_type]
        
        for apartment in self.__apartments:
            apartment.price_per_person = self.__type_price[apartment.type] * self.__comfort_price_coefficient[apartment.comfort]

            for catering in Hotel.__catering_price:
                apartment.price_with_catering[catering] = apartment.price_per_person + Hotel.__catering_price[catering]

    @property
    def apartments(self):
        return self.__apartments
    
    @property
    def types(self):
        return list(self.__type_price.keys())
    
    @staticmethod
    def load_apartments(file):
        with open(file, encoding='utf-8') as f:
            return [Apartment(*[x for x in line.split()]) for line in f]


    def calculate_price(self, booking: BookingApplic):
        '''
        Calculates the price for a booking based on available apartments and booking details.
        '''

        discount = False
        disc_coef = 0.3
        booking_period = []
        success = False
        refuse = False

        for i in range(1, booking.accomod_days + 1):
            date = datetime.date(year=booking.accomod_date[-1], month=booking.accomod_date[-2], \
                                 day=booking.accomod_date[-3]) + datetime.timedelta(days=i)

            result_date = f'{date.day:02d}.{date.month:02d}.{date.year}'
            booking_period.append(result_date)
        capacity = booking.people_count

        while (not success) and capacity < 7 and (not refuse):
            if capacity != booking.people_count:
                discount = True

            for apart_type in self.apart_hier[capacity]:
                for apart in self.apart_hier[capacity][apart_type]: 
                    if apart.price_per_person * (1 - disc_coef*discount) <= booking.max_spend_per_person and \
                        set(booking_period).intersection(apart.occupied_set) == set() and (not refuse) and (not success):
    
                        for catering in apart.price_with_catering:
                            if apart.price_with_catering[catering] * (1 - disc_coef*discount) <= booking.max_spend_per_person:
                                offer_price = apart.price_with_catering[catering]
                                answer = random.choice([0, 1, 2, 3])

                                if answer != 0:
                                    self.total_profit += offer_price * booking.accomod_days * booking.people_count
                                    for x in booking_period:
                                        apart.occupied_set.add(x)
                                    success = True
                                    msg = f'{booking} {ru.booked} {apart} {ru.with_catering} {catering}. {ru.price}: {offer_price * booking.accomod_days * booking.people_count}'
                                    print(msg)
                                else:
                                    refuse = True
                                    self.loss_profit += offer_price * booking.accomod_days * booking.people_count
                                    print(f'{ru.client} {booking.last_name} {booking.first_name} {booking.family_name} {ru.offer_reject}. {ru.lost_rvn}: {offer_price * booking.accomod_days * booking.people_count}')
                                break  
            capacity += 1          

        if (not success) and (not refuse):
            self.loss_profit += booking.max_spend_per_person
            print(f'{ru.check_in_fail} {booking.last_name} {booking.first_name} {booking.family_name}. {ru.lost_rvn}: {booking.max_spend_per_person * booking.accomod_days * booking.people_count}')

class Model:
    '''
    The Model class represents a model for managing hotel bookings and calculating daily profits and losses.

    Attributes:
    -----------
    - daily_profit (float): The daily profit earned by the hotel.
    - daily_loss_profit (float): The daily loss in profit for the hotel.
    - hotel (Hotel): The Hotel object associated with the model.
    - start_date (str): The start date for the model.

    Methods:
    --------
    - load_booking(file): Static method to load booking data from a file and return a list of BookingApplic objects.
    - start(self, booking_file): Method to start the model processing by loading bookings, 
    calculating daily profits and losses, and displaying results.
    '''

    def __init__(self, hotel: Hotel, start_date):
        self.daily_profit = 0
        self.daily_loss_profit = 0
        self.hotel = hotel
        self.start_date = start_date

    @staticmethod
    def load_booking(file):
        with open(file, encoding='utf-8') as f:
            return [BookingApplic(*[x for x in line.split()]) for line in f]
    
    def start(self, booking_file):
        '''
        Method to start the model processing by loading bookings, 
        calculating daily profits and losses, and displaying results.
        '''

        bookings_list = Model.load_booking(booking_file)
        date_lst = []
        
        for i in range(32):
            date = datetime.date(year=int(self.start_date.split('.')[-1]), month=int(self.start_date.split('.')[-2]), \
                                 day=int(self.start_date.split('.')[-3])) + datetime.timedelta(days=i)
            
            result_date = f'{date.day:02d}.{date.month:02d}.{date.year}'
            date_lst.append(result_date)

        yest_profit = 0
        yest_loss = 0

        for date in date_lst:
            print(f"------------------------------------------------------------------------------{date}------------------------------------------------------")
            daily_bookings = filter(lambda x: x.booking_date == date, bookings_list) 

            for booking in daily_bookings:
                self.hotel.calculate_price(booking)
                print()

            self.daily_profit = self.hotel.total_profit - yest_profit
            yest_profit = self.hotel.total_profit
            self.daily_loss_profit = self.hotel.loss_profit - yest_loss
            yest_loss = self.hotel.loss_profit
            print('')
            print(f'{ru.daily_rvn}:', self.daily_profit)
            print(f'{ru.daily_lost_rvn}:', self.daily_loss_profit)
            
            occupations = 0
            occup_dict = dict.fromkeys(self.hotel.types, 0)

            for apart in self.hotel.apartments:
                if date in apart.occupied_set:
                    occupations += 1
                    if apart.type in occup_dict:
                        occup_dict[apart.type] += 1
            
            for apart_type in occup_dict:
                occup_dict[apart_type] = round(occup_dict[apart_type] / len(list(apart for apart in self.hotel.apartments if apart.type == apart_type)), 2) * 100
            
            print(f'{ru.occup_apart}:', occupations)
            print(f'{ru.vacant_apart}:', len(self.hotel.apartments) - occupations)
            print(f'{ru.occup_percent}:', round(occupations / len(self.hotel.apartments), 2) * 100, '%')
            print(f'{ru.occup_type_percent}:', end = '')
            for apart_type in occup_dict:
                print(f'{apart_type}: {occup_dict[apart_type]}%; ', end = '')
            print('\n')

        print(f'{ru.total_rvn}:', self.hotel.total_profit)
        print(f'{ru.total_lost_rvn}:', self.hotel.loss_profit)
