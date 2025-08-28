from time import sleep

# Info about the person
name = input("Hey, what's your name?\n")
age = input("What about your age?\n")
while not age.isdigit(): # avoid error, but mostly insult person
    print("Danggg you can't even enter your age properly? Try again")
    age = input("What's your age?\n")
age = int(age)
sport = input("What's your favorite sport?\n").lower()
number = input("What's your favorite number?\n")
while not number.isdigit(): # avoid error, and insult person
    print("Your answers already suck and now you can't type a number properly? Try again.")
    number = input("What's your favorite number?\n")
number = int(number)
color = input("What's your favorite color?\n")
gatorade = input("What is your favorite Gatorade?\n")

# Name handling
myAge = 16
print(f"Your name starts with a {name[0].upper()} and ends with {name[-1].upper()}? Basic.")
sleep(3)

# Age handling
if age <= myAge:
    print("You're a youngin, lil bro missed everything")
else:
    print(f"Unc is {age}, were the dinosaurs scary?")
sleep(3)

# Favorite sport handling
if sport == "soccer":
    print("Soccer's a Tuff ahh sport")
elif sport == "football":
    print("Madden is better than actual football")
elif sport == "baseball":
    print("Baseball's equivalent to watching paint dry. Guess you have a lot of patience")
elif sport == "hockey":
    print("You like Hockey? You're better off watching wrestling at that point.")
else:
    print("Never heard of that sport.")
sleep(3)

# Favorite number handling 
if number != 67:
    print("Why is your favorite number not 67?")
else:
    print("W Favorite Number")

sleep(3)

# Color handling
if color.lower() == "green":
    print("Oh I wonder why? It's not like trees, grass, bushes, and just about everything around us is green.")
elif color.lower() == "blue":
    print("Common ahh color to like.")
elif color.lower() == "orange":
    print("Blue is better")
else:
    print("L color.")
sleep(3)

# Gatorade handling
gatoradeColors = [
    "red",
    "orange",
    "yellow",
    "blue",
    "purple",
    "light blue",
    "green"
]

if gatorade.lower() in gatoradeColors:
    print("Good Boy.")
else:
    print("Cringe ahh for saying the flavor of Gatorade instead of the color.")
sleep(3)





# Fun Art
print(r"""
$$\              $$$$$$\                                                                  
$$ |            $$  __$$\                                                                 
$$ |            $$ /  $$ |$$$$$$$\   $$$$$$$\ $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$\ 
$$ |            $$$$$$$$ |$$  __$$\ $$  _____|$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  _____|
$$ |            $$  __$$ |$$ |  $$ |\$$$$$$\  $$ | $$ | $$ |$$$$$$$$ |$$ |  \__|\$$$$$$\  
$$ |            $$ |  $$ |$$ |  $$ | \____$$\ $$ | $$ | $$ |$$   ____|$$ |       \____$$\ 
$$$$$$$$\       $$ |  $$ |$$ |  $$ |$$$$$$$  |\$$$$$\$$$$  |\$$$$$$$\ $$ |      $$$$$$$  |
\________|      \__|  \__|\__|  \__|\_______/  \_____\____/  \_______|\__|      \_______/                                                      
""")
sleep(2)
print(r"""
  o   \o      
 <|>   v\     
 < >    <\    
          \o  
           |> 
          //  
  o     o/    
 <|>   /v     
 < >  />             
""")