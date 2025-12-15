events = [
    "backend:code-review:15",
    "android:deploy:45",
    "frontend:hotfix:10",
    "backend:hotfix:30",
    "frontend:code-review:70",
    "mobile:code-review:25",
    "invalid_format",
    "backend:code-review:50",
    "frontend:code-review:45",
    "devops:hotfix:5"
]

rapid_departments = {
    parts[0]  # dept
    for event in events
    if (parts := event.split(":")) and len(parts) == 3
    if parts[1] in ["code-review", "hotfix"] and int(parts[2]) < 20
}

dept_reviews = {}
for event in events:
    parts = event.split(":")
    if len(parts) != 3:
        continue
    dept, action, minutes = parts[0], parts[1], parts[2]
    if action == "code-review":
        dept_reviews.setdefault(dept, []).append(int(minutes))

review_slots = {
    dept: durations
    for dept, durations in dept_reviews.items()
    if all(duration <= 60 for duration in durations)
}

print("rapid_departments:", rapid_departments)
print("review_slots:", review_slots)