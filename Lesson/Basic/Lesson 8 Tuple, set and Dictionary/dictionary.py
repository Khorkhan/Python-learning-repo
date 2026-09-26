student = {"name": "Alex", "age": 20, "gpa": 3.75}

print(student["name"])
print(student.get("email"))
print(student.get("email", "Do data"))

student["email"] = "alex@gmail.com"
student["gpa"] = 3.80
del student["age"]

for key, value in student.items():
    print(key, "->", value)