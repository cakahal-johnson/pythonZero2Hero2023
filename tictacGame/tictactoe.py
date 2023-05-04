# importing pygame
import pygame as pg, sys
from pygame.locals import *
import time

#  initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
black = (10, 10, 10) # RBG color code
line_color = (238, 75, 43) # RBG color code

# define the board using 3x3
TTT = [[None]*3, [None]*3, [None]*3]

# defining the pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Cakahal Project")


# loading the images
opening = pg.image.load('bg.jpg')
x_img = pg.image.load('queen.jpg')
o_img = pg.image.load('king.png')

# resizing the images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height+100))


# function for starting up the game using blit()
def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(black)

#     Drawing vertical line
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)

#     Drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)

#     naming the function as draw_status()
    draw_status()

#     draw_status() function draws a black rectangle where we update the status of the game showing which players turn
#     is it and whether the game ends or draws.


def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + " 's Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

#     coping the rendered message onto the board
    screen.fill((128, 128, 128), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()


#    checking for the winning by holding them in variable
def check_win():
    global TTT, winner, draw

#     checking the winner rows
    for row in range(0, 3):
        if((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
# here we find a row that won
            winner = TTT[row][0]
            # drawing the winner line
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6), (width, (row + 1) *height/3 - height/6),4)

            break
#     checking the winner columns
    for col in range(0, 3):
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):

            #  here the column won the game

            winner = TTT[0][col]
#                        # drawing the winner line
            pg.draw.line(screen, (250, 0, 0), ((col + 1)* width/3 - width/6, 0), ((col + 1) * width/3 - width/6, height), 4)

            break

#     checking the diagonally winner
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        #  game won on diagonally left to right
        winner = TTT[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (TTT[0][2] == TTT[1][1] == TTT[2][0] and (TTT[0][2]) is not None):
        # game won diagonally right to left
        winner == TTT[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

#         here has the diagonal code
#     parking everything to check for the draw match
    if(all([all(row) for row in TTT]) and winner is None):
        draw = True
    draw_status()

    # here we write function that takes the row and column where the mouse is clicked and the it draws the "queen" or
    # "king" to get mark we calculate the coordinates of the queen n the king starting point from where we'll draw
    # the png image of the mark


# these userClick() function is triggered every time the user presses the mouse
def drawXO(row, col):
    global TTT, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30

    #         column coordinate
    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    TTT[row - 1][col - 1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
    # print(posx, posy)
    # print(TTT)


def userClick():
# getting coordinates of the mouse clicked
    x, y = pg.mouse.get_pos()

#     getting column of mouse click (1 - 3)
    if(x < width/3):
        col = 1
    elif (x < width/3*2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None
        # get row of mouse click
    if (y < height/3):
        row = 1
    elif (y < height/3*2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    # print(row, col)
#     parking the queen and king as the XO
    if(row and col and TTT[row-1][col-1] is None):
        global XO
#         let's draw the queen or the king screen
        drawXO(row, col)
        check_win()


#     let's start after each set played and also reset all the variables to the beginning of the game

def reset_game():
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]

"""
to start the game we need to call the game_opening() function 
if user presses mouse button event will be captured and then we trigger the userClick() function
where if user wins or draw we reset_game() function 
we update the display in each iteration and we have set the frames per second to 30

"""

game_opening()
# # running the looping for the game
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
#             the user clicked and place an King or queen
            userClick()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)



