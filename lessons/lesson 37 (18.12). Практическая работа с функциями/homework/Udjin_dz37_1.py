def rectangle_info(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter
area, perimeter = rectangle_info(5, 3)
print(f"Площадь: {area}, Периметр: {perimeter}")

def is_adult(age):
    if age < 0:
        return "Ошибка: возраст не может быть отрицательным"
    else:
        return age >= 18
print(is_adult(20))  
print(is_adult(17.5))  
print(is_adult(18))  
print(is_adult(-30))   
print(is_adult(70)) 

def safe_div(a, b):
    if b == 0:
        return None
    return a / b
print(safe_div(8, 2)) 
print(safe_div(10, 0)) 
print(safe_div(20, 3)) 