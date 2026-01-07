def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's Castle this evening, 7:00 PM.set.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

items = {"Mario":"Princess Peach", 
         "Luigi": "Princess Peach", 
         "Daisy": "Princess Peach", 
         "Yoshi": "Princess Peach"}

for i in items:
    print(write_letter(i, items[i]))