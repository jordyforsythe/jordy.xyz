# ============================================================
# Program 5: African Student Scores Analyser
# Uses a function that returns average, highest, and lowest
# scores via tuple unpacking.
# ============================================================

def analyse_scores(scores):
    """
    Analyse a list of student scores.

    Args:
        scores (list of float): The student scores.

    Returns:
        tuple: (average, highest, lowest)
    """
    if not scores:
        return (0, 0, 0)

    total   = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest  = min(scores)

    return (average, highest, lowest)


def get_grade(score):
    """Return a letter grade for a given score."""
    if score >= 75:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


# --- Dataset: Students from various African countries ---
students = [
    ("Amara Diallo",    "Senegal",      82),
    ("Chidi Okonkwo",   "Nigeria",      74),
    ("Fatima El-Amin",  "Sudan",        91),
    ("Kwame Asante",    "Ghana",        65),
    ("Lindiwe Dube",    "Zimbabwe",     58),
    ("Musa Kamara",     "Sierra Leone", 43),
    ("Nala Mensah",     "Ghana",        77),
    ("Omar Farouk",     "Egypt",        88),
    ("Priya Naidoo",    "South Africa", 69),
    ("Zawadi Ochieng",  "Kenya",        95),
]

scores_only = [score for _, _, score in students]

# --- Tuple unpacking from the function ---
average, highest, lowest = analyse_scores(scores_only)

print("=" * 60)
print("      AFRICAN STUDENT SCORES ANALYSER")
print("=" * 60)
print(f"\n{'Name':<22} {'Country':<16} {'Score':>6}  {'Grade'}")
print("─" * 60)

for name, country, score in students:
    grade = get_grade(score)
    marker = " ⭐" if score == highest else (" ⚠️" if score == lowest else "")
    print(f"{name:<22} {country:<16} {score:>6}   {grade}{marker}")

print("=" * 60)
print(f"\n📊 Class Statistics:")
print(f"   Average Score : {average:.2f}  (Grade: {get_grade(average)})")
print(f"   Highest Score : {highest}       ⭐ Top performer")
print(f"   Lowest Score  : {lowest}       ⚠️  Needs support")
print(f"   Total Students: {len(scores_only)}")
print("=" * 60)
