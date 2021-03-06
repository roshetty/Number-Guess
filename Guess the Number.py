# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_number = 0
count = 7
ur_no = None
num_range = 100
# helper function to start and restart the game
def new_game():
    
    global secret_number
    global count 
    count = 7
    secret_number = random.randrange(0, num_range)
    
    if num_range == 100:
        count = 7
        print "\nNew Game. Range is from 0 to 100"
        print "Number of remaining Gusses is",count,"\n"
    elif num_range == 1000:
        count = 10
        print "\nNew Game.Range is from 0 to 1000"
        print "Number of remaining gusses is",count,"\n"
    
     
    

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()
    # button that changes the range to [0,100) and starts a new game
    
 
    
    # remove this when you add your code
def range1000():
    global num_range
    num_range = 1000
    new_game()


    # button that changes the range to [0,1000) and starts a new game
    
    
    def input_guess(guess):
    # main game logic goes here
    global count
    global ur_no
    ur_no = int(guess)
    print "Guess was ",ur_no
   
    
    if (ur_no == secret_number):
        print "Correct"
        new_game()
    elif (ur_no > secret_number) and not(count <= 0):
        print "Lower!"
        count = count - 1
        print "Number of remaining gusses is",count,"\n"
    elif (ur_no < secret_number) and not(count <= 0):
        print "Higher!"
        count = count - 1
        print "Number of remaining gusses is",count,"\n"
    if count == 0:
        print"You ran out of guesses. The number was",secret_number,"\n"
        new_game()
        
    

    
# create frame


# register event handlers for control elements and start frame


# call new_game
new_game()
frame = simplegui.create_frame('Testing', 200, 200)
button1 = frame.add_button('Range is[0-100)',range100,150)
button2 = frame.add_button('Range is [0-1000)',range1000,150)
frame.add_input('Enter a guess', input_guess, 150)
frame.start()


# always remember to check your completed program against the grading rubric
