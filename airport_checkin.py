class AirportFastCheckIn:

    def __init__(self, customer_id, country, money, luggage_weight):
        self.customer_id = customer_id
        self.country = country
        self.money = int(money)
        self.luggage_weight = int(luggage_weight)

    def check_for_pass(self):
        country_check = self.country == str('USA')
        money_check = 100 < self.money < 1000
        luggage_weight_check = self.luggage_weight <= 20
        condition = country_check == money_check == luggage_weight_check
        print('For customer', self.customer_id, 'condition is:', condition)


data1 = AirportFastCheckIn(1, 'PL', 500, 20)
data2 = AirportFastCheckIn(2, 'USA', 500, 20)
data3 = AirportFastCheckIn(3, 'EU', 2000, 20)
data4 = AirportFastCheckIn(4, 'EU', 500, 30)
data1.check_for_pass()
data2.check_for_pass()
data3.check_for_pass()
data4.check_for_pass()

'''
[customer_id = '1', country="PL", money = 500, luggage_weight = 20]
[customer_id = '2', country="USA", money = 500, luggage_weight = 20],
[customer_id = '3', country="EU", money = 2000, luggage_weight = 20],
[customer_id = '4', country="EU", money = 500, luggage_weight = 30]]
'''
