class Sandwich(object):
    def _init_(self,owner, bread="white"):
        self.owner = owner
        self.bread = bread
        self.toppings = []


mine = Sandwich("Dusty")