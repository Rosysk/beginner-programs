# r: red
# g: green
# y: yellow
# l: blue
# b: black
# w: white

# later, ask the human to type this in.
# answer="ybrl"
import random
game=["l","r","b","w","y","g"]
random.shuffle(game)
answer = game[0]+game[1]+game[2]+game[3]

def add(x,y):
    return x+y

def black(guess):
    black_pin = 0
    for y in range(0,4):
        if answer[y]==guess[y]:
            black_pin += 1
    return black_pin

def white(guess):
    white_pin = 0
    for x in range(0,4):
        if answer[0]==guess[x]:
            white_pin += 1
    for x in range(0,4):
        if answer[1]==guess[x]:
            white_pin += 1
    for x in range(0,4):
        if answer[2]==guess[x]:
            white_pin += 1        
    for x in range(0,4):
        if answer[3]==guess[x]:
            white_pin += 1        

    return white_pin-black(guess)

def guess(x):
    print('you got %s black pins' % black(x))
    print('you got %s white pins' % white(x))
