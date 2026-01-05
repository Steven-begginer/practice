x = str(input(""))
# replace the space with "..."
y = []
for i in range(len(x)):
    if x[i] == " ":
        y.append("...")
    else:
        y.append(x[i])
print(''.join(y)) # join() function: concatenated into string and delete quotes. 
