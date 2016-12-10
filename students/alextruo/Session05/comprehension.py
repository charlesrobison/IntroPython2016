#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
food_prefs = {"Name" : "Chris", "City": "Seattle", "Cake": "Chocolate", "Fruit": "mango", "Salad": "greek", "Pasta": "lasagna"}


#1. Print the dict by passing it to a string format method, so that you get something like: 
#Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”

print(" {Name} is from Seattle, and he likes {Cake} cake and {Fruit} fruit and {Salad} salad and {Pasta} pasta.".format(**food_prefs))

#Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number.)

comprehension1 = dict( (i, hex(i)) for i in range(16)    )
print(comprehension1)

#Do the previous entirely with a dict comprehension -- should be a one-liner

comprehension2 = {i: hex(i) for i in range(16)}

print(comprehension2)

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘a’s in each value. 
#You can do this either by editing the dict in place, or making a new one. If you edit in place, make a copy first!

comprehension3 = {key:value.count('a') for key, value in food_prefs.items()}
print(comprehension3)

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

comprehension_set2 = {item for item in range(21) if not item %2}
comprehension_set3 = {item for item in range(21) if not item %3}
comprehension_set4 = {item for item in range(21) if not item %4}

print(comprehension_set2)
print(comprehension_set3)
print(comprehension_set4)

#create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.

number = 12

#create up to 11 sets
dividers =  range(2, number + 1)
print("\nThis is the range of dividers:", dividers)

example_set = [set() for item in dividers]
print("\nThis is the example set:", example_set)

#zip() function combines the dividers and the example_set into pairs

for item, sets in zip(dividers, example_set):
    #list comprehension here, for each object in range up to 20, make sure it's  divisible by the item object
    [sets.add(example) for example in range(21) if not example % item]

print("These are the sets:", example_set)
#loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.

#The idea here is that when you see three (Or more!) lines of code that are almost identical, 
#then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.