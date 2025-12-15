hubs = [
    {"name": "DevHub", "capacity": 200, "streams": [{"viewers": 120}, {"viewers": 80}]},
    {"name": "CodeLab", "capacity": 150, "streams": [{"viewers": 90}]},
    {"name": "TechSpace", "capacity": 300, "streams": [{"viewers": 150}, {"viewers": 120}, {"viewers": 80}]},
    {"name": "EmptyHub", "capacity": 100, "streams": []}
]
hub_load = {
    hub["name"]: round(sum(stream["viewers"] for stream in hub["streams"]) / hub["capacity"], 1)
    for hub in hubs
    if len(hub["streams"]) >= 2
}

print(hub_load)