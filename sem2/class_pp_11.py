'''
OOP (object oriented programming) paradigm

(a programming paradigm is a style, or "way, ” of
programming.)

Object Oriented Programming (OOP) is a paradigm in
which real-world objects are each viewed as seperate
entities having their own state.

(state are the values of variables used in the program
while it is running.)

Each object is composed of data structures consisting of
datafields and methods together with their interactions

Every Object has
a type e.g., int, string, list .
• a set of properties and/or procedures for interaction with the object ;
Each instance is a particular type of object
789 is an instance of int
a = 'Hello World' is an instance of a string class (methods : lower(), upper(), join())
• everything in Python is an object and has a type
• we qan create new instances of objects
• we can destroy objects using del or „forget"

When we just „forget" the instance of an object, Python
will make them destroyed or inaccessible using so called
„garbage collection"

OOP ADVANTAGES
You do it ALL with CLASSES:

- bundle data into packages together with methods that
work on them through well-defined interfaces
- make it easy to reuse code
- make it easier to test the code
- you can create and use your own real-world objects.

HOW CLASSES MIMIC REAL LIFE?

Mimic real life
Group different objects as part of the same type!

DEFINE YOUR OWN TYPES
• CLASS components:

ATTRIBUTES -> data and procedures/methods that "belong" to the class
Data attributes
    - how can you represent your object with data?
    - think of data as other objects that make up the class
        (e,g, for an animal: age, name)

- Procedural attributes (behaviour / operations / methods)
    - what kinds of things can you do with the object, what it does ?
    - think of methods as functions that only work with this class
        (e,g., for an animal: make a sound)
-   for e@mple you can define a distance between two coordinate objects
        but there is no meaning to a distance between two list objects

Use the class keyword to define a new type
CLASS DEFINITION:

            Parent Class
                |
                v

class Animal (object):                  <- INHERITANCE
        <define attributes here>

example:

class Animal(object):
    def __init__ (self, age):
        self.age = age                  <- ENCAPSULATION
        self.name = None  



'''

# DEFINE YOUR OWN TYPES (CLASS)
# Parrent class
class Animal (object):
    def __init__(self, age) :
        self.age = age
        self.name = None

    def __str__(self) :
        return "Animal name:"+str(self. name)+", age: "+str(self.age)

class Cat(Animal):
    def __init__(self, age):
        self.name = None
        self.age = 15

    def speak(self):
        print('meow')

    def __str__(self): #this one ovverides the str from class(Animal)
        return "Cat name: "+str(self. name)+" age:"+str(self.age)

animec = Animal(12) #overrides the 
animec.name = "Animec"
animec.age = 2
print(animec)

anima = Animal(8)
anima.name = 'ANIMA'
print(anima)

billy = Cat(2)
billy.name = "Billy"
billy.speak()
print(billy)

johny = Cat(3)
johny.name ="Johny"
johny.speak()
print(johny)