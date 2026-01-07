# a list of dictionary
students =[
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
] # do not forget the comma.
for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ",")


# from this codes, we know the purpose of list is for storage, the dictionary is for query and quicly extract the related information from the database.
