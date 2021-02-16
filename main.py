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
rows, cols = (11, 11)
visited = [[False] * cols] * rows
row_queue = queue.Queue()
column_queue = queue.Queue()
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def print_maze(user_maze):
    for row in user_maze:
        for c in row:
            print(c, end='')
        print('')


def bfs():
    row_queue.put(start_position[0])
    column_queue.put(start_position[1])
    solution = Queue()
    solution.put("")
    found_the_end = False
    # cell = maze[row][column]
    visited[start_position[0]][start_position[1]] = True
    while solution.qsize() > 0:
        temp_path = solution.get()  # updates the size in order to exit while loop
        row = row_queue.get()
        column = column_queue.get()
        current_position = [row, column]
        # FIXME: Debating on whether or not to use explore neighbours...
        for i in range(4):
            rr = current_position[0] + dr[i]
            cc = current_position[1] + dc[i]
            new_rc = (rr, cc)
            for j in ["L", "R", "U", "D"]:
                put = temp_path + j
                if reachable(new_rc, put):
                    if visited[rr][cc] is not True:
                        solution.put(put)
                        visited[rr][cc] = True

                row_queue.put(rr)
                column_queue.put(cc)
    print(solution)
    return solution


# def find_end(coordinates, moves):
#     start_row = coordinates[0]
#     start_column = coordinates[1]
#     for move in moves:
#         if move == "L":
#             i -= 1
#         elif move == "R":
#             i += 1
#         elif move == "U":
#             j -= 1
#         elif move == "D":
#             j += 1
#     if i == 11 and j == 11:
#         print("Found: " + moves)
#         # print_Solution(maze, moves)
#         return True
#     return False


# def print_Solution(maze, moves):
#     i = 0;
#     j = 0;
#     pos = set()
#     for move in path:
#         if move ==


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
bfs()

print()
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
# bfs(maze)
