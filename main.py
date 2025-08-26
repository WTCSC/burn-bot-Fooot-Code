from time import sleep

# Info about the person
name = input("Hey, what's your name?\n")
age = input("What about your age?\n")
while not age.isdigit():
    print("Danggg you can't even enter your age properly? Try again")
    age = input("What's your age?\n")
age = int(age)
sport = input("What's your favorite sport?\n").lower()

# Number handling
number = input("What's your favorite number?\n")
while not number.isdigit():
    print("Your answers already suck and now you can't type a number properly? Try again.")
    number = input("What's your favorite number?\n")
number = int(number)


# Name handling
myAge = 16
print(f"Your name starts with a {name[0].upper()} and ends with {name[-1].upper()}? Basic.")
sleep(3)

# Age handling
if age <= myAge:
    print("You're a youngin, lil bro missed everything")
else:
    print(f"Unc is {age}, were the dinosaurs scary?")
sleep(2)

# Favorite sport handling
if sport == "soccer":
    print("Soccer's a Tuff ahh sport")
elif sport == "football":
    print("Madden is better than actual football")
elif sport == "baseball":
    print("Baseball's equivalent to watching paint dry. Guess you have a lot of patience")
elif sport == "hockey":
    print("You like Hockey? Your'e better off watching wrestling at that point.")
else:
    print("Never heard of that sport.")
sleep(3)

# Favorite number handling 
if number != 67:
    print("Why is your favorite number not 67?")
else:
    print("W Favorite Number")