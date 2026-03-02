from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod
    def spawn(self):
        print("System: Spawning...") # Actual logic exists!

class Warrior(Character):
    def spawn(self):
        super().spawn() # You use this to get the "System: Spawning..." print (it depends on whether u wanna execute the spawn function.)
        print("Equipping Sword.")

# character = Character()  # This would still throw an error (TypeError)
hero = Warrior()
hero.spawn()