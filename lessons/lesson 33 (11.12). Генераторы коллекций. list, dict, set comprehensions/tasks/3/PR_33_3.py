hubs = [
    {
        "name": "DevHub",
        "capacity": 200,
        "streams": [
            {"title": "Python", "viewers": 120},
            {"title": "Go", "viewers": 80}
        ]
    },
    {
        "name": "DataHub",
        "capacity": 150,
        "streams": [
            {"title": "ML", "viewers": 90}
        ]
    },
    {
        "name": "AsyncHub",
        "capacity": 180,
        "streams": [
            {"title": "Asyncio", "viewers": 130},
            {"title": "Trio", "viewers": 100},
            {"title": "AnyIO", "viewers": 70}
        ]
    }
]
result = {
    hub["name"]: round(
        sum(stream["viewers"] for
    stream in hub["streams"]) /
        len(hub["streams"])/
        hub["capacity"],1
        )
    for hub in hubs
    if len(hub.get("streams", [])) >= 2
}
print(result)
