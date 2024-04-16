from solution import Hotel, Model

hotel = Hotel('fund.txt')
model = Model(hotel, '01.03.2020')
model.start('booking.txt')