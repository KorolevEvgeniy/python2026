stations = {
    "Тверская": [65, 82, 77],
    "Савёловская": [55, 60, 58],
    "Бауманская": [71, 69, 88]
}
labels = ["утро", "день", "вечер"]

result = [
    f"{name} → {labels[i]}"
    for name, loads in stations.items{}
    if any(load > 70 for load in loads)
    for i in range(3)
    if loads[i] > 70
    if i == next((idx for idx, load in enumerate(loads) if load > 70), None)
]

print(result)
