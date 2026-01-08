Input = input("Input: ")
list = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
for i in Input:
    for j in range(len(list)):
        if i == list[j]:
            Input.translate(i)
print(f"Output: ")
