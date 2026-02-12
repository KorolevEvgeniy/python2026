import re

def extract_dates(text):

    date_pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    
    dates = re.findall(date_pattern, text)
    
    return dates

text = "Сегодня 25.04.2024, а завтра будет 26.04.2024."

found_dates = extract_dates(text)

print("Найденные даты:")
print(found_dates)

