numbers = [1,7,19,22,24,8]
#defining functions

def is_odd(numero):
    #parenthesis form the paremeters of our fxn
    odd = True
    if numero %2 == 0:
        odd=False
    else:
        odd=True
        return odd
for i in numbers:
    if is_odd(i) :
        print(f"{i} is odd")
    else:
        print(f"{i} is even")

#calling 2 same things different 2.