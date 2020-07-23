class  Bike:
	def  __init__(self, model_name, acceleration):
		self.model_name = model_name
		self.acceleration = acceleration
		self.current_speed =  0
		self.color =  "black"
	
	def  accelerate(self):
		self.current_speed += self.acceleration


def create_bike_object(model_name, acceleration):
	bike_object = Bike(model_name,acceleration)
	return  bike_object  #"To fill create_bike_object code" # Change this
	
def get_bike_object_color(bike_object):
	return  bike_object.color # Change this

def get_bike_object_current_speed(bike_object):
	return  bike_object.current_speed #"To fill get_bike_object_current_speed code"

def change_bike_color(bike_object, new_color):
	bike_object.color = new_color
	return bike_object.color  #"To fill change_bike_color code" # Change this

def increase_bike_speed(bike_object):
	return bike_object.accelerate()  #"To fill increase_bike_speed code" # Change this


if  __name__  ==  '__main__':
	bike_object =  create_bike_object('Yamaha', 10)
	print(bike_object)
	print(get_bike_object_color(bike_object))
	print(get_bike_object_current_speed(bike_object))
	print(change_bike_color(bike_object, "red"))
	(increase_bike_speed(bike_object))
	print(get_bike_object_current_speed(bike_object))   