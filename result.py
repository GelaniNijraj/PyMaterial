__author__ = 'root'

credits = {"TOM": 4, "TOOL": 4, "PP": 4, "CP": 3, "CAD": 2, "MnI": 4}
grades = {"A+": 10, "A": 9, "B+": 8, "B": 7, "C+": 6, "C": 5}
possibilities = [
                    {"TOM": "A+", "TOOL": "A", "PP": "A+", "CP": "A+", "CAD": "B", "MnI": "A+"},
                    {"TOM": "A+", "TOOL": "A+", "PP": "A+", "CP": "A+", "CAD": "B", "MnI": "A+"},
                    {"TOM": "A+", "TOOL": "A+", "PP": "A+", "CP": "A+", "CAD": "B+", "MnI": "A+"},
                    {"TOM": "A+", "TOOL": "A", "PP": "A+", "CP": "A+", "CAD": "B+", "MnI": "A+"},
                    {"TOM": "A+", "TOOL": "A", "PP": "A+", "CP": "A+", "CAD": "C", "MnI": "A+"}
]
for p in possibilities:
    score = 0
    for subject, grade in p.items():
        score += grades[grade]*credits[subject]
    score /= sum(credits.values())
    print(p, score)