import pandas as pd
from exercise_database import exercise_database
from helpers import workout_sets_file

def get_last_trained_muscles():
    workout_df = pd.read_csv(workout_sets_file)
    muscle_history = {}

    for _, row in workout_df.iterrows():
        exercise = row["Exercise"]
        date = row["Date"]

        if exercise in exercise_database:
            primary = exercise_database[exercise]["primary"]
            secondary = exercise_database[exercise]["secondary"]
            all_muscles = primary + secondary

            for muscle in all_muscles:
                if muscle not in muscle_history:
                    muscle_history[muscle] = date
                elif date > muscle_history[muscle]:
                    muscle_history[muscle] = date
                
    return muscle_history
                

    

    

    
    