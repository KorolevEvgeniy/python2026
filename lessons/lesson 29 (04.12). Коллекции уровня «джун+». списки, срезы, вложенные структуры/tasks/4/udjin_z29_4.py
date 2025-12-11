seansy = [
    {"week": 1, "meeting": "Zoom", "topic": "синхронизация", "students": ["Аня", "Кирилл"]},
    {"week": 2, "meeting": "Discord", "topic": "проект", "students": ["Кирилл", "Марк", "Лиза"]}
]
focus_student = "Кирилл"

for seans in seansy:
    print(f"Неделя {seans['week']}. Тема. {seans['topic']}. Участники. {', '.join(seans['students'])}")

vse_students = {student for seans in seansy for student in seans["students"]}
print(f"\nВсе студенты. {vse_students}")

размер_групп = {seans["topic"]: len(seans["students"]) for seans in seansy}
print(f"\nРазмер групп по темам. {размер_групп}")


seansy_focus = [seans.copy() for seans in seansy if focus_student in seans["students"]]
print(f"\nСессии с {focus_student}. {seansy_focus}")
