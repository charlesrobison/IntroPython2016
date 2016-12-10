from collections import OrderedDict

#!/usr/bin/env python

#this is my list of donors, with each key as the name and value as a list of numbers.
donors = {"Alex Truong" : [30, 50], "Bob Jones": [50], "Sarah Green": [24, 1], "John Allen": [10, 2], "Laura Lee": [100, 120]}

#define the function for report: TO DO
def print_report():
    print("\nThis will print a report.")
#If I choose‘Create a Report’ print a list of your donors, sorted by total historical donation amount.
    print("\nThese are the donors: {}".format(donors))
#Include Donor Name, total donated, number of donations and average donation amount as values in each row.
    for name, donation in donors.items():
        print("\tName: {} \tNumber of donations: {} \tAverage: {}".format(name, len(donation), sum(donation)/len(donation)))
        #this is the same way, without string formatting. print("\tName: ", name,"\tNumber of donations: ", len(donation), "\tAverage: ", sum(donation)/len(donation))
    #Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
#After printing this report, return to the original prompt.

#At any point, the user should be able to quit their current task and return to the original prompt.


#define the send_thanks function
def send_thanks():
    #while True, do this loop
    while True: 
        print("\nThis will write a thank you note.")
        #give the user options
        print("""
            1. Type the full name of the donor.
            2. Type 'list' if you want to see everyone who donated.
            3. Type 'x' to go back to main menu.
            =>
            """)
        #prompt the user for an input
        x = input()
 #If  user types ‘list’, shows the  list of the donor names and re-prompt
        if x == "list":
            #print the list of donors
            print(donors)
        elif x in donors:
#If the user types a name in the list, use it and tell me how much the current person donated.
            print("\n",x, "gave this much money:", "$",donors[x])
            #Ask for another donation amount

#add exception #1
            try:
                donate = float(input("\nDonation amount: " ))
            #if it's an integer, then  print the thank you email and then enter the amount in the email.
            #if  type(donate) == int:
                thank_you = "Thanks for your ${} donation! You are a reoccuring donor!".format(donate)
                print(thank_you)
                print("We are adding %s" % donate, "for ", x)  
                #this appends a value to the value, which is a list.
                donors[x].append(donate)         
            
            #If I tried to enter a string, throw this error.   
            except ValueError:
                print("Sorry, you must enter an integer for the donation. No strings allowed")
                send_thanks()
           # if type(donate) == str:
             #   raise 
            #start over again
                
            #append new value to existing key or donor name. If the user does not exist, then add him/her/
        elif x not in donors and x != "x":
            try:
                donate = float(input("\nEnter a donation: " ))
           #if the donation is an integer, thank the donor and add it to the list. 
                print("\nWe're adding the donor to the list!")
                donors[x] = [donate]
                thank_you = """
                Thanks for your ${} donation! 

                We are so glad you could join as a donor! Your contribution makes things possible.

                Sincerely, 
                    The Donation Company
                """.format(donate)
                print(thank_you)           

#add second exception error
            except ValueError:
                print("Sorry, you must enter an integer for the donation. No strings allowed")
                send_thanks()

#Verify that the amount is in fact a number, and re-prompt if it isn’t.
        elif x == "x":
            main()
        else:
            print("\nSorry, that's not a valid input. Try again.")
            send_thanks()

# here is where triple quoted strings can be helpful
message = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""
def main():
    """
    run the main interactive loop
    """
    response = ""
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(message)
        response = input("==> ").strip()  # strip() in case there are any spaces
        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('Please type: "s", "p", or "x"')

if __name__ == "__main__":
    main()