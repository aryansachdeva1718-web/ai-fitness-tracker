import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

daily_metrics_file = "daily_metrics.csv"
workout_sets_file = "workout_sets.csv"

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

def get_date():
    return input("\nEnter date (DD/MM/YYYY): ")
def load_daily_data():
    return pd.read_csv(daily_metrics_file)
def load_workout_data():
    return pd.read_csv(workout_sets_file)
daily_df = load_daily_data()
workout_df = load_workout_data()