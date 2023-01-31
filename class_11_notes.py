# Class_11

# while True:
#     text = input('Enter any text: \n')
#     if text == "exit":
#         break


## LISTS

L1 = [1, 3, 2, 7, 5] #list is usually hoogeneous
L2 = ['Hello', 'World', 'Smile']
L3 =[[1, 2, 7, 3], 'Warsaw', 5]
L4 = [[1, 2, 7, 3], [14, 9, 15, 6]]
L5 = [] # this is an empty list

print(L1)

print("count(element) method")
L = [6, 5, 4, 10, 15, 8]
print(L.count(6))

first_list = [2, 'cat', 5.0, True]
print(first_list[0])
print(first_list[1])
print(first_list[2])
print(first_list[3])
# print(first_list[4]) error

print(len(first_list))

i = 2
print(first_list[i-1])

# LIST ARE MUTABLE

first_list[0] = 3
print(first_list[0])

# STRING ARE IMMUTABLE
text = 'Hello'
print(id(text))
print(hex(id(text)))












