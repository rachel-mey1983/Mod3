#   Make a list that includes the least three people you'd like to invite to dinner. Include the following in
#   ######

#	Print the list with at least three people
#	Modify your list, replacing the name of one the guest who can't make it with the name of the new person you are inviting. Then print the new list.
#	Use insert() to add one new guest to the beginning of your list.
#	Use insert() to add one new guest to the middle of your list.
#	Use append() to add one new guest to the end of your list.
#	Print the new list
#	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner. #####

dinner_guests = ["Josh Homme", "Lady Gaga", "Layne Staley"]
print ( "Original guest list:",
        dinner_guests )

# Replacing a guest who can't make it
print ( "Lady Gaga can't make it, inviting Chris Cornell instead." )


class Cornell:
    pass


print ( "Updated guest list:",
        dinner_guests )

# Adding guests with insert()
dinner_guests.insert ( 0,
                       "Kathleen Hanna" )  # Beginning
dinner_guests.insert ( 2,
                       "Chris Cornell" )  # Middle
print ( "Guest list with new additions:",
        dinner_guests )

# Adding a guest with append()
dinner_guests.append ( "Dave Grohl" )
print ( "Guest list after adding Chris:",
        dinner_guests )

# Removing guests until only two remain with pop()
while len ( dinner_guests ) > 2:
    removed_guest = dinner_guests.pop ()
    print ( f"Sorry, {removed_guest}, we can't invite you to dinner." )

print ( "Final guest list:",
        dinner_guests )
