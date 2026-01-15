def print_attendees(path: str):
        try:
                with open(path.txt, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
        except FileNotFoundError:
                print("Нет файла со списком участников")
                return
        attendees = []
        for line in lines:
                cleaned_name = line.strip()
                if cleaned_name: 
                    attendees.append(cleaned_name)
        if not attendees:
                print("Список участников пуст")
                return        
        print(f"Участники ({len(attendees)}):")
        for i, name in enumerate(attendees, start=1):
                print(f"{i}) {name}")
