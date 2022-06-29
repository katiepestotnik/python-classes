# OOP with python
# inheritance - parent/child relationship an object can inherit all of the properties of the parent element

# encapsulation - when an object keeps it's state private like scoping or variables only accessable in function 

# polymorphism - change functionality of parent's properties to adjust for the child

# abstraction - each object only exposes high level mechanism. functionality is under the hood, user(coder) only sees what is needed not all of the code like sorted()

# __init__ == magic method 


nums = [1, 2, 3, 8, 2, 4, 0]
# print all of the properties of list object
#print(dir(nums))

# dog class
class Dog():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    #overwrite str method
    def __str__(self):
        return f'My dog is {self.name} and is {self.age} years old'
    
    def bark(self):
        print(f'{self.name} barked woof woof')

#instantiate dog in python
#create object from class
missy = Dog('Missy', 5)
# printing missy returns dog object with location
# instance of dog is missy with no __str__ method
#with __str__method it will show init values
print(missy)
print(missy.name)
missy.bark()

class Vehicle():
    def __init__(self, vin, make, model, running = False):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = running
    def __str__(self):
        return f'''
        This vehicle is a:
        {self.make}
        Vin is:
        {self.vin}
        Model is:
        {self.model}
        Running?
        {self.running}
    '''
    def start(self):
        self.running = True
    def stop(self):
        self.running = False

car = Vehicle(12345, 'Toyota', 'Highlander')

car.start()
print(car)
car.stop()
print(car)