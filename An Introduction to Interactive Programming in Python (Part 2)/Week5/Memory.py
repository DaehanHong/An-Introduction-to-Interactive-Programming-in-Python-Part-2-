# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def init():
    global cards, opened, state, f_open, s_open, score, move    
    state = 0
    score = 0
    move = 0
    f_open = -1
    s_open = -1    
    cards = []
    
    for x in range(8):
        cards.append(x)
    cards *= 2
    random.shuffle(cards)
    opened = [False]*16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, score, f_open, s_open, move
    cardIndex = list(pos)[0]//50
    
    if not opened[cardIndex]:
        if state == 0:
            f_open = cardIndex
            opened[cardIndex] = True
            state = 1
        elif state == 1:
            s_open = cardIndex
            opened[cardIndex] = True
            if cards[f_open] == cards[s_open]:
                score += 1
            state = 2
            move += 1
            label.set_text("Move = " + str(move))
        else:
            if cards[f_open] != cards[s_open]:
                opened[f_open], opened[s_open] = False, False
                f_open, s_open = -1, -1
            f_open = cardIndex
            opened[cardIndex] = True
            state = 1
                  
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if opened[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "white", "pink")
            canvas.draw_text(str(cards[i]), (i*50+11, 69), 55, "Black")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "white", "skyblue")
    label.set_text("Move = " + str(move))
init()

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", init)
label = frame.add_label("Move = " + str(move))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric