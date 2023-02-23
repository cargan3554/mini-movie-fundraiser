# main routine starts here

# # set maximum number of tickets below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")
    tickets_sold +=1
    
    if name == 'xxx':
        break

# output number of tickets sold