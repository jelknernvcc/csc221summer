from gasp import *


def draw_grid():
    for x in range(0, 640, 20):
        Line((x, 0),(x, 640), thickness=0.01, color=color.LIGHTGRAY)

    for y in range(0, 480, 20):
        Line((0, y),(640, y), thickness=0.01, color=color.LIGHTGRAY)


def place_player():
    global player_x, player_y, player_shape

    player_radius = 10
    player_x = 150
    player_y = 110
    player_shape = Circle((player_x, player_y),
                          player_radius, filled=True, color=color.BLUE)



begin_graphics()
draw_grid()  
place_player()

while True:
    key = update_when('key_pressed')
    if key == 'Escape':  
        break
    elif key == 's':
        move_direction = (0, 0)
    elif key == 'w':
        move_direction = (0, 1)
    elif key == 'a':
        move_direction = (-1, 0)
    elif key == 'd':
        move_direction = (1, 0)
    elif key == 'e':
        move_direction = (1, 1)
    elif key == 'q':
        move_direction = (-1, 1)
    elif key == 'c':
        move_direction = (1, -1)
    elif key == 'Shift_L':
        move_direction = (-1, -1)

    player_x += 20 * move_direction[0]
    player_y += 20 * move_direction[1]
    move_to(player_shape, (player_x, player_y))

  
end_graphics()
