# Class_10

# isistance(object, type) function

# number = 5.00
# if isinstance(number, int):
#     print("Yes")
# else:
#     print("No")

# # No

# number = 5
# if isinstance(number, int):
#     print("Yes")
# else:
#     print("No")

# # Yes

# # ternary operator - one line if statement

# number = 5.0
# print("Yes") if isinstance(number, int) else print("No")

# # No

# string methods 

# lower() 

# s = "Hi There!"
# print(s.lower())
# print(s)
# s2 = s.lower()
# print(s2)

# hi there!
# Hi There!
# hi there!

# upper()

# s = "Hi There!"
# print(s.upper())
# print(s)
# s2 = s.upper()
# print(s2)

# HI THERE!
# Hi There!
# HI THERE!

# capitalize()

# s = "hi there!"
# print(s.capitalize())
# print(s)
# s2 = s.capitalize()
# print(s2)

# Hi there!
# hi there!
# Hi there!

# title()

# s = "he lives in Poznan"
# print(s.title())
# print(s)
# s2 = s.title()
# print(s2)

# He Lives In Poznan
# he lives in Poznan
# He Lives In Poznan

# strip()

# s = "he lives in Poznan"
# print(s.strip())
# print(s)
# s2 = s.strip()
# print(s2)

# he lives in Poznan
# he lives in Poznan
# he lives in Poznan

# s = "he lives in Poznan"
# print(s.strip('nhe'))
# print(s)
# s2 = s.strip('nhe')
# print(s2)

#  lives in Pozna
# he lives in Poznan
#  lives in Pozna

# lstrip()

# s = "he lives in Poznan"
# print(s.lstrip('nha'))
# print(s)
# s2 = s.lstrip('nha')
# print(s2)

# e lives in Poznan
# he lives in Poznan
# e lives in Poznan

#rstrip()

# s = "he lives in Poznan"
# print(s.rstrip('nha'))
# print(s)
# s2 = s.rstrip('nha')
# print(s2)

# he lives in Poz   
# he lives in Poznan
# he lives in Poz 

# find(value)

# s = "he lives in Poznan"
# print(s.find("i"))
# print(s.find("b"))

# 4
# -1

# index(value)

# s = "he lives in Poznan"
# print(s.index("i"))
# 4
# print(s.index("b")) # error

# replace(old_value, new_value, count)

# s = "he lives in Poznan"
# print(s.replace("i", "B"))
# print(s.replace("i", "B", 1))
# print(s.replace("i", ""))

# he lBves Bn Poznan
# he lBves in Poznan
# he lves n Poznan  

# iteration & while loop

# counter = 0 # variable must be initialized
# while counter < 6:
#     print(counter)
#     counter += 1

# 0
# 1
# 2
# 3
# 4
# 5

# # print("## INFINITE LOOP")
# # counter = 0
# # while counter < 6:
# #     print(counter)

# print("## FOR LOOP")
# x = range(5)
# print(x) # WRONG WAY

# for i in range(5):
#     print(i)

# 0
# 1
# 2
# 3
# 4

# for i in range(3, 7):
#     print(i)
# 3
# 4
# 5
# 6

# for i in range(3, 20, 2):
#     print(i)

# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

# for i in "Appalachicola":
#     print(i)

# A
# p
# p
# a
# l
# a
# c
# h
# i
# c
# o
# l
# a

# # summarize all numbers from 0-20

# mysum = 0
# for i in range(0, 21):
#     mysum += i
# print("The sum of numbers 0-20 is", mysum)

# The sum of numbers 0-20 is 210 

# # Counting vowels in a string

# vowels = "aeiou"
# vowelCount = 0
# word = "Appalachicola"
# for ch in word:
#     if ch in vowels:
#         vowelCount += 1
# print("Number of vowels is", vowelCount)

# Number of vowels is 5