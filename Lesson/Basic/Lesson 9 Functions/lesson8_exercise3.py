def score_grade(score):
    if score >= 80: return "A"
    elif score >= 70: return "B"
    elif score >= 60: return "C"
    elif score >= 50: return "D"
    else: return "E"

for s in [95, 82, 71, 63, 40]:
    print(s, "->", score_grade(s))