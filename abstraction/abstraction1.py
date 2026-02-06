# the abstract method is aim to define a blueprint or API, people can utlize it to build multiple implementations.
from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def execute(self):
        pass

