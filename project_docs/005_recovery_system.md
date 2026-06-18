# Recovery System Design

Goal:

Create a recovery score from 0–100 after each workout session.

The score estimates how recovered the user is.

---

## Inputs Used

1. Sleep
2. Calories
3. Bodyweight
4. Workout Volume

---

## Why These Inputs?

### Sleep

Most important recovery factor.

Weightage increased because personal experience shows sleep affects recovery significantly.

### Calories

Calorie intake should be relative to bodyweight instead of fixed value.

Different users have different maintenance calories.

### Workout Volume

Higher training volume means higher fatigue accumulation.

---

## Weight Distribution

Sleep → 50 points

Calories → 30 points

Workout Fatigue → 20 points

Total → 100 points

## Sleep Scoring

8+ hrs → 50

7–8 hrs → 40

6–7 hrs → 28

5–6 hrs → 15

<5 hrs → 5

---

## Calories Scoring

Maintenance Calories = Bodyweight × 33

100% maintenance → 30

90% maintenance → 24

80% maintenance → 18

70% maintenance → 10

<70% maintenance → 5

---

## Workout Fatigue Scoring

Volume <3000 → 20

3000–5000 → 15

5000–7000 → 8

7000+ → 4

## Special Case

If no workout is logged for the day:

Treat it as Rest Day.

Fatigue Score automatically becomes maximum.

Reason:

No training fatigue accumulated.

---

Example:

Sleep = 40

Calories = 25

Fatigue = 20

Final Score = 85/100

## Architecture Decision

Recovery score will NOT be added inside workout_summary().

Reason:

Single Responsibility Principle

workout_summary()

Purpose:

- total sets
- total volume
- heaviest lift
- exercise count

recovery_score()

Purpose:

- calculate user recovery state

Keeping functions separate improves code organization.

## Planned Function Structure

sleep_score(sleep)

Purpose:

Calculate sleep score

Returns integer score

---

calorie_score(calories, bodyweight)

Purpose:

Compare calories against maintenance calories

Returns integer score

---

fatigue_score(volume)

Purpose:

Determine fatigue score from workout volume

Returns integer score

---

recovery_score(date)

Purpose:

Main function

Tasks:

- fetch daily data
- fetch workout data
- call scoring functions
- calculate total score
- print recommendations