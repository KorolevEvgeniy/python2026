def make_multiplier(factor):
    def mul(x):
        return x * factor
    return mul


double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(10) = {double(10)}") 
print(f"triple(10) = {triple(10)}")\

def mean(*args):
    if not args:  
        return None
    
    return sum(args) / len(args)

print(f"mean() = {mean()}") 
print(f"mean(1, 2, 3) = {mean(1, 2, 3)}")
print(f"mean(10, 20, 30, 40) = {mean(10, 20, 30, 40)}")

def build_profile(**kwargs):

    profile = {
        "name": kwargs.get("name", "Без имени"),
        "age": kwargs.get("age", 0),
        "extra_info": kwargs
    }
    
    return profile



profile1 = build_profile(name="Андрей", age=23, city="Уфа", job="Студент")
print("Профиль 1 :")
for key, value in profile1.items():
    print(f"  {key}: {value}")

profile2 = build_profile(name="Андрей")
print("Профиль 2 :")
print(f"  Имя: {profile2['name']}")
print(f"  Возраст: {profile2['age']}")

profile3 = build_profile(age=23, city="Уфа")
print("Профиль 3 :")
print(f"  Имя: {profile3['name']}")
print(f"  Возраст: {profile3['age']}")
print(f"  Город: {profile3['extra_info'].get('city')}")

profile4 = build_profile()
print("Профиль 4 :")
print(f"  Имя: {profile4['name']}")
print(f"  Возраст: {profile4['age']}")