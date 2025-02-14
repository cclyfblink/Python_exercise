house = input("What house are you in? ").lower()

print("Your house colours are\n")
if house == "gryffindor":
    print("Scarlet and yellow")
elif house == "hufflepuff":
    print("Yellow and black")
elif house == "ravenclaw":
    print("Blue and bronze")
elif house == "slytherin":
    print("Green and silver")
else:
    print("Not known")