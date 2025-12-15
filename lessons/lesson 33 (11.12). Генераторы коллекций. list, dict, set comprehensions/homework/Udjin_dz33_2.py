tracks = [("UNNQ", "Pulse"), ("Horizon", "Flight")]
plays = [("Pulse", 95), ("Flight", 110)]

result = [
    f"{artist} — {track} ({count} прослушиваний)"
    for artist, track in tracks
    for name, count in plays if name == track
    if count > (sum(c for _, c in plays) / len(plays) if plays else 0)
]

print(result)