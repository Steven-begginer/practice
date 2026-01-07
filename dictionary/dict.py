students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep = ",") # student is key and students[student] = value. They are totally different from the list data structure.
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# we can think of the dictionary like the excel format or database.
"""
|   Hermione   |    Harry    |    Ron     |    Draco    | -- indices/columns/keys
    Gryffindor    Gryffindor    Gryffindor    Slytherin   -- values
"""

