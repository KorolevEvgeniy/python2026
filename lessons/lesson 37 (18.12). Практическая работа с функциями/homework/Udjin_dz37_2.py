def delivery_price(city, weight_kg, urgent):
    if urgent:
        return 500 + 30 * weight_kg
    else:
        return 300 + 20 * weight_kg
print("1. Уфа, 5 кг, обычная:", delivery_price("Уфа", 5, False))
print("2. Киров, 2.5 кг, срочная:", delivery_price("Киров-град", 2.5, True))
print("3. Казань, 10 кг, обычная:", delivery_price(city="Казань", weight_kg=10, urgent=False))
print("4. Саратов, 1 кг, срочная:", delivery_price(urgent=True, weight_kg=1, city="Саратов"))
#print("5. Москва, 1 кг, срочная:",delivery_price("Москва", 5, urgent=True, extra_param=100))
#print("6. Москва, 1 кг, срочная:",delivery_price(city="Москва", 5, urgent=False)