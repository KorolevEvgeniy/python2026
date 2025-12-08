base_gear = ["палатка", "спальник", "коврик"] # Базовое снаряжение
dop_gear = ["фонарик", "аптечка", "карта"]  # Дополнительное снаряжение
all_gear = base_gear + dop_gear # Объединяем оба списка
total_items = len(all_gear)
first_item = all_gear[0]
last_item = all_gear[-1]
print(f"Общее количество предметов: {total_items}")
print(f"Первый предмет: {first_item}")
print(f"Последний предмет: {last_item}")
print("\nВесь список снаряжения:")
for i, item in enumerate(all_gear, start=1):
    print(f"{i}. {item}")