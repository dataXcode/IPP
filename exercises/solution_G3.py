# define the Vehicle class
class Vehicle:
    
  def __init__(self, name, color, price):
    self.name = name
    self.color = color
    self.price = price
        
  def description(self):
    return 'Car name: {} Color: {} Price: {}'.format(self.name, self.color, self.price)

# Create car1 object and print out the description
car1 = Vehicle('BMW', 'Red', 40000)
print(car1.description())

# Create car2 object and print out the description
car2 = Vehicle('Mercedes', 'White', 50000)
print(car2.description())
