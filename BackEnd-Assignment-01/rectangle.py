class Rectangle:
    
   def __init__(self, length, breadth):   
       self.length = length
       self.breadth = breadth
       
   
   def calculate_area(self):
       self.area_of_rectangle =   (self.length * self.breadth)
       return ('{}'.format(self.area_of_rectangle))
       
   def calculate_perimeter(self):
       self.perimeter_of_rectangle = (2 * (self.length + self.breadth))
       return ('{}'.format(self.perimeter_of_rectangle))
      
if __name__ == "__main__":  
   rectangle_one = Rectangle(5, 5) 
   print("area of rectangle is ", rectangle_one.calculate_area()) 
   print("perimeter of rectangle is ",  rectangle_one.calculate_perimeter())  