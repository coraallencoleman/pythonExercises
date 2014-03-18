print("Please think of a number between 0 and 100!")

numGuesses = 0
ans = 50
user = ''
low = 0
high = 100

print("Is your secret number " + str(ans) + "?")
user = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
while user != 'c':
    if user == 'h':
        high = ans
        ans = (ans + low)/2
    elif user == 'l':
        low = ans
        ans = (ans + high)/2
    else:
        print "Sorry, I did not understand your input."
    print("Is your secret number " + str(ans) + "?")
    user = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
print('Game over. Your secret number was: ' + str(ans))