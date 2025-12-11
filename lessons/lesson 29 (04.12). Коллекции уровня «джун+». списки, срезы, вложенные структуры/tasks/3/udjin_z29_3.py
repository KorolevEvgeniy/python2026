# Исходные данные
kisti = ["круглая №1", "плоская №6", "веерообразная"]
dop_kisti = ["тонкая синтетика", "широкая щетина"]

kisti.extend(dop_kisti)
kisti.insert(2, "детальная №0")
print(kisti)

kisti.remove("веерообразная")

последняя = kisti.pop()
kisti.insert(0, последняя)

print(kisti)
