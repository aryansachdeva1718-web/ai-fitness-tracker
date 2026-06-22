from tracker import *
from recovery import *


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