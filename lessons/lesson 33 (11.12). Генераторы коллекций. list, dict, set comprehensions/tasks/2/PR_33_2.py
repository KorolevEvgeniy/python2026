films = [
    ("Нолан", 2014),
    ("Прибытие", 2016),
    ("Дюна", 2021)
]
ratings = [
    ("Нолан", 6.9),
    ("Прибытие", 8.0),
    ("Дюна", 7.4)
]
result = [
    f"{film_name} ({year}) - {rating_name} ({rating})"
    for film_name, year in films
    for rating_name, rating in ratings
    if film_name == rating_name and year > 2015 and rating >= 7.5
]
print(result)
