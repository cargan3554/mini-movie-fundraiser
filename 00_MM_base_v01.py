# functions go here
# Checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
            
        elif response == "no" or response == "n":
            return "no"
            
        else:
            print("Please enter yes or no")
            
# checks that user response is not blank
def not_blank(question):
    
    while True:
        response = input(question)
        
        if response == "":
            print("sorry this can't be blank. Please try again")
        
        else:
            return response
            
#checks user enter an interger to a given question

def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response       
        except ValueError:
            print("please enter an interger.")
            
# main routine starts here


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5
    
    # ticket is $10.50 fro users between 16 and 64
    elif var_age < 65:
        price = 10.50     
    
    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5
        
    return price
    
# set maximum number of tickets below

MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the imstructions
want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    print("instructions go here")
    
print()

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break
    
    age = num_check("Age: ")
    
    if 12 <= age <= 120:
        pass
    
    elif age < 12:
        print("sorry you are too young for this movie")
        continue

    else:        
        print("?? That looks like a typo, please try agian.") 
        continue    
    
    tickets_sold += 1
    
    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost))
    
#output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("congratulations you have sold all the tickets")

else:
    print("you have sold {} ticket/s.  There is {} tickets/s "
"remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))