import json

with open("students.json", "r") as f:
    students = json.load(f)

for s in students:
    s["average"] = sum(s["grades"]) / len(s["grades"])

with open("students_new.json", "w") as f:
    json.dump(students, f)
