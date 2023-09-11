# Robofriend Cafe!

def start_play(visitor, friend):
    print("   One moment please\n    ... \n    ... \n    ...\n")
    friend.greet_visiter(visitor)
    friend.introduce_self()
    friend.share_likes()
    print("Let's play!")

def new_design():
    print("    Initiating Robofriend Creation Service... \n    ... \n    Please input your design choices below:")
    name = input("Name: ")
    colour = input("Colour: ")
    weight = input("Weight in Kg: ")
    greeting = input("Favoured greeting: ")
    likes = input("Likes: ")
    return Robofriend(name, colour, weight, greeting, likes)

class Robofriend():
    def __init__(self, name, colour, weight, greeting, likes):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.greeting = greeting
        self.likes = likes
    
    def greet_visiter(self, visitor):
        print("Beep Boop!\n" + self.greeting + " " + visitor + "!")
        
    def introduce_self(self):
        print(f"I am a {self.colour} robot called {self.name} and I weigh {self.weight}Kg.")
    
    def share_likes(self):
        print("I like " + self.likes + "!")

# Robofriend menu
r1 = Robofriend("Benji", "red", 43, "Heyyy", "puppies")
r2 = Robofriend("George", "blue", 37, "Salutations", "world domination")
r3 = Robofriend("Fiona", "green", 32, "Well, hello there", "sushi")

Robot_dict = {
    "r1" : r1,
    "r2" : r2,
    "r3" : r3
}

# A new customer arrives
print("Welcome to Robofriend Cafe, where coffee comes in cups and friends come in 1s and 0s!")
visitor = input("What's your name? ")
choice = input("Which Robofriend would you like to play with? (Write r and a number)")
if choice in Robot_dict:
    friend = Robot_dict.get(choice)
    start_play(visitor, friend)
else:
    print("Sorry, we have no Robofriends with that reference number. Please design your own!")
    r4 = new_design()
    start_play(visitor, r4)




