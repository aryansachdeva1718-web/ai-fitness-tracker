import pandas as pd
import matplotlib.pyplot as plt
from helpers import *

#----------RECOVERY SYSTEM----------
#Average volume over last 10 sessions
def get_avg_volume(exclude_date):

    workout_df = load_workout_data()

    # We don't want current workout affecting historical average
    workout_df = workout_df[workout_df["Date"] != exclude_date]

    # create volume column for each set
    workout_df["Volume"] = workout_df["Reps"] * workout_df["Weight"]

    daily_volume = workout_df.groupby("Date")["Volume"].sum()
    recent_sessions = daily_volume.tail(10)

    # if insufficient history
    if len(recent_sessions) < 10:
        return None

    avg_volume = recent_sessions.mean()
    return avg_volume

#Today Volume
def get_today_volume(date):

    workout_df = load_workout_data()

    today_workout = workout_df[workout_df["Date"] == date]
    today_workout["Volume"] = (today_workout["Reps"] * today_workout["Weight"])

    total_volume = today_workout["Volume"].sum()

    return total_volume

#Fatigue Score
def fatigue_score(today_volume, avg_volume):

    ratio = today_volume / avg_volume

    if ratio <= 1.0:
        score = 20
    elif ratio <= 1.2:
        score = 16
    elif ratio <= 1.4:
        score = 12
    elif ratio <= 1.7:
        score = 7
    else:
        score = 3
    return score

#Sleep Score
def sleep_score(sleep_hours):

    if sleep_hours >= 8:
        score = 50
    elif sleep_hours >= 7:
        score = 42
    elif sleep_hours >= 6:
        score = 35
    elif sleep_hours >= 5:
        score = 20
    else:
        score = 10
    return score

#Calorie Score
def calorie_score(calories, bodyweight):
    
    maintenance = bodyweight * 33
    ratio = calories / maintenance

    if ratio >= 0.95:
        score = 30
    elif ratio >= 0.85:
        score = 25
    elif ratio >= 0.75:
        score = 18
    elif ratio >= 0.60:
        score = 10
    else:
        score = 5
    return score
 
#Recovery Score
def recovery_score(date):
    daily_df = load_daily_data()
    today_data = daily_df[daily_df["Date"] == date]

    if today_data.empty:
        print("\nDaily metrics not found for today.")
        print("Please log sleep, calories and bodyweight first.")
        return None

    sleep_hours = today_data["Sleep"].iloc[0]
    calories = today_data["Calories"].iloc[0]
    bodyweight = today_data["Bodyweight"].iloc[0]

    sleep_points = sleep_score(sleep_hours)
    calorie_points = calorie_score(calories, bodyweight)

    today_volume = get_today_volume(date)
    avg_volume = get_avg_volume(date)
    
    if avg_volume is not None:

        fatigue_points = fatigue_score(today_volume, avg_volume)
        total_score = ( sleep_points + calorie_points + fatigue_points)
    
    else:
        print("\nNote: Limited workout history detected.")
        print("Recovery score calculated without fatigue analysis.")

        total_score = sleep_points + calorie_points
        total_score = (total_score / 80) * 100
    return total_score

#Interpret Score
def interpret_score(score):

    if score >= 85:
        print("\nRecovery Status: Excellent")
        print("You are well recovered and ready for hard training.")

    elif score >= 70:
        print("\nRecovery Status: Good")
        print("Recovery looks good. Performance should be solid.")

    elif score >= 55:
        print("\nRecovery Status: Moderate")
        print("Recovery is decent. Avoid pushing to absolute limits.")

    elif score >= 40:
        print("\nRecovery Status: Poor")
        print("Recovery is lower than ideal. Consider lighter training.")

    else:
        print("\nRecovery Status: Very Poor")
        print("Sleep, nutrition or fatigue may be limiting recovery today.")