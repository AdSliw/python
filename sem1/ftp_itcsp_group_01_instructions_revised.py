'''
ITCSP, Final Programming Task, 1LMT, group 01
(30 points)

Let's imagine you are a young entrepreneur. 
You decided to start a shop.
Write a program to handle the assortment of your store. 
Implement the following functionalities:

adding product, 
changing the name of product, 
deleting product, 
showing all products on the terminal screen.


First, consider what data structure you will use to store your product names.
Data structure you use for storing product names should be a variable 'products'

Data structure: ________________


I see the program-user interaction as follows ( please printout on the terminal as below):

    =========================================
    Store management software, version 1.0.0
    =========================================
    Please select the operation you want to perform:

1. Add a product
    Selecting the operation number should result in the appearance of a message, e.g

        --> Enter the name of the product you want to add ...


2. Change the name of the product
    The user should now enter the product number and the program should give the option to enter a new name.
    Now the user should enter the name of the new product and the program should add this name to the data structure.

        --> Enter the product number you want to rename ...

3. Remove the product
    The user should now enter the product number, and after that, the program should remove the product.

        --> Enter the product number you want to remove ...
    


4. Show all products

    Printing to the terminal
    Selecting option 4 should result in printing to the terminal the names of all products entered in the previous step along with their indexes (but starting from number 1, not 0).

        Showing all products operation should be implemented as a function "show_products(products: list) -> None" and invoked if you choose required option

            def show_products(products: list) -> None:
                
                    Function prints all products

                    Parameters : 
                        products: enumerated list of products
                        eg. 1. Orange
                            2. Bananas

    # here your function code block

    Selecting number 4 should show all products you have enetered during runtime, e.g.,

        My products:
        1. Bananas
        2. Oranges
        3. Apples
        4. Figs
        5. Strawberries
        =====  Finished




5. Exit the program

    Finishing work with the program
    Selecting option 5 should result in termination of work with the program
        --> ... 
        ++++++++++++++



If you have enough time, implement error handling (for volunteers)

PASTE YOUR SOURCE CODE ON TEAMS !!! (ftp_itcsp_01.py)
'''


### HERE REST OF THE PROGRAM:

products = ['Apple']
def storeManagementSoftware():
    '''    
    =========================================
    Store management software, version 1.0.0
    =========================================
    Please select the operation you want to perform:
    1. Add a product
    2. Change the name of the product
    3. Remove the product
    4. Show all products
    5. Exit the program
    '''
    print(storeManagementSoftware.__doc__)
    menuChoice = input('Operation --> ')

    def addProduct():
        newProduct = input('Name the product --> ')
        products.append(newProduct)
        print('Product:', newProduct, 'added.')

        storeManagementSoftware() #go_back

    def changeName():
        productNumeration = 0
        for product in products:
            productNumeration = productNumeration + 1
            print(str(productNumeration) + ".", product)
        try:
            selectedProductForNameChange = int(input('Enter the product number you want to rename --> ')) - 1
            selectedProductNewName = input('Enter the product new name --> ')
            print('Product:',products[selectedProductForNameChange], 'has been changed to:', selectedProductNewName)
            products[selectedProductForNameChange] = selectedProductNewName
        except Exception as e:
            print('Error,',str(e),', perhaps you have chosen wrong element.')
            storeManagementSoftware()

        storeManagementSoftware() #go_back

    def removeProduct():
        productNumeration = 0
        for product in products:
            productNumeration = productNumeration + 1
            print(str(productNumeration) + ".", product)
        try:
            selectedProductForRemove = int(input('Enter the product number you want to remove --> ')) - 1
            removedProduct = str(products[selectedProductForRemove])
            products.pop(selectedProductForRemove)
            print('Product:',removedProduct,'removed.')
        except Exception as e:
            print('Error,',str(e),', perhaps you have chosen wrong element.')
            storeManagementSoftware()

        storeManagementSoftware() #go_back

    def subShowProducts():

        def showProducts(product: list) -> None:
            productNumeration = 0
            for product in products:
                productNumeration = productNumeration + 1
                print(str(productNumeration) + ".", product)

        showProducts(products) #!
        storeManagementSoftware() #go_back

    def exitProgram():
        '''
        ===================
        Program terminated.
        ===================
        '''
        print(exitProgram.__doc__)
        exit


    if menuChoice == str(1):
        addProduct()
    elif menuChoice == str(2):
        changeName()
    elif menuChoice == str(3):
        removeProduct()
    elif menuChoice == str(4):
        subShowProducts()
    elif menuChoice == str(5):
        exitProgram()
    else: 
        print('Choose the correct number!')
        storeManagementSoftware() #go_back

try:
    storeManagementSoftware()
except Exception as e:
        print('Error.' + str(e))
        storeManagementSoftware()
