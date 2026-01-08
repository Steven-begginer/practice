# buid a trigger for watering the plant immediately.
import random
moisture = random.randint(1, 100)
Day = 0
print(f"Day {Day}: moisture: {moisture}%")
while moisture > 20:
    moisture = random.randint(1,100)
    Day += 1
    print(f"Day {Day}: moisture: {moisture}%")

print("Time to water!")