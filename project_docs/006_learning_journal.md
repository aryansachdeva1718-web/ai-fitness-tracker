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

**1. Personalized scoring > fixed thresholds**  
Static fatigue thresholds don’t work. Using volume ratio (`today_volume / avg_volume`) makes scoring user-specific.

**2. Historical data matters**  
Chose last **10 workout sessions** — enough data without including outdated performance.

**3. Edge cases shape design**  
Excluded current date from average volume calculation to avoid skewed recovery scores.

**4. Missing data should not be faked**  
If workout history is insufficient, skip fatigue score and scale remaining score instead.

**5. Scope discipline matters**  
Dropped sleep quality tracking since accurate monitoring is unrealistic for current project scope.

### Biggest Takeaway

Building projects is not just coding.

Good architecture means handling real-world edge cases before they become bugs.

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

# June 22

## Focus: Calorie Trend Analysis & Code Refactoring

### Key Learnings

**1. Trends are better than isolated values**  
Single day calorie intake means little without comparing recent eating patterns.

**2. Recent data > entire history**  
Used last 3 entries instead of full history to reflect current eating habits.

**3. Relative comparison improves analysis**  
Used percentage-based thresholds (±20%) instead of fixed calorie differences.

**4. Handle insufficient history**  
If fewer than 3 past entries exist, skip analysis instead of forcing output.

**5. Large files become hard to manage**  
362 lines in a single file made future scaling difficult.

**6. Code should be split by responsibility**  
Separated project into tracker, recovery, helpers, and main modules.

**7. Testing after every change is critical**  
Verified imports and functionality after each file split.

### Biggest Takeaway

Analytics become more meaningful when current data is compared against user history rather than viewed independently.

Organizing code into maintainable architecture is also important.

# June 26

## Focus: Workout Recommendation Engine Architecture

### Key Learnings

**1. Exercise-level data is important**

Built an exercise database mapping each exercise to primary and secondary muscles.

---

**2. Recommendation logic needs muscle tracking**

The system must know which muscles were trained before suggesting the next workout.

---

**3. Compound vs isolation exercises differ**

Compound lifts affect multiple muscles, while isolation movements may have little or no secondary involvement.

---

## Biggest Takeaway

Smart systems are built on well-structured logic before adding machine learning.