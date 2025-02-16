##  Think of at least seven different animals. Store the names of these animals in a list, and then use a for loop to print out the name of each animal. # type: ignore
#	Print the message The first three items in the list are:. Then use a slice to print the first three items from that program's list.
#	Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
#	Print the message The last three items in the list are:. Use a slice to print the last three items in the list.###



list    = ['dog', 'cat', 'elephant', 'lion', 'tiger', 'giraffe', 'bear']

print("The first three items in the list are:")

for i in list[:3]:
    print(i)    

print("Three items from the middle of the list are:")

for i in list[2:5]:

    print(i)

print("The last three items in the list are:")

for i in list[4:]:

    print(i)        
    
    





