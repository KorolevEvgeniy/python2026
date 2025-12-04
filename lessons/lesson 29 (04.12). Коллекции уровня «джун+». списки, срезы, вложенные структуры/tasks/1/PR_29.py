base_set = ["кисть круглая", "кисть плоская", "гуашь"]
extras = ["акварель", "палитра"]
base_set.extend(extras)
print("Всего предметов: ", len(base_set))
print("Второй предмет: ",(base_set[1]))
print("Последний предмет: ",(base_set[-1]))
for index, item in enumerate(base_set, start=1):
    print(f"{index}. {item}")
