# Исходные данные
spisok_uchastnikov = [
    {"имя": "Алексей", "роль": "гид", "вес_рюкзака": 20},
    {"имя": "Мария", "роль": "участник", "вес_рюкзака": 12},
    {"имя": "Иван", "роль": "гид", "вес_рюкзака": 18},
    {"имя": "Елена", "роль": "участник", "вес_рюкзака": 10}
]

print("1. Все участники:")
for person in spisok_uchastnikov:
    print(f"{person['имя']}: {person['роль']} ({person['вес_рюкзака']} кг)")

print("\n2. Участники с рюкзаком более 15 кг:")
heavy_backpack = [person["имя"] for person in spisok_uchastnikov if person["вес_рюкзака"] > 15]
print(f"   {heavy_backpack}")

print("\n3. Группа гидов:")
guides = [person for person in spisok_uchastnikov if person["роль"] == "гид"]
for guide in guides:
    print(f"   {guide['имя']}: {guide['вес_рюкзака']} кг")

print("\n4. Статистика весов:")
total_ves = sum(person["вес_рюкзака"] for person in spisok_uchastnikov)
sredniy_ves = total_ves / len(spisok_uchastnikov)
print(f"   Общий вес всех рюкзаков: {total_ves} кг")
print(f"   Средний вес рюкзака: {sredniy_ves:.1f} кг")