def delivery_price(city, weight_kg, urgent):
    if urgent:
        return 500 + 30 * weight_kg
    else:
        return 300 + 20 * weight_kg
print(delivery_price("Rim", 20, True))  

pos1 = delivery_price("Rim", 20, True)
pos2 = delivery_price("Rim", 20, False)
imen1 = delivery_price(city = "Rim", weight_kg = 20, urgent = True)
imen2 = delivery_price(weight_kg = 20, urgent = True, city = "Rim")
print(f"\n{pos1} \n{pos2} \n{imen1} \n{imen2}")
