class Car:
    def __init__(self, in_color,car_type, car_acc):
        #print('GVK')
        self.color = in_color
        self.accleration = car_acc
        self.type = car_type
        self.current_speed = 100
        self.decelerate = 15
    def accelerate(self):
        self.current_speed += self.accleration
  
    def brake(self):
        if self.current_speed>15:
            self.current_speed -= self.decelerate
        elif self.current_speed<15:
            self.current_speed = 0