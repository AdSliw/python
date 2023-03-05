# # Class_13

# # tuples are immutable, ordered sequences of elements

# # Tuples declaration

# t1 = ()
# print(t1)
# t2 = (1, 'two', 3.25)
# print(t2)

# Extra comma means a tuple with one elements
# t3 = ('one',)  # if only one element, needs an extra comma
# print(t3)

# # tuple's indices, getting element value
# t2 = (1, 'two', 3.25)
# print(t2[0])

# t5 = (1, 'two', 3.25, ('a', 'b', 'c'))
# print(t5)

# t2 = (1, 'two', 3.25)
# tuples are immutable
# t2[0] = 2 # error

# Slicing tuple
# t2 = (1, 'two', 3.25)
# print(t2[1:2])

# tuples - concatenation operator '+'
# this operation creates new tuple

# t2 = (1, 'two', 3.25)
# t3 = ('one',)
# t4 = t2 + t3
# print(t4)

# # t2 = (1, 'two', 3.25)
# # t3 = 'one'
# # t2[3] = 'one' # ERROR

# # iterating over tuples

# # compute the sum of elements of a tuple

# T = (1, 2, 3, 4)
# sum = 0
# for i in T:
#     sum += i
# print(sum)

#10

# T = (1, 2, 9, 5)
# sum = 0
# for i in range(len(T)):
#     sum += T[i]
# print(sum)

# # DICTONARIES

# # indexed by keys, type: dict

# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}

# s_grade = student_grades['Ana']
# print(s_grade)

# B

# # Add an entry
# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# student_grades['Bob'] = 'A'
# print(student_grades)

# # change the value
# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# student_grades['Ana'] = 2
# print(student_grades)

# # getting the value
# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# s_grade = student_grades.get('Rob', 'No such key')  # returns 'No such key'
# print(s_grade)

# # DELETING AN ENTRY
# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# s_grade = student_grades.pop('Bob')
# print(s_grade)

# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# del (student_grades['Katy'])
# print(student_grades)

# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# s_grade = student_grades.pop('Rob', 'No such key')  # returns 'No such key'
# print(s_grade)

# # searching element(key) in dictionary
# # using membership operator 'in'

# print('John' in student_grades)

# student_grades['Bob'] = 'B'

# # keys() method returns the view object of dictionary keys

# print(student_grades.keys())

# # keys converted to list
# print(list(student_grades.keys()))
# for k in student_grades.keys():
#     print(k)

# # getting an iterable of all values
# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# student_grades.values()
# print(list(student_grades.values())) !!!
# for v in student_grades.values():
#     print(v)

# # getting an iterable of all items (pairs)
# print(student_grades.items())
# print(list(student_grades.items())) !!!
# for i in student_grades.items():
#     print(i)

# # items converted to

# student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# month_numbers = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '4'}
# for k, v in student_grades.items():
#     print(k, v)

# # len()

# print(len(student_grades))

# # copying a dict

# s_grade = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}

# s_grade = s_grade.copy()
# print(s_grade)

# # removing all elements from a dict
# s_grade.clear()
# print(s_grade)

# How to get value from dictionary of dictionaries:
# data = {
#     "key1": {
#         "inner_key1": 1,
#         "inner_key2": 2
#     },
#     "key2": {
#         "inner_key1": 3,
#         "inner_key2": 4
#     }
# }
# value = data.get("key1").get("inner_key1")
# value = data['key1']['inner_key2']
# print(value)  # Output: 1

# print(data)

# # F-STRINGS - strings that allow for functions in {} brackets

# name = 'Adam'
# print(f'My name is {name} :)')

# var1 = 2
# var2 = 5
# print(f'{var1} multiplied by {var2} equals: {var1*var2}')

# #  FUNCTIONS DEFINITIONS - defining reusable functions

# Function checks whether the number is even or odd.
# Parameters:
#     i (int): positive int number to be checked
# Returns:
#     (bool): True if i is even, otherwise False


# def is_even(i):
#     return i % 2 == 0

# print(is_even(3))
# print(is_even.__doc__)  # prints docstring

# #  FUNCTION DEFINITION (WITHOUT RETURN STATEMENT)


# def send_greetings(name: str) -> None:
#     '''
#     Function prints a greeting

#     Parameters:
#         name: name of the person
#     '''
#     print(f"Hello {name}")


# send_greetings("Adam")
# print(send_greetings.__doc__)
