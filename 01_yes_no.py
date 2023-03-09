def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please answer yes / no")

show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = yes_no("Do you want to see the instructions?")

    if show_instructions == "yes":
        print("game continues\n")
    elif show_instructions == "no":
        print("show instructions \n")