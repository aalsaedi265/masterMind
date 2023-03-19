import random

COLORS =['R','G','B', 'Y','W','O']
TRIES = 10
#difficutly level
CODE_LENGTH=4

def generateCode():
    code =[]
    
    for _ in range(CODE_LENGTH): # _ this is an anounmous varable
        color=random.choice(COLORS)
        code.append(color)
    return code

code = generateCode()

def guess_code():
    while True:
        #spplit to spereate elemetns based on spaces
        guess = input('Guess: ').upper().split(' ')
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid: {color}. Try again")
                
                break
        else:
            break
        
    return guess
            
            
def check_code(guess,real_code):
    color_counts={}
    correct_pos=0
    incorrect_pos=0    
    for color in real_code:
        if color not in color_counts: color_counts[color] =0
        color_counts[color]+=1
#zip will take two argumetns and turn them into a toppul
# guess=['x','z']
# real =['w','y']
# [('x','w'),('z','y')]

    arr =list(zip(guess, real_code))
    
    for guess_color, real_color in zip(guess, real_code):
            if guess_color == real_color:
                correct_pos += 1
                color_counts[real_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
            if (
                guess_color in color_counts
                and color_counts[guess_color] > 0
                and guess_color != real_color
            ):
                incorrect_pos += 1
                color_counts[guess_color] -= 1 
    return correct_pos, incorrect_pos
             
def theGame():
    print(f"Welecome to the Game, you have {TRIES} tries before it over")
    print ("Valid options are, " + ", ".join(COLORS))
    code = generateCode()
    for attempts in range(1,TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess,code)
        if correct_pos == CODE_LENGTH:
            print(f"Good you finished in {attempts} attempts; now go achieve more glory")
            break
        print(f"Correct positions: {correct_pos} | Incorect Position: {incorrect_pos}")
    else:
        print('you lost waigee, here is the answer: ', *code)
              
if __name__=="__main__": # insures the file is running completes not just using some of it functionality
    theGame()