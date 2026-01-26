import os

# Задача 1
def print_participants(path):
    if not os.path.exists(path):
        print("Нет файла со списком участников")
        return
    
    with open(path, 'r', encoding='utf-8') as file:
        names = []
        for line in file:
            stripped = line.strip()
            if stripped:  # игнорируем пустые строки
                names.append(stripped)
    
    if not names:
        print("Список участников пуст")
        return
    
    print(f"Участники ({len(names)}):")
    for i, name in enumerate(names, 1):
        print(f"{i}) {name}")

if __name__ == "__main__":
    print("=== Задача 1 ===")
    path_participants = "participants.txt"
    print_participants(path_participants)

def add_to_log():
    path_log = "log.txt"
    
    message = input("Введите сообщение: ").strip()
    if not message:
        print("Пустое сообщение. Ничего не записано")
        return
    
    with open(path_log, 'a', encoding='utf-8') as file:
        file.write(message + '\n')
    
    print("Запись добавлена")
 

def create_score_report():
    path_scores = "scores.txt"
    path_report = "report.txt"
    
    if not os.path.exists(path_scores):
        print("Нет файла с оценками")
        return
    
    valid_data = []
    
    with open(path_scores, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            stripped = line.strip()
            if not stripped:
                continue
                
            parts = stripped.split()
            if len(parts) != 2:
                continue
            
            name, score_str = parts
            if not score_str.isdigit():
                continue
            
            score = int(score_str)
            valid_data.append((name, score))
    
    if not valid_data:
        print("Нет корректных данных")
        return
