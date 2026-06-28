from muscle_history import days_since_last_trained

def recommend_next_workout():
    muscle_days = days_since_last_trained()
    priority_scores = {}
    
    #.items() = give me both key + value
    for muscle, days in muscle_days.items():
        score = days * 2
        priority_scores[muscle] = score

        #DO NOT compare keys, compare values using .get()
        best_muscle = max(priority_scores, key=priority_scores.get)

    sorted_scores = dict(sorted(priority_scores.items(), key=lambda x: x[1], reverse=True))
    return sorted_scores