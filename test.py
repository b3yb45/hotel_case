from solution import Hotel, Model

hotel = Hotel('fund.txt')
model = Model(hotel)
model.start('booking.txt')