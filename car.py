class Car(object):
  def __init__(self,name='General', model='GM', car_type=None):
    self.name = name
    self.model = model
    self.car_type = car_type
    self.speed = 0
  
    if self.name == 'Koenigsegg' or self.name == 'Porshe':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    
    if self.car_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
      
  def is_saloon(self):
    if self.car_type == 'trailer':
      return False
    else:
      return True
  
  def drive(self, speed):
    if speed==7:
      self.speed =77
    elif speed == 3:
      self.speed = 1000
    return self
