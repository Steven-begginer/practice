dic = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
keys = []
total = 0
for k in dic:
    keys.append(k)
while True:
    try:
        Item = input("Item: ")
        if Item in keys:
            total = total + dic[Item]
            print(f"Total: ${total}")
    except EOFError:
        print("Item: ")  # Print a newline to move the cursor
        break
    except KeyError:
        pass

        
