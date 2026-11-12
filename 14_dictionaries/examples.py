student = {"name": "Kiran", "age": 19, "grade": "A"}
print(student["name"])

student["age"] = 20
student["city"] = "Madurai"
print(student)

for key, value in student.items():
    print(key, "->", value)
