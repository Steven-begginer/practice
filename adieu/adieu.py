import inflect
p = inflect.engine()
ini_list = ["Adieu", "adieu"]
# add new name into list
try:
    while True:
        name = input("Name: ")
        if name == "Liesl":
            ini_list.append("to Liesl")
        elif "to Liesl" in ini_list and name not in ini_list:
            ini_list.append(name)
# print the definite whole name 
except EOFError:
    if len(ini_list) == 2:
        print(", ".join(ini_list))
    elif "to Liesl" in ini_list and len(ini_list) == 3:
        print(", ".join(ini_list))
    else:
        result = p.join(ini_list)
        print(result)