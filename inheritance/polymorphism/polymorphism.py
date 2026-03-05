class Bird:
   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class Sparrow(Bird):
   
    def flight(self):
        print("Sparrows can fly.")
 
class Ostrich(Bird):
 
    def flight(self):
        print("Ostriches cannot fly.")
 
def try_flying(bird: Bird): # the function shows polymorphism.
    bird.flight()  


if __name__ == '__main__':
    obj_bird = Bird()
    obj_spr = Sparrow()
    obj_ost = Ostrich()
    
    obj_bird.intro()
    try_flying(obj_bird)    
    obj_spr.intro()   
    try_flying(obj_spr)    
    obj_ost.intro()
    try_flying(obj_ost)    