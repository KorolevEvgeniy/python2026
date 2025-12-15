stations = [
    {"name": "Тимирязевская", "load": [45, 60, 80]},
    {"name": "Савёловская", "load": [50, 65, 75]},
    {"name": "Дмитровская", "load": [40, 55, 60]},
    {"name": "Менделеевская", "load": [68, 72, 85]}
]

periods = ["утро", "день", "вечер"]

result = [
    f"{station['name']} — {periods[i]} ({load_value}%)"
    for station in stations
    for i, load_value in enumerate(station['load'])
    if load_value > 70 and all(value <= 70 for value in station['load'][:i])
]

print(result)