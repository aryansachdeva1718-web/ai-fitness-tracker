import pandas as pd
from exercise_database import exercise_database
from helpers import workout_sets_file
from datetime import datetime

def get_last_trained_muscles():
    workout_df = pd.read_csv(workout_sets_file)
    muscle_history = {}

    for _, row in workout_df.iterrows():
        exercise = row["Exercise"]
        date = row["Date"]

        if exercise in exercise_database:
            primary = exercise_database[exercise]["primary"]
            secondary = exercise_database[exercise]["secondary"]
            
            for muscle in primary:
                if muscle not in muscle_history:
                    muscle_history[muscle] = {"last_primary": None,"last_secondary": None}
                if muscle_history[muscle]["last_primary"] is None or date > muscle_history[muscle]["last_primary"]:
                    muscle_history[muscle]["last_primary"] = date


            for muscle in secondary:
                if muscle not in muscle_history:
                    muscle_history[muscle] = {"last_primary": None,"last_secondary": None}
                if muscle_history[muscle]["last_secondary"] is None or date > muscle_history[muscle]["last_secondary"]:
                    muscle_history[muscle]["last_secondary"] = date
                
    return muscle_history

def days_since_last_trained():
    muscle_history = get_last_trained_muscles()
    days_since = {}

    today = datetime.today()

    for muscle, info in muscle_history.items():
        primary_days = None
        secondary_days = None

        if info["last_primary"] is not None:
            primary_days = datetime.strptime(info["last_primary"],"%Y-%m-%d")
            primary_difference = (today - primary_days).days
            primary_days = primary_difference
            
        if info["last_secondary"] is not None:
            secondary_days = datetime.strptime(info["last_secondary"],"%Y-%m-%d")
            secondary_difference = (today - secondary_days).days
            secondary_days = secondary_difference

        days_since[muscle] = {"primary_days": primary_days,"secondary_days": secondary_days}

    return days_since

                

    

    

    
    