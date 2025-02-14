
# Julius Caesar Act 4, Scene 3, 218–224
brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."

# print out the text of this speech
print(brutus_speech)

list_of_words = brutus_speech.split(sep=" ")

# Strip out punctuation
for word in list_of_words:
    word = word.strip(",")
    word = word.strip(".")
    word = word.strip(";")
    word = word.strip("\n")

print(f"Number of words = {len(list_of_words)}\n")
for i in range(1, 20):
    number_words = len([x for x in list_of_words if len(x) == i])
    print(f"{i}-letter words = {number_words}") if number_words > 0 else None
