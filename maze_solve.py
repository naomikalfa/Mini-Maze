from colorama import Fore
import sys
import time


def read_maze(filename):
    file = open(filename)
    string_maze = file.read()
    split_maze = string_maze.split('\n')
    clean_maze = [list(i) for i in split_maze]
    return clean_maze


def print_maze(maze):
    for char_list in maze:
        for char in char_list:
            print(char, end='')
        print()
    return


def find_agent_position(maze):
    position_y = 0
    position_x = 0
    for y in maze:
        for x in y:
            if maze[position_y][position_x] == 'o':
                return position_y, position_x
            position_x = position_x + 1

        position_x = 0
        position_y = position_y + 1
    return position_y, position_x


def n(maze, starting_x, starting_y):
    return maze[starting_y - 1][starting_x]


def e(maze, starting_x, starting_y):
    return maze[starting_y][starting_x + 1]


def s(maze, starting_x, starting_y):
    return maze[starting_y + 1][starting_x]


def w(maze, starting_x, starting_y):
    return maze[starting_y][starting_x - 1]


def rotate_right(direction):
    if direction == DIRECTION_N:
        return DIRECTION_E
    if direction == DIRECTION_E:
        return DIRECTION_S
    if direction == DIRECTION_S:
        return DIRECTION_W
    if direction == DIRECTION_W:
        return DIRECTION_N


def rotate_left(direction):
    if direction == DIRECTION_N:
        return DIRECTION_W
    if direction == DIRECTION_W:
        return DIRECTION_S
    if direction == DIRECTION_S:
        return DIRECTION_E
    if direction == DIRECTION_E:
        return DIRECTION_N


maze = read_maze('~/1.txt')
print_maze(maze)

starting_y, starting_x = find_agent_position(maze)

DIRECTION_N = 0
DIRECTION_E = 1
DIRECTION_S = 2
DIRECTION_W = 3

agent_direction = 0

CRUMB = '.'
END = 'x'
SPACE = ' '
WALL = '+'

gen = 0

while True:

    print(Fore.LIGHTCYAN_EX + 'generation:', gen)
    gen += 1

    # LOOK
    if agent_direction == DIRECTION_N:
        what_im_looking_at = n(maze, starting_x, starting_y)
    elif agent_direction == DIRECTION_E:
        what_im_looking_at = e(maze, starting_x, starting_y)
    elif agent_direction == DIRECTION_S:
        what_im_looking_at = s(maze, starting_x, starting_y)
    elif agent_direction == DIRECTION_W:
        what_im_looking_at = w(maze, starting_x, starting_y)
    else:
        raise Exception('Invalid direction %s' % str(agent_direction))

    # PERCEIVE
    if what_im_looking_at == WALL:
        agent_direction = rotate_right(agent_direction)

    elif what_im_looking_at == SPACE or what_im_looking_at == CRUMB:
        if agent_direction == DIRECTION_N:
            maze[starting_y][starting_x] = '.'
            starting_y = starting_y - 1
            maze[starting_y][starting_x] = 'o'
            agent_direction = rotate_left(agent_direction)

        elif agent_direction == DIRECTION_E:
            maze[starting_y][starting_x] = '.'
            starting_x = starting_x + 1
            maze[starting_y][starting_x] = 'o'
            agent_direction = rotate_left(agent_direction)

        elif agent_direction == DIRECTION_S:
            maze[starting_y][starting_x] = '.'
            starting_y = starting_y + 1
            maze[starting_y][starting_x] = 'o'
            agent_direction = rotate_left(agent_direction)

        elif agent_direction == DIRECTION_W:
            maze[starting_y][starting_x] = '.'
            starting_x = starting_x - 1
            maze[starting_y][starting_x] = 'o'
            agent_direction = rotate_left(agent_direction)

    elif what_im_looking_at == END:
        print(Fore.GREEN + 'Well done, agent - X marked the solve!')
        sys.exit(0)
    else:
        raise Exception('Invalid direction %s' % str(agent_direction))

    print_maze(maze)
    time.sleep(.05)
