shelves = [
    ('cereals', 'Аня'),
    ('spices', 'Илья'),
    ('fruits', 'Маша'),
]
check_shelf = 'spices'
empty_shelf = 'tea'

restock_by = {}
for shelf_name, volunteer_name in shelves:
    restock_by[shelf_name] = volunteer_name


print(f"{check_shelf} -> {restock_by.get(check_shelf, 'пока никто')}")
print(f"{empty_shelf} -> {restock_by.get(empty_shelf, 'пока никто')}")
