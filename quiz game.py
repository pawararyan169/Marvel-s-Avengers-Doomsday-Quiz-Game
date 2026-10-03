print("Welcome to the marvel quiz game!")

playing = input("Do you want to play? (yes/no) ") 

if playing != "yes":
    quit()

print("Okay! Let's test your knowledge about marvel movies!")

answers= input("What is the name of doctor doom's mother? ")
if answers.lower() == "cynthia von doom":
    print("You are correct!")
else:
    print("Incorrect! The correct answer is Cynthia Von Doom.")

answers= input("What is the name of the secret group of Reed Richards variants from different universes?" )
if answers.lower() == "the council of reeds":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answe is The Council of Reeds.")

answers= input("Which cosmic beings did Doctor Doom steal power from to create Battleworld in Secret Wars (2015)? ")
if answers.lower() == "The Beyonders":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answer is the Beyonders.")

answers= input("What title does Doctor Doom hold when he rules Battleworld in Secret Wars (2015)? ")
if answers.lower() == "God Emperor Doom":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answer is God Emperor Doom.")

answers= input("What is the name of the alternate universe where Doctor Doom rules as God Emperor Doom? ")
if answers.lower() == "BattleWorld":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answer is BattleWorld.")

answers= input("Which scientist's matter-manipulating powers are central to Doctor Doom's plan in the original Secret Wars (1984) storyline? ")
if answers.lower() == "molecule man":
    print("Yes! You are correct!")  
else:
    print("Incorrect! The correct answer is Molecule Man.")

answers= input(". What is the name of the Marvel comic event in which the multiverse collapses and Battleworld is created? ")
if answers.lower() == "secret wars":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answer is Secret Wars.")

answers= input("What is the name of the multiversal phenomenon in which two universes collide and threaten to destroy each other? ")
if answers.lower() =="incursion":
    print("Yes! You are correct!")
else:
    print("Incorrect! The correct answer is Incursion.")

answers = input("Which Fox X-Men movie features Wolverine travelling back in time to prevent a dystopian future? ")
if answers.lower() == "x-men: days of future past":
    print("Yes! You are correct!")  
else:
    print("Incorrect! The correct answer is X-Men: Days of Future Past.")