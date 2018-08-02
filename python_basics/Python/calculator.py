

# User input prompt
userName = input ("User: ")
userPass = input ("Password: ")
# Answer user prompt

userRight = "word"


if userPass == userRight :
    print ("Correct password. Hello "+userName)
    while True:

        number_one = input("Please enter a number:")
        number_two = input("Please enter another number:")

        number_one = int(number_one)
        number_two = int(number_two)

        total = number_one+number_two
        print("Total is: " + str(total))

if userPass != userRight :
    print ("Incorrect password. Try again.")
    userName = input ("User: ")
    userPass = input ("Password: ")

    


    


# Variables
'''interchangable
variables'''



