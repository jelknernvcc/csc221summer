from gasp import *

def place_player():
    global x, y, shape
    x, y = 400, 300
    shape = Circle((x, y), 10, filled=True, color=color.BLUE)

begin_graphics(800, 600)
place_player()
while True:
    key = update_when('key_pressed')
    if key == 'Escape':  
        break
    elif key == 'h':
        move_direction = (-1, 0)
    elif key == 'j':
        move_direction = (0, 1)
    elif key == 'k':
        move_direction = (1, 0)
    elif key == 'l':
        move_direction = (0, -1)
    else:
        move_direction = (0, 0)
    x, y = x + 20 * move_direction[0], y + 20 * move_direction[1]
    move_to(shape, (x, y))
end_graphics()
