contacts = {
    "number":4,
    "students":
    [
        {"name":"Test1","email":"Test1@test.com"},
        {"name":"Test2","email":"Test2@test.com"},
        {"name":"Test3","email":"Test3@test.com"},
        {"name":"Test4","email":"Test4@test.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])