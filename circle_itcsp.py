'''
Exercise 05
Write a program that will calculate circle area (and print to the terminal),
radius is 5 cm,
lets's assume pi = 3.14
A=𝜋𝑟^2 (this is our formula)
expected result: e.g.,

"Circle area is: 78.5 cm2"

'''


def circle_itcsp():
    radius = 5
    pi = 3.14

    a = pi*(radius ** 2)
    print("Circle area is: ", a, "cm2")

circle_itcsp()

