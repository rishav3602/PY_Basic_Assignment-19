"""

1. Make a class called Thing with no contents and print it. Then, create an object called example
from this class and also print it. Are the printed values the same or different?


ANS-To make a class called Thing with no contents, you can simply use the following code:

class Thing:
    pass

print(Thing()) # prints: <__main__.Thing object at 0x7fb2a1a9ae20>

example = Thing()
print(example) # prints: <__main__.Thing object at 0x7fb2a1a9ae80>

--------------------------------------------------------------------------------------------------------------------

2. Create a new class called Thing2 and add the value &#39;abc&#39; to the letters class attribute. Letters
should be printed.

ANSWER..

To create a new class called Thing2 and add the value 'abc' to the letters class attribute, you can use the following code:

class Thing2:
    letters = 'abc'

print(Thing2.letters) # prints: abc

--------------------------------------------------------------------------------------------------------------------

3. Make yet another class called, of course, Thing3. This time, assign the value &#39;xyz&#39; to an instance
(object) attribute called letters. Print letters. Do you need to make an object from the class to do
this?

ANSWER

To make yet another class called Thing3, assign the value 'xyz' to an instance (object) attribute called letters, and print letters without making an object from the class, you can use the following code:

class Thing3:
    def __init__(self):
        self.letters = 'xyz'

print(Thing3().letters) # prints: xyz

---------------------------------------------------------------------------------------------------------------------

4. Create an Element class with the instance attributes name, symbol, and number. Create a class
object with the values &#39;Hydrogen,&#39; &#39;H,&#39; and 1.

ANSWER..

To create an Element class with the instance attributes name, symbol, and number and create a class object with the values 'Hydrogen,' 'H,' and 1, you can use the following code:

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element('Hydrogen', 'H', 1)


---------------------------------------------------------------------------------------------------------------------


5. Make a dictionary with these keys and values: &#39;name&#39;: &#39;Hydrogen&#39;, &#39;symbol&#39;: &#39;H&#39;, &#39;number&#39;: 1. Then,
create an object called hydrogen from class Element using this dictionary.

ANSWER..

To make a dictionary with keys and values 'name': 'Hydrogen', 'symbol': 'H', 'number': 1, and then create an object called hydrogen from class Element using this dictionary, you can use the following code:

element_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**element_dict)


-------------------------------------------------------------------------------------------------------------------------------


6. For the Element class, define a method called dump() that prints the values of the object’s
attributes (name, symbol, and number). Create the hydrogen object from this new definition and
use dump() to print its attributes.

ANSWER..

To define a method called dump() for the Element class that prints the values of the object’s attributes (name, symbol, and number) and then use this new definition to create the hydrogen object and print its attributes using dump(), you can use the following code:

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('Name:', self.name)
        print('Symbol:', self.symbol)
        print('Number:', self.number)

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump() # prints: Name: Hydrogen, Symbol: H, Number: 1


--------------------------------------------------------------------------------------------------------------


7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__,
create a new hydrogen object, and call print(hydrogen) again.

ANSWER..

To call print(hydrogen), change the name of method dump to str, create a new hydrogen object, and call print(hydrogen) again, you can use the following code:

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}'

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen) # prints: Name: Hydrogen, Symbol: H, Number: 1


-----------------------------------------------------------------------------------------------------------------------------------------


8. Modify Element to make the attributes name, symbol, and number private. Define a getter
property for each to return its value.

ANSWER..

To make the attributes name, symbol, and number private, add two underscores (__) before their names. Then define getter methods using the property decorator to return their values.
Example code:

class Element:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number
        
    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def number(self):
        return self._number


-------------------------------------------------------------------------------------------------------------------------------------------

9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This
should return &#39;berries&#39; (Bear), &#39;clover&#39; (Rabbit), or &#39;campers&#39; (Octothorpe). Create one object from
each and print what it eats.

ANSWER..

class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

# Create one object from each class and print what it eats
bear = Bear()
print(bear.eats())   # Output: berries

rabbit = Rabbit()
print(rabbit.eats())   # Output: clover

octothorpe = Octothorpe()
print(octothorpe.eats())   # Output: campers


-------------------------------------------------------------------------------------------------------------------


10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This
returns &#39;disintegrate&#39; (Laser), &#39;crush&#39; (Claw), or &#39;ring&#39; (SmartPhone). Then, define the class Robot that
has one instance (object) of each of these. Define a does() method for the Robot that prints what its
component objects do.

ANSWER..

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.phone = SmartPhone()
        
    def does(self):
        return f'Laser: {self.laser.does()}, Claw: {self.claw.does()}, Phone: {self.phone.does()}'

Implemention of the code:-

r = Robot()
print(r.does())  # Output: Laser: disintegrate, Claw: crush, Phone: ring

---------------------------------------------------------------------------------------------------------------------

"""



