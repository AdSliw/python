'''
Abstraction, 
think about it as defining an abstract
representation of a system.
Modeling the relevant
attributes and interactions
of entities as classes

Encapsulation, 
Hiding the internal state and
functionality of an object
and only allowing access
through a public set of
functions:

class Animal(object):
    def init (self, age) :
        self.age = age
        self.name = None


Inheritance (programming) 
allows us to define a class
that inherits all the data attributes and data methods
from another class, which means that in addition to its
own data attributes and methods, it also obtains those
derived from the class from which it inherits.

Polymorphism, 
Ability to implement inherited
properties or methods
in different ways across
multiple abstractions:

class Animal(object):
...
    def speak(self):
        print(f"I am an animal. My name is {self. name}. ")
    def __str__(self) :
        return f "Animal name: {self. name}, age: {selfage}"

class Cat(Animal):
    def speak(self):
        print(f"I am an cat. My name is {self. name}. Moew")
    def __str__(self):
        return f"name: {self.name}, age: {self,age}"

Special operators:
    +, >, len(), print, and many others

https://docs.python.org/3/reference/datamodel.html#basic-customization

- like print, can override Onese to work with your class
- define them with double underscores before/after

__add__ (self, other) -> self + other
__sub__(self, other) -> self - other
__eq__(self, other) self == other
__It__ (self, other) self < other
-------
(self)
__str__ (self) print(self)
and others



Cse a special method called __init__() if you want to initialize some
data attributes (constructor).

But you almost always haye data attributes in the class, and it is a good
practice to initialize them, even by using the default values

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

(age, name) -> two data attributes for every Animal object
(self) -> parameter to refer to an instance of the class


jelly = Cat(4)

At the same time, the init 0 method is called
implicitly and automatically.

jelly.set_name(' Jelly' )
jelly.speak()
billy = Cat(5)

• Anjmaljs a parent class (superclass) of the Cat
• Cat is a child class (subclass) of the Animal
1
class Cat (Animal):
def speak(self):
print ( "meow" )
def str (self):
return "cat: "+str(self.name)+" : "+str(self.age)



'''
import random

class Animal(object):
    def __init__ (self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return f"Animal name: {self.name}, animal age:{self.age}"

    def speak(self):
        print (f" I am a cat. My name is {self.name}. Meow")

class Cat(Animal):
    def speak(self):
        print(f'Meow')

    def __str__(self):
        return f"Animal name: {self.name}, animal age:{self.age}"

class Person(Animal):
    def __init__(self, name, age):
        # in the body of the class we can invoke (Parent class) Animal.__init__() to set an
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def __eq__(self, other):
        return self.name == other.name

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        # the same way we can invoke any other parrent method
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(f"{self.name} is {diff} years older than {other.name} ")
        else:
            print(f"{self.name} is {-diff} years younger than {other. name}" )

    def __str__(self): # overrides __str__() method from Animal class
        return f"Person name: {self.name}, person age: {self.age}"

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print('i have homework')
        elif 0.25 <= r < 0.5:
            print('i need sleep')
        elif 0.5 <= r < 0.75:
            print('i should eat')
        else: 
            print('i am watching tv')

def __str__(self): # overrides __str__() method from Person class
    return f"Student name: {self.name}, student age: {self.age}"



# animec = Animal (10)
# animec.name = "Animec"
# animec.age - 12
# animec.speak()
# # print(animec)

# jelly = Cat(4)
# jelly.set_name('Jelly')

# tiger = Cat(1)
# tiger.set_name('Tiger')

# hillary = Person('Hillary', 25)
# print(hillary)
# tom = Person('Tom', 32)
# print(tom)

# hillary.add_friend('Tom')
# print(hillary.get_friends())
# hillary.age_diff(tom)
# tom.age_diff(hillary)
# print(tom == hillary)

# john = Student('John', 25, 'IT Dept')
# jack = Student('Jack', 27, 'IT Dept')
# print(john)
# john.speak()
# print(jack)
# jack.speak()
# john.age_diff(jack)
# jack.add_friend('John')
# print(jack.get_friends())