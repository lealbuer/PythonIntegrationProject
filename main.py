"""Reel Fishing - This is an integration project showcasing what I've
learned in COP1500. This program is geared towards helping anglers with
calculations and regulations off the Florida Coast.  The following coastal
species are included: trout, snook, redfish, and bonefish."""
__author__ = "Lilia Jamette"


# Resources: MyFWC.com, CallOutdoors.com, Salim Jamette (recreational angler)

def input_option1234(prompt):
    """Requires user to input 1, 2, 3, or 4 to select an option"""
    while True:
        try:
            option = int(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            continue

        if option < 1 or option > 4:
            print("Please enter 1, 2, 3, or 4")
            continue
        else:
            break
    return option


def input_option1_or_2(prompt):
    """Requires user to input 1 or 2 to select an option"""
    while True:
        try:
            option = int(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            continue

        if option < 1 or option > 2:
            print("Please enter 1 or 2")
            continue
        else:
            break
    return option


def input_integer(prompt):
    """Ensures user input will only be an integer"""
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Please enter a whole number")
            continue
        else:
            break
    return user_input


def input_decimal(prompt):
    """Ensures user input will only be an integer or decimal"""
    while True:
        try:
            user_input = float(input(prompt))
        except ValueError:
            print("Please enter a whole number or a decimal")
            continue
        else:
            break
    return user_input


def get_fish_weight(length, girth, name):
    """Determines fish weight"""
    # Multiply length by girth squared all divided by 900.
    fish_weight = length * girth ** 2 / 900
    # Print fish_weight rounded to two decimal places.
    print("Your fish weighs about {:.2f} pounds.".format(fish_weight))
    print("Nice catch, " + name + "!")


def get_average_fish_length():
    """Calculates average length of fish from user input"""
    sum_of_lengths = 0
    fish_total = input_integer("How many fish did you catch? ")
    if fish_total > 0:
        print("Sweet! Press enter to start entering your fish lengths one at "
              "a time. Be sure to press 'enter' after each length.")
        # for loop to get input from user for as many fish as caught
        for x in range(fish_total):
            sum_of_lengths += input_decimal("Enter a fish length: ")
        print("Average length: {:.2f}".format(sum_of_lengths / fish_total))
    else:
        print("Sorry, can't find the average.")


def get_share_of_fish(fish_total, people):
    """Calculates whole number of fish per person"""
    # floor division for quantity of whole fish per person.
    share = fish_total // people
    print("Each person gets at least {} whole fish.".format(share))
    return share


def add_fish_info_to_file():
    """Uses a while loop to add fish information to a file"""
    option = input_option1_or_2("Enter '1' to add fish or '2' when finished")
    while option == 1:
        fish_type = input("Enter fish_type: ")
        date_caught = input("Enter date caught: ")
        fish_length = input("Enter fish length: ")
        in_file = open("fish_info.txt", 'w')
        in_file.write(fish_type + " " + date_caught + " " + fish_length + "\n")
        option = input_option1_or_2("Enter '1' to add fish or '2' when "
                                    "finished")
        in_file.close()
    print("Your fish information has been saved!")


def main():
    """Helps users with fishing calculations and regulations off the Florida
    Coast."""
    name = input("Enter your name: ")
    print("Welcome to Reel Fishing, " + name + "!")  # concatenate strings
    print("Find information for the following Coastal Species in Florida:")
    print("Snook, Trout, Redfish, Bonefish")

    # Get input from user to calculate fish weight.
    print("1. Estimate weight of fish without the need for a scale.")
    length = input_decimal("Enter fish length in inches as a whole number or "
                           "decimal: ")
    girth = input_decimal("Enter fish girth in inches as a whole number or "
                          "decimal: ")
    get_fish_weight(length, girth, name)

    # Have user input fish type to provide specific information for that
    # species.
    print("2. Choose your fish.")
    fish_type = input_option1234("Enter the number for type of fish: 1-snook "
                                 "2-trout 3-redfish 4-bonefish.")
    # Snook
    if fish_type == 1:
        print("Snook")
        print("Closed Season:\nAtlantic(except Monroe): Dec 15-Jan 31 and "
              "June 1- Aug 31\nGulf(including Monroe):Dec 1-end of Feb and "
              "May 1-Aug 31")
        coast = input_option1_or_2("Enter the number 1-for Atlantic OR 2-for "
                                   "Gulf and Monroe County")
        if coast == 1:
            # Determine if fish is too short, too long, or able to keep.
            # Use subtraction operator to find how short or long.
            if length < 28:
                short = 28 - length
                print("Your fish is {:.2f} inches too short.".format(short))
            elif length > 32:
                long = length - 32
                print("Your fish is {:.2f} inches too long.".format(long))
            else:
                print("You've got a keeper!")
        else:
            # Determine if fish is too short, too long, or able to keep.
            if length < 28:
                short = 28 - length
                print("Your fish is {:.2f} inches too short.".format(short))
            elif length > 33:
                long = length - 33
                print("Your fish is {:.2f} inches too long.".format(long))
            else:
                print("You've got a keeper!")
    # Trout
    elif fish_type == 2:
        print("Trout")
        print("Closed Season:\nW.P. Zone: Feb\nC.E. Zone: Nov-Dec")
        print("CATCH and RELEASE in Pasco-Gordon Pass/Collier Counties")
        # Determine if fish is too short, too long, or able to keep.
        if length < 15:
            short = 15 - length
            print("Your fish is {:.2f} inches too short.".format(short))
        elif length > 19:
            print('You can keep only 1 trout greater than 19" per vessel.')
        else:
            print("You've got a keeper! (NOT Pasco-Gordon Pass/Collier "
                  "Counties")
    # Redfish
    elif fish_type == 3:
        print("Redfish")
        print("No closed season")
        print("CATCH and RELEASE in Pasco-Gordon Pass/Collier Counties")
        # Determine if fish is too short, too long, or able to keep.
        if length < 18:
            short = 18 - length
            print("Your fish is {:.2f} inches too short.".format(short))
        elif length > 27:
            long = length - 27
            print("Your fish is {:.2f} inches too long.".format(long))
        else:
            print("You've got a keeper! (NOT Pasco-Gordon Pass/Collier "
                  "Counties")
    # Bonefish
    else:
        print("Bonefish")
        print("CATCH and RELEASE ONLY")

    # Find the average of last 3 catches.
    print("Do you want to find the average length of your caught fish?")
    answer = input_option1_or_2("Type the number '1' for yes or '2' for no.")
    if answer == 1:
        get_average_fish_length()
    else:
        print("No problem! Maybe next time!")

    # Sharing fish on the boat.
    print("4. Share the fish on the boat!")
    fish_total = input_integer("Enter total number of fish caught and kept by "
                               "all as a whole number:  ")
    people = input_integer("Enter number of people on the boat: ")
    share = get_share_of_fish(fish_total, people)
    # Mod operator to calculate the extra fish and share, if necessary
    extra = fish_total % people
    if extra > 0 and share != 0:
        print("There is/are {} extra fish. Raffle it/them off!".format(extra))
        # shortcut operator to add 1 extra fish to share
        share += 1
        print("You could be going home with {} fish!".format(share))
        if extra > 1:
            print("Only 1 extra fish allowed. :)")

    print("Would you like to enter and store all of your fish information?")
    choice = input_option1_or_2("Enter the number '1' for yes OR '2' for no")
    if choice == 1:
        add_fish_info_to_file()
    else:
        print("Maybe next time!")

    # repeat string 3 times using *.
    print("Thanks for using Reel Fishing! " + "BYE! " * 3)


# Call to main function
main()
