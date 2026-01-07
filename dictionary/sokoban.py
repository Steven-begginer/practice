history = []
while True:
    action = input("Action: ")
    if action == "Undo":
        Undone = history.pop()
        print(f"Undone: {Undone}")
    else:
        history.append(action) # remember that it represent the string value now.
    print(history) # remember that whatever "for", "while", "if", "else", their exit indentation is the same as themselves.(the question is for "if" and "else".)
# there are the implementation of list.