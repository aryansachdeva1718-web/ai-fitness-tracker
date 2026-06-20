# June 18

Worked On

- Recovery score system design

Learned

- Product prioritization
- Function decomposition
- Handling edge cases
- Recovery score heuristics
- Architecture planning before coding

Important Realization

Not every intelligent feature needs Machine Learning.

Rule-based systems can create useful software.

Decision Taken

Will postpone scikit-learn.

Will focus on building intelligent logic first.


# June 19

## Focus: Recovery System Architecture

### Key Learnings

**1. Fixed thresholds are unreliable**

Using static volume thresholds (like 7000+ = high fatigue) does not work because every user has different training capacity.

---

**2. Relative scoring is better**

Instead of fixed thresholds:

volume_ratio = today_volume / avg_volume

This makes fatigue scoring personalized.

---

**3. Historical data selection matters**

Decided to use **last 10 workout sessions**.

Reason:

- 5 sessions too noisy  
- 15 sessions may include outdated strength levels  

---

**4. Edge cases affect architecture**

Today’s workout should not affect historical average.

Solution:

Pass current date into `get_avg_volume()` and exclude it from calculation.

---

**5. Never fake missing data**

If user has fewer than 10 workout sessions:

- Skip fatigue scoring  
- Scale remaining score to 100  

Better than inventing fake values.

---

**6. Product scope should stay realistic**

Considered tracking sleep quality.

Rejected because project cannot realistically measure sleep cycles or interruptions.

Sleep duration only.

---

**7. Added future feedback system idea**

User can optionally log recovery feedback.

Example:

- Felt weak  
- Low energy  
- Still sore  

Can help compare prediction vs actual experience.

---

## Biggest Takeaway

Today reinforced that building projects is not just writing code.

Good code solves problems.

Good architecture handles real-world edge cases.

# June 20

Built complete recovery scoring subsystem.

Implemented:
- fatigue_score() based on workout volume vs historical average
- sleep_score() using sleep duration thresholds
- calorie_score() using bodyweight-based maintenance calories (33x multiplier)
- recovery_score() combining all recovery parameters
- interpret_score() for recovery feedback

Key learning:
- Learned how to combine multiple scoring systems into one analytics pipeline
- Improved pandas filtering and validation handling using .empty and .iloc
- Understood importance of handling missing data instead of forcing calculations