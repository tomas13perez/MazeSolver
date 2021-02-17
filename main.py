"""
CSC 412
ICA #3
2/5/2021

@author: Tomas Perez
"""
import queue
from queue import Queue

totalNodesVisited = 0
fastestRoute = []
start_position = [0, 1]
end_position = [11, 11]
visited = [[False for i in range(11)] for j in range(11)]
row_queue = queue.Queue()
column_queue = queue.Queue()


# dr = [0, -1, +1, 0]
# dc = [-1, 0, 0, +1]
# dr = [-1, +1, 0, 0]
# dc = [0, 0, +1, -1]

def wipe_table():
    global totalNodesVisited
    totalNodesVisited = 0
    global fastestRoute
    fastestRoute = []
    global start_position
    start_position = [0, 1]
    global visited
    visited = [[False for i in range(11)] for j in range(11)]
    global row_queue
    row_queue = queue.Queue()
    global column_queue
    column_queue = queue.Queue()


def print_maze(user_maze):
    for row in user_maze:
        for c in row:
            print(c, end='')
        print('')


def bfs(end_row, end_column):
    row_queue.put(start_position[0])
    column_queue.put(start_position[1])
    solution = queue.Queue()
    solution.put("")
    found_the_end = False
    while row_queue.qsize() > 0:
        temp_path = solution.get()
        row = row_queue.get()
        column = column_queue.get()
        current_position = [row, column]
        if current_position[0] == end_row and current_position[1] == end_column:
            found_the_end = True
            return found_the_end
        for j in ["L", "R", "U", "D"]:
            temp = maze[current_position[0]][current_position[1]]
            put = temp_path + j
            if reachable(current_position, j):
                if is_visited(current_position[0], current_position[1], j) is not True:
                    solution.put(put)
                    visited[current_position[0]][current_position[1]] = True
                    rr, cc = update_pos(current_position[0], current_position[1], j)
                    row_queue.put(rr)
                    column_queue.put(cc)
    print(list(solution.queue))

    return found_the_end


def update_pos(r, c, direction):
    if direction == "U":
        r -= 1
    elif direction == "D":
        r += 1
    elif direction == "L":
        c -= 1
    elif direction == "R":
        c += 1
    return r, c


def is_visited(r, c, direction):
    if direction == "U":
        if visited[r - 1][c] is True:
            return True
    elif direction == "D":
        if visited[r + 1][c] is True:
            return True
    elif direction == "L":
        if visited[r][c - 1] is True:
            return True
    elif direction == "R":
        if visited[r][c + 1] is True:
            return True
    return False


""" This is ICA 6 """

"""
This method receives a coordinate for a maze and a direction
and determines whether the desired cell is reachable or not.
@coordinate:param - location on the maze in the form of [row, column]
@direction:param - refers to a lettered representation of direction, 
                    such as 'U', 'D', 'L', 'R'
@:returns - true if cell is reachable, false if not. 
"""


def reachable(coordinate, direction):
    row = coordinate[0]
    column = coordinate[1]
    cell = maze[row][column]
    adjacent_cell = ""
    if direction == 'U':
        if '¯' in cell:
            return False
    # Special case where we need to look at an adjacent cell.
    elif direction == 'D':
        adjacent_cell = maze[row + 1][column]
        if '¯' in adjacent_cell:
            return False
    # Special case where we need to look at an adjacent cell.
    elif direction == 'L':
        adjacent_cell = maze[row][column - 1]
        if '|' in adjacent_cell:
            return False
    elif direction == 'R':
        if '|' in cell:
            return False
    return True


maze = [[" |", "¯|", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", " |", " |", "¯ ", "¯|", "  ", "  ", "  ", "  ", "  ", " |"],
        [" |", " |", " |", " |", "¯ ", "  ", "  ", "  ", "  ", "  ", " |"],
        [" |", "  ", "¯ ", "  ", "¯ ", "¯ ", "¯|", "  ", "  ", "  ", " |"],
        [" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯|", "  ", "¯ ", "¯ ", "¯|", " |"],
        [" |", "  ", "  ", "  ", "  ", " |", " |", "¯ ", "¯ ", "¯ ", " |"],
        [" |", "  ", "  ", "  ", "  ", " |", "  ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", "  ", "  ", "  ", "  ", " |", " |", "¯ ", "¯ ", "¯|", " |"],
        [" |", "  ", "  ", "  ", "  ", " |", " |", "  ", "  ", " |", " |"],
        [" |", "  ", "  ", "  ", "  ", " |", " |", "  ", "  ", " |", " |"],
        ["¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ "]]
print_maze(maze)
myBoolean = bfs(9, 10)
print(myBoolean)

print()
wipe_table()
print()

""" Dr. Kolta's Maze """
# 11 x 11 version
maze = [[" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", " |", "  ", "¯ ", "¯ ", "¯ ", "¯|", "¯ ", "¯ ", "¯ ", " |"],
        [" |", " |", "¯ ", "¯ ", "¯ ", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", " |", "  ", "  ", "  ", " |", "  ", "¯|", "¯ ", "¯|", " |"],
        [" |", " |", "  ", "  ", "  ", "  ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", " |", " |", "¯ ", "¯|", "¯ ", "¯|", "¯|", "¯|", "¯ ", " |"],
        [" |", " |", " |", " |", " |", " |", " |", "  ", " |", "  ", "¯|"],
        [" |", " |", "  ", " |", "  ", " |", "  ", "¯ ", "  ", "¯ ", " |"],
        ["¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ "]]

print_maze(maze)
myBoolean = bfs(9, 10)
print(myBoolean)
