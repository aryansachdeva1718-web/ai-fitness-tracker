import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from exercise_database import exercise_database

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

daily_metrics_file = os.path.join(BASE_DIR, "data", "daily_metrics.csv")
workout_sets_file = os.path.join(BASE_DIR, "data", "workout_sets.csv")

if not Path(daily_metrics_file).exists():

    daily_df = pd.DataFrame(columns=[
        "Date",
        "Sleep",
        "Calories",
        "Bodyweight"
    ])

    daily_df.to_csv(daily_metrics_file, index=False)

if not Path(workout_sets_file).exists():

    workout_df = pd.DataFrame(columns=[
        "Date",
        "Exercise",
        "Set",
        "Reps",
        "Weight"
    ])

    workout_df.to_csv(workout_sets_file, index=False)

from datetime import date

def get_date():
    return str(date.today())

def load_daily_data():
    return pd.read_csv(daily_metrics_file)
def load_workout_data():
    return pd.read_csv(workout_sets_file)
daily_df = load_daily_data()
workout_df = load_workout_data()

def select_exercise():

    exercises = list(exercise_database.keys())

    print("\nSelect Exercise:")

    for i, exercise in enumerate(exercises, start=1):

        print(f"{i}. {exercise}")

    choice = int(input("Enter choice: "))

    return exercises[choice - 1]