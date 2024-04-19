#Description-  This is a simple example of how to handle exceptions in Python

student_records = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21}
]

for record in student_records:
    name = record["name"]
    grade = record["grade"] 
    print(f"{name}'s grade: {grade}")
