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

daily_df = pd.read_csv(daily_metrics_file)
workout_df = pd.read_csv(workout_sets_file)

# DAILY METRICS FUNCTION
def log_daily_metrics():

    daily_df= pd.read_csv(daily_metrics_file)
    print("\n--- DAILY METRICS ---")

    date = input("Enter date (YYYY-MM-DD): ")
    sleep = float(input("Enter sleep hours: "))
    calories = int(input("Enter calories: "))
    bodyweight = float(input("Enter bodyweight: "))



    new_daily_entry = {
        "Date": date,
        "Sleep": sleep,
        "Calories": calories,
        "Bodyweight": bodyweight
    }

    daily_df = pd.concat([daily_df, pd.DataFrame([new_daily_entry])],
    ignore_index=True)

    daily_df.to_csv(daily_metrics_file, index=False)

    print(daily_df.tail())

# WORKOUT INPUT FUNCTION
def log_workout():
    print("\n--- WORKOUT LOGGING ---")

    workout_df = pd.read_csv(workout_sets_file)
    date = input("Enter date (YYYY-MM-DD): ")

    while True:
        
        exercise = input("\nEnter exercise name: ").strip().title()
        set_number = int(input("Enter total sets: "))
        
        for i in range(set_number):
            print(f"\nSet {i+1}")

            reps = int(input("Enter reps: "))
            weight = float(input("Enter weight: "))

            exercise_history = workout_df[workout_df["Exercise"] == exercise]

            if exercise_history.empty:
                print("First time doing this exercise")
            else:
                max_weight = exercise_history["Weight"].max()
                if weight > max_weight:
                     print(f"New {exercise} PR: Previous {max_weight} kg -> Current {weight} kg ")

            new_workout_entry = {
                "Date": date,
                "Exercise": exercise,
                "Set": set_number,
                "Reps": reps,
                "Weight": weight
            }

            workout_df = pd.concat( [workout_df, pd.DataFrame([new_workout_entry])],
            ignore_index=True)

        another = input("Add another exercise? (y/n): ")

        if another.lower() != "y":
            break
    
    workout_df.to_csv(workout_sets_file, index=False)
    workout_summary(date) 
    choice = input("\nDo you want to see progress graphs? (y/n): ")

    if choice.lower() in ["y", "yes"]:
        plot_progress(date) 

    print("\nWorkout saved successfully.\n")
    print(workout_df.tail(10))

#Analytics Functions
def workout_summary(date):
    workout_df = pd.read_csv(workout_sets_file)
    today_data = workout_df[workout_df["Date"] == date]

    total_sets = len(today_data)
    exercise_count = today_data["Exercise"].nunique()
    today_data["Volume"] = (today_data["Weight"] * today_data["Reps"])
    total_volume = today_data["Volume"].sum()

    heaviest_row = today_data.loc[today_data["Weight"].idxmax()]
    heaviest_exercise = heaviest_row["Exercise"]
    heaviest_weight = heaviest_row["Weight"]

    print("\n")
    print("==============================")
    print("      WORKOUT SUMMARY")
    print("==============================")
    print(f"\nExercises Performed: {exercise_count}")
    print(f"Total Sets Done: {total_sets}")
    print(f"Total Volume: {total_volume} kg")
    print(f"Heaviest Lift: {heaviest_exercise} ({heaviest_weight} kg) ")
    print("\nWorkout completed successfully.\n")

def plot_progress(date):
    workout_df = pd.read_csv(workout_sets_file)
    today_data = workout_df[workout_df["Date"] == date]

    today_exercises = today_data["Exercise"].unique()

    for exercise in today_exercises:
        exercise_data = workout_df[workout_df["Exercise"] == exercise]

    progress = exercise_data.groupby("Date")["Weight"].max()

    plt.figure()
    plt.plot(progress.index,progress.values,marker="o")
    plt.title(f"{exercise} Progress")
    plt.xlabel("Date")
    plt.ylabel("Max Weight (kg)")
    # Rotate dates so they don't overlap
    plt.xticks(rotation=45)
     # Adds grid lines
    plt.grid()
    # Prevent cutting labels
    plt.tight_layout()
    plt.show()
#Recovery System

def get_avg_volume(exclude_date):

    workout_df = pd.read_csv(workout_sets_file)

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


#FUNCTION CALLS

def main():
    daily_df = pd.read_csv("daily_metrics.csv")

    workout_df = pd.read_csv("workout_sets.csv")

    log_daily_metrics()

    log_workout()

main()
