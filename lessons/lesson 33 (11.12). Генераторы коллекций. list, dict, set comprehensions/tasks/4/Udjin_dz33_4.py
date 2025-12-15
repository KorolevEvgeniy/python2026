tracks = [
    {"title": "Airwaves", "tags": ["synth", "ambient"], "released": 2019},
    {"title": "Dust", "tags": ["ambient", "cinematic"], "released": 2021},
    {"title": "Retro", "tags": ["synth", "pop"], "released": 2016}
]

counter = {}
for track in tracks:
    if track["released"] > 2018:
        for tag in track["tags"]:
            counter[tag] = counter.get(tag, 0) + 1

focus_tags = {tag for tag, count in counter.items() if count >= 2}

print(focus_tags)  