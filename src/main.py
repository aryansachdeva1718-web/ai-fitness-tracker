from tracker import *
from recovery import *
from recommendation_engine import recommend_next_workout


def main():

    while True:

        print("\n----- Fitness Tracker -----")
        print("1. Log Daily Metrics")
        print("2. Log Workout Session")
        print("3. Get Workout Recommendation")
        print("4. Exit")

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
                consistency_tracker(date)

        elif choice == "3":
            recommendation = recommend_next_workout()
            print("\n----- Workout Recommendation -----")

            if recommendation["training_focus"] == "neglected_muscle":
                print("Priority Muscle To Train:")
                print(", ".join(recommendation["muscles"]))

            else: 
                print("Recommended Muscle Priority:")
                for muscle, score in recommendation["recommendations"].items():
                    print(f"{muscle}: {score} points")


        elif choice == "4":
            break

        else:
            print("Invalid Choice")

main()