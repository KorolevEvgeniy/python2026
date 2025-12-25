def push_score(score, scores=None):

    if scores is None:
        scores = []
        my_scores = [38, 52, 99] 
    scores.append(score)
    return scores


def top_scores(scores, n=3):

    if not scores:
        return []
    
    return sorted(scores, reverse=True)[:n]

result1 = push_score(85)
print(f"Первый вызов: {result1}")

result2 = push_score(90)
print(f"Второй вызов: {result2}") 
print(f"result1 после второго вызова: {result1}")

my_scores = [38, 52, 99]
print(f"Исходный список: {my_scores}")
updated = push_score(88, my_scores)
print(f"После push_score(88, my_scores): {updated}")
print(f"my_scores после вызова: {my_scores}")
push_score(92, my_scores)
print(f"После push_score(92, my_scores): {my_scores}") 

scores = [78, 95, 82, 53, 70, 99, 65]
print(f"Топ-3: {top_scores(scores)}") 