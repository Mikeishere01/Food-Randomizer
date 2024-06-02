import random # this is how we can get python to choose randopmly from the list

print("Welcome to the food radomizer. My name is bulb! \n")

#creating the array/list
foodz = []

# asking users how many food places they want to add to the randomzier

r = int(input("Enter how many food places you wish to enter into the pool: "))
for i in range(0,r):
    ele=input()
    foodz.append(ele) #append  = insert this into the list

print("This is your list of restaurants ", foodz , "\n")  

#choosing random now
selected_item=random.choice(foodz)
print("This is what I have choosen! " , selected_item , "\n")  # prints out its choice

print("I hope you enjoy your meal ")