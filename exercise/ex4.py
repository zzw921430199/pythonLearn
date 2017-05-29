
cars = 100
sapce_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpoo_capacity = cars_driven * sapce_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpoo_capacity, "people today")
print("We have", passengers, "to carpoll today")
print("We need to put about", average_passengers_per_car, "in which car")

