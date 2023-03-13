L1 = [('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)]

filtered_items = []

def get_price_filtered_list(filtering_criterion, items):
    for element in items:
        if element[1] > filtering_criterion:
            filtered_items.append(element)

get_price_filtered_list(15, L1)

print(filtered_items)