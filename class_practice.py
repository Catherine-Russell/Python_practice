class Dog():
    def __init__(self, name, size, colour, fav_toy, bark):
        self.name = name
        self.size = size
        self.colour = colour
        self.fav_toy = fav_toy
        self.bark = bark

    def speak(self):
        print(self.bark)
    
    def fetch(self):
        print(f"{self.name} fetches {self.fav_toy}")

    def poop(self):
        print(f"Hope you brought bags! {self.name} does a {self.size} shit")
        res = None
        while res != True:
            pickup = input("Will you pick it up? (y/n): ")
            if pickup == "y":
                print("What a responsible dog owner")
                res = True
            elif pickup == "n":
                print(f"You are as disgusting as that {self.size} shit.")
                res = True
            else:
                res = False
            
dog1 = Dog("Yogi", "small", "black", "Basil the fox", "Yip! Yip!")
dog2 = Dog("Bobby", "medium", "black and white", "food", "Wuff Wuff")

dog1.speak()
dog1.fetch()
dog1.poop()
print("\n")
dog2.speak()
dog2.fetch()
dog2.poop()



class Person():
    def __init__(self, first_name, surname):
        # note that we're not using instance variables here
        self.first_name = first_name
        self.surname = surname
    def full_name(self):
        # will this work without using instance variables above?
        return f"{self.first_name} {self.surname}"

alan_turing = Person("Alan", "Turing")
print(alan_turing.full_name())
# what gets returned here?