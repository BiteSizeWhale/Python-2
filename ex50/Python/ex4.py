#tells how many cars are aviable
cars = 100
#Tells how many people will fit in each car
space_in_a_car = 4.0
#Tells how many drivers are aviable
drivers = 30
#Tells how many passengers are there
passengers = float(90)
#Dives the number of cars are not being driven by subcracting the total number of drivers from the total number of cars
cars_not_driven = float(cars - drivers)
#Tells how many cars are being driven by having it equal the variable drives which seems repetative
cars_driven = drivers
#Adss the number of driver and the space in each car to get how many people can be driven today
carpool_capacity = cars_driven * space_in_a_car
#Dives the number of passengers by the number of cars driven, or 3=90/30
average_passengers_per_car = passengers / cars_driven



print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."