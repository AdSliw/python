"""
Exercise 08
Write a program that asks the user for their first name, year of birth and the current year, then calculates
and lists the information about name and age in the terminal.
Sample workflow:
Enter your name: ... Ann
Enter your birth Year: ... 2001
Enter the current Year: ... 2021

Sample result
Ann, you are 20 years old.

"""

first_name = input('Enter your name: ')
year_of_birth = int(input('Enter your birth Year: '))
current_year = int(input('Enter the current Year: '))

age = current_year - year_of_birth

print(first_name + ', you are ' + str(age) + ' years old.')
