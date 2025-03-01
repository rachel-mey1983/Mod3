#####IS201 Fundamentals of Computing########
PE03 Lists and Tuples
School of Technology &amp; Computing (STC) @City University of Seattle (CityU)



Before You Start
&bull;	If you have questions about the lab requirements, please ask a TA to clarify for you.
&bull;	If you are not sure what to do:
1.	Consult the resources listed below.
2.	If you cannot solve the problem after a few tries, ask a TA for help.

Lab Tasks
•	Write Python programs to complete the given tasks

1) Make a list that includes at least three people you'd like to invite to dinner. Include the following in your code.
•	print the list with at least three people
•	Modify your list, replacing the name of one the guest who can't make it with the name of the new person you are inviting. Then print the new list.
•	Use insert() to add one new guest to the beginning of your list.
•	Use insert() to add one new guest to the middle of your list.
•	Use append() to add one new guest to the end of your list.
•	Print the new list
•	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.

2) Think of at least seven different animals. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
•	Print the message The first three items in the list are:. Then use a slice to print the first three items from that program's list.
•	Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
•	Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

3) Given a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one.
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

4) A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
•	Use a for loop to print each food the restaurant offers.
•	Try to modify one of the items, and make sure that Python rejects the change.
•	The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
5) Given a list of tuples, write a Python program to sort the tuples by the second item of each tuple.
Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]
