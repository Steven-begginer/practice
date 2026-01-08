name = input("camelCase: ")
rename = []
for i in range(len(name)):
    if 'A' <= name[i] <= 'Z':
        rename.append("_" + name[i].lower())
    else:
        rename.append(name[i])
print(f"snake_name : {''.join(rename)}")
        