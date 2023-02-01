# # Class_12

# # LISTS part 2

# # Iterating over the list

# L = [1, 2, 9, 5]

# for i in L:
#     print(i)

# L2 = [1, 2, 9, 5]

# for i in range(len(L2)): 
#     print(L2(i))


# compute sum of elements

# L2 = [1, 2, 9, 5]
# sum = 0
# for i in L2: # here 'i' is a list element
#     sum+= i
#     print(sum)

# ver 02

# L = [1, 2, 9, 5]
# sum = 0
# for i in range(len(L)):
#     sum += L[i]
#     print(sum)

# # add element to a list

# L = [1, 2, 9, 5]
# L.append(9)
# print(L)

# # list concatenation. '+' operator
# L1 = [2, 6, 3]
# L2 = [8, 7, 3]
# L3 = L1 + L2
# print(L3)

# # list extending, extend() method

# L1 = [2, 6, 3]
# L2 = [8, 7, 3]
# L1.extend(L2) # L1 has a new structure
# print(L1)

# removing an element from the list
# 1. remove() method (only first occurance)

# L = ['apple', 'banana', ' cherry', 'banana'] !!!
# L.remove('banana')
# print(L)
# # L.remove('pineapple')

# # 2. pop() method (removes the last item) !!!

# L = ['apple', 'banana', ' cherry', 'banana']
# L.pop()
# print(L)

# 3. pop(index) method (removes element at the specified index) !!!

# L = ['apple', 'banana', ' cherry', 'banana']
# L.pop(1)
# print(L)

# # 4. del(index) function (removes element at the specified index) !!!

# L = ['apple', 'banana', ' cherry', 'banana']
# del(L[1])
# print(L)

# # clear() method (removes all elements from the list)

# L = ['apple', 'banana', ' cherry', 'banana']
# L.clear()
# print(L)

# # converting string to list
# # list() function

# s1 = "Hello World!"
# L = list(s1)
# print(L)

# # split the string into a list
# # split() on space, default way)

# s1 = "Hello World!"
# print(s1.split())

# s1 = "value1,value2,value3"
# L = s1.split(',')
# print(L)

# # converting lists to  strings
# # string.join(iterable)

# L = ['a','b','c','d']
# result = '*'.join(L)
# print(result)

# L = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
# text = ''.join(L)
# print(text)

# # sorting lists

# # 1. sort() method 
# L = [6,5,4,10,15,2]
# L.sort()
# print(L)

# L = [6,5,4,10,15,2]
# L.sort(reverse = True)
# print(L)

# # 2. sorted(list), returns the sorted list, does not mutate list
# L = [6,5,4,10,15,2]
# L1 = sorted(L)
# print(L1)

# # reversing the elements of the list
# # reverse() mutates the list
# L = [6,5,4,10,15,2]
# L.reverse()
# print(L)

# # counting specified elements of the list

# L = [6,5,4,10,15,6]
# print(L.count(6))

# # counting all elements of the list

# L = [6,5,4,10,15,6]
# print(len(L))







