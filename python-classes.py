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
    # class attribute - creates an id for each instance of Dog()
    next_id = 1
    #instance attributes
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        # class attribute access next_id
        self.id = Dog.next_id
        # when init is run/ id will increment by 1
        Dog.next_id += 1 
    #overwrite str method
    def __str__(self):
        return f'My dog is {self.name} and is {self.age} years old with id# of: {self.id}'
    
    # class methods
    #decorator label tells Dog class only called on Dog
    # use class attribute next_id
    @classmethod
    def get_total_dogs(cls):
        return cls.next_id - 1
        
    # instance methods
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
# check id increment with new instance
klondike = Dog('Klondike', 5)
print(klondike)

# check total dogs
print(f'Total Dogs = {Dog.get_total_dogs()}')

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

