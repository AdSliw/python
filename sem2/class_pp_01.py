# def sendGreetings(name):
#     return f'Hello {name}'

# print(sendGreetings('Adam'))

# start = '''
# ========================================
# Store management software, version 1.0.0
# ========================================
# '''
# products = []

# def show_products(products: list) -> None:
#     '''
#     Function prints all products 

#     Parameters :
#         products: list of products
#         eg. 1. Orange
#             2. Banana
#     '''

#     print('\n===== My products: ')
#     for i in range(len(products)):
#         print(f'{i+i}. {products[i]}')
#     print('===== Finished\n')

# menu = '''
# Please select the operaton you want to perform:
# 1. Add a product
# 2. Change the name of the product
# 3. Remove the product
# 4. Show all products
# 5. Exit the program

# '''

# while True:
#     print(menu)
#     operation = input('--> ...')
#     if operation == '5':
#         break
#     elif operation == '1':
#         name = input('Enter the number of the product you want to add ...')
#         products.append(name)
#         print(f'--> ... {name} added\n')
#     elif operation == '2':
#         index = int(
#             input('Enter the product number you want to rename ...'))
#         old_name = products[index-1]
#         new_name = input(f'Enter the new name for '{old_name}' ...')
#         products[index - 1] = new_name
#         print(f'--> ... {old_name} renamed\n')
#     elif operation == '3':
#         index = int(
#             input('Enter the product number you want to rename ...'))
        
#     elif operation == '4':


### UNFINISHED

# def add_profile(index, ix, iy, area):
#     print(
#         f' Adding profile {index} with moments of inertia Ix={ix} cm4, Iy={iy} cm4 and area {area} cm2')

# #ver1
# add_profile('MC014', 166.9, 23.6, 30)
# #ver2
# add_profile('MC014', ix=166.9, iy=23.6, area=30)

# #we can define default arguments in function definition
# print('1_line', 'Hello')
# print('2_line', 'World')
# #parameters are defined in function definition
# print('1_line', 'Hello', sep='', end=' ')
# print('2_line', 'World', sep='')

#default arguments in function definition

# def add_item(item_name, quantitiy=1):
#     print(f'{quantitiy} units of {item_name} was added')

# add_item('bread')
# add_item('apples', 2)