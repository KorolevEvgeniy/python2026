def push_score(score, scores=None):
    if scores == None:
        scores = []
    scores.append(score)
    return scores
print(push_score(""))
result1 = push_score(25)
print(f"Результат 1: {result1}")
result2 = push_score(53)
print(f"Результат 2: {result2}")
my_scores = [25, 50, 90]
print(f"Исходный список: {my_scores}")
result3 = push_score(95, my_scores)
print(f"Результат 3: {result3}")

scores = [1,23,25,58,86,100]
def top_scores(scores, n=3):
    return sorted(scores, reverse=True)[:n]

print(f"{top_scores(scores)}")
