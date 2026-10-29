has_error = True
#think of has_error as a portal to bring it back to top in case of crash

while has_error: has_error = True
    try:
        number=int(input("Enter a number: "))
        print(number)
    except:
        print("Invalid number. Please try again.")
    except ValueError:
        print("Invalid number. Please try again.")
    except KeyboardInterrupt: 
        print("You stopped the program.")
    except:
        print("You got some rando error.")
         break






