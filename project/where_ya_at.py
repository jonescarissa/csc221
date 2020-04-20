# Guess That Zipcode

import webbrowser

print('''Welcome to Guess That Zipcode. I will give you a location and
you have to guess the zipcode of that location. You will have 1 guess
for each state and do not worry I will give you some hints.''')

guesses = 0
print('''Okay, this is the first one...Mahnomen, Minnesota. Here's 
your HINT: the first two numbers are 56 and the last number is 7.''')
zip1 = 56557
for guesses in range(1):
    guess = input()
    guess = int(guess)

    if guess == zip1:
        print('Correct...you are not as stupid as I thought')
        guesses = str(guesses + 1)
        break

    else:
        print('Incorrect. The correct answer is:') 
        webbrowser.open('http://www.google.com/maps/place/56557')
        break

print('''The next location is the area I grew up in which is Inwood, 
New York. Here's your HINT: the last number is 4.''')
zip2 = 10034
for guesses in range(1):
    guess = input()
    guess = int(guess)

    if guess == zip2:
       print('Correct...on to the next one') 
       guesses = str(guesses + 1)
       break

    else:
        print('Incorrect. The correct answer is:')
        webbrowser.open('http://www.google.com/maps/place/10034')
        break

print('''Since you are so smart I'm going to give you another one: Plano
Texas. And you know what I am not going to give a HINT.''')
zip3 = 75025
for guesses in range(1):
    guess = input()
    guess = int(guess)

    if guess == zip3:
        print('Correct...on to the next one')
        guesses = str(guesses + 1)
        break

    else:
        print('Incorrect. The correct answer is:')
        webbrowser.open('http://www.google.com/maps/place/75025')
        break

print('''The next location is: Eupora, Mississippi. Here's a HINT:
the last two numbers are 44. ''')
zip4 = 39744
for guesses in range(1):
    guess = input()
    guess = int(guess)
    
    if guess == zip4:
        print('Correct...on to the next one')
        guesses = str(guesses + 1)
        break

    else:
        print('Incorrect. The correct answer is:')
        webbrowser.open('http://www.google.com/maps/place/39744')
        break

print('''Next to last location is: Bay Lake, Florida. Here's a 
HINT: the middle number is 8.''')
zip5 = 32821
for guesses in range(1):
    guess = input()
    guess = int(guess)

    if guess == zip5:
        print('Correct...on to the next one')
        guesses = str(guesses + 1)
        break

    else:
        print('Incorrect. The correct answer is:')
        webbrowser.open('http://www.google.com/maps/place/32821')
        break

print('''The last one location is: Fresno, California. Here's a HINT:
the first two numbers are 93.''')
zip6 = 93701
for guesses in range(1):
    guess = input
    guess = int(guess)

    if guess == zip6:
        print('Correct...you good')
        guesses = str(guesses + 1)
        break

     else:
        print('Incorrect. The correct answer is:')
        webbrowser.open('http://www.google.com/maps/place/93701')
        break

print('''You have finished the game. You're safe for now''')





    