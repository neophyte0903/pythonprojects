# # we want to create a string with dynamic blank filling
# youtuber = "triggered insaan "


# # three ways to do it
# print("subscribe to " + youtuber)  # using string concatination
# print("subscribe to {}".format(youtuber))  # using string formater
# print(f"subscribe to {youtuber}")  # using f strings

adj = input("adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"computer programing is so{adj}! it makes me so excited all the time because \n i love to {verb1}. stay hydrated and {verb2} like you are {famous_person}"

print(madlib)
