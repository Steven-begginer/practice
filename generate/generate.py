"""
#import modules: including the whole functions together.
import random
coin = random.choice(["heads", "tails"])
print(coin)
"""
# from modules import specific function.
from random import choice
coin = choice(["heads", "tails"])
print(coin)