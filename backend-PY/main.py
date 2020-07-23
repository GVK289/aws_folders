from car import Car

car_1 = Car("Green", "Automated Car",100)
car_2 = Car("Red", "Automated Car", 100)

car_1.accelerate()
car_2.accelerate()

print(car_1.color,car_1.type,car_1.current_speed)
print(car_2.color,car_2.type,car_2.current_speed)

 
print()
car_2.current_speed = 14
car_2.brake()

print(car_1.color,car_1.type,car_1.current_speed)
print(car_2.color,car_2.type,car_2.current_speed)
print()

