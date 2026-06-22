import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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