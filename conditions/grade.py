score = int(input("score: "))

if score >= 80 and score <= 100:
    print("HD")
elif score >= 70 and score < 80:
    print("D")
elif score >= 60 and score < 70:
    print("C")
elif score >=50 and score < 60:
    print("P")
else:
    print("Fail")
