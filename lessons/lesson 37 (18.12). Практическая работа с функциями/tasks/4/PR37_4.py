def make_multiplier(factor):
    def mul(x):
        return x * factor
    return mul

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(10) = {double(10)}") 
print(f"triple(10) = {triple(10)}")

def mean(*args):
    if len(args) == 0:
        return None
    return sum(args) / len(args)

def build_profile(**kwargs):
    profile = {
        "name": kwargs.get("name", "Без имени"),
        "age": kwargs.get("age", 0)
    }
    for key, value in kwargs.items():
        if key not in profile:
            profile[key] = value
    return profile

print(f"\nmean(1, 2, 3, 4, 5) = {mean(1, 2, 3, 4, 5)}") 
print(f"mean() = {mean()}") 
print(f"mean(10, 20) = {mean(10, 20)}") 
print(f"\nbuild_profile(name='Alex', age=40, city='Ufa') = {build_profile(name='Alex', age=40, city='Ufa')}")
print(f"build_profile(age=30) = {build_profile(age=30)}")
print(f"build_profile(name='Anna') = {build_profile(name='Anna')}")
print(f"build_profile() = {build_profile()}")
