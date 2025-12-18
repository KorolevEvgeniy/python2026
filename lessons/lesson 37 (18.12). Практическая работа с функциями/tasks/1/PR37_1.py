def rectangle_info(width, height):
    ploshad = width * height
    perimetr = (width + height) * 2
    return ploshad, perimetr
result = (rectangle_info(13, 8))
print(f"Площадь и периметр = {result}")


def is_adult(age):
    
    if age >= 18:
        return True
    else:
        return False
    
print(is_adult(18))

def safe_div(a, b):
    if b == 0:
        return None
    return a / b
print(safe_div(2, 0))
