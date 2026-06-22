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


#----------DAILY METRICS FUNCTION----------
def log_daily_metrics():

    daily_df = load_daily_data()
    print("\n--- DAILY METRICS ---")

    date = get_date()
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

#----------WORKOUT INPUT FUNCTION----------
def log_workout():
    print("\n--- WORKOUT LOGGING ---")

    workout_df = load_workout_data()
    date = get_date()

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
    return date

#----------ANALYTICS & GRAPHS----------
def workout_summary(date):
    workout_df = load_workout_data()
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
    workout_df = load_workout_data()
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

#Calorie Trend
def calorie_trend(date):
    daily_df = load_daily_data()
    today_data = daily_df[daily_df["Date"] == date]
    calories = today_data["Calories"].iloc[0]

    history_data = daily_df[daily_df["Date"] != date]
    if len(history_data) < 3:
        print("\nNot enough history for calorie trend analysis.")
        return
    recent_data = history_data.tail(3)
    avg_calories = recent_data["Calories"].mean()

    if calories > avg_calories * 1.20:
        print("\nCalorie intake is significantly higher than your recent average.")
    elif calories < avg_calories * 0.80:
        print("\nCalorie intake is significantly lower than your recent average.")
    else:
        print("\nCalorie intake is consistent with your recent average.")

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
    
    
#----------FUNCTION CALLS----------
def main():

    while True:

        print("\n----- Fitness Tracker -----")
        print("1. Log Daily Metrics")
        print("2. Log Workout Session")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            log_daily_metrics()


        elif choice == "2":
            date = log_workout()
            score = recovery_score(date)

            if score is not None:
                print(f"\nRecovery Score: {score:.2f}/100")
                interpret_score(score)
                calorie_trend(date)


        elif choice == "3":
            break

main()
