"""
CSC 412
Assignment #3
2/17/2021

@author: Tomas Perez
"""
import queue
from queue import Queue
from queue import LifoQueue

start_position = [0, 1]
end_position = [11, 11]
visited = [[False for i in range(11)] for j in range(11)]
row_queue = queue.Queue()
column_queue = queue.Queue()
stack_row_queue = LifoQueue()
stack_column_queue = LifoQueue()
dfs_solution = LifoQueue()

"""
This method is responsible for wiping the global variables
and prepping them for the next iteration of maze solver.
"""


def wipe_table():
    global start_position
    start_position = [0, 1]
    global visited
    visited = [[False for i in range(11)] for j in range(11)]
    global row_queue
    row_queue = queue.Queue()
    global column_queue
    column_queue = queue.Queue()
    global stack_column_queue
    stack_column_queue = LifoQueue()
    global stack_row_queue
    stack_row_queue = LifoQueue()
    global dfs_solution
    dfs_solution = LifoQueue()


"""
This method prints the given maze to the console.
@user_maze:param - the maze the user wants to print.
"""


def print_maze(user_maze):
    for row in user_maze:
        for c in row:
            print(c, end='')
        print('')


"""
This method implements the Breadth First Search algorithm by
keeping track of the current queue of cells that need to
be searched through, while also keeping track of the most
optimal path as well as the total amount of nodes searched in.
@end_row:param - the end row number.
@end_column:param - the end column number.
@:returns - True if there is a solution to the maze, False if not,
            the optimal solution, and the total number of nodes 
            searched through.
"""


def bfs(end_row, end_column):
    total_nodes_visited = 0
    optimal_solution = ""
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
            optimal_solution = temp_path
            return found_the_end, optimal_solution, total_nodes_visited
        for j in ["L", "R", "U", "D"]:
            put = temp_path + j
            if reachable(current_position, j):
                if is_visited(current_position[0], current_position[1], j) is not True:
                    solution.put(put)
                    visited[current_position[0]][current_position[1]] = True
                    total_nodes_visited += 1
                    rr, cc = update_pos(current_position[0], current_position[1], j)
                    row_queue.put(rr)
                    column_queue.put(cc)

    return found_the_end, optimal_solution, total_nodes_visited


"""
This method implements the Depth First Search algorithm by
keeping track of the current stack of cells that need to
be searched through, while also keeping track of the most
optimal path as well as the total amount of nodes searched in.
@current_node:param - the starting cell.
@end_row:param - the end row number.
@end_column:param - the end column number.
@:returns - True if there is a solution to the maze, False if not,
            the optimal solution, and the total number of nodes 
            searched through.
"""


def dfs(current_node, end_row, end_column):
    total_nodes_visited = 0
    optimal_solution = ""
    stack_row_queue.put(current_node[0])
    stack_column_queue.put(current_node[1])
    dfs_solution.put("")
    visited[current_node[0]][current_node[1]] = True
    while stack_row_queue.qsize() > 0:
        temp_path = dfs_solution.get()
        x = stack_row_queue.get()
        y = stack_column_queue.get()
        for j in ["L", "R", "U", "D"]:
            put = temp_path + j
            if reachable((x, y), j):
                if is_visited(x, y, j) is not True:
                    temp_x, temp_y = update_pos(x, y, j)
                    stack_row_queue.put(temp_x)
                    stack_column_queue.put(temp_y)
                    visited[temp_x][temp_y] = True
                    dfs_solution.put(put)
                    total_nodes_visited += 1
                    if temp_x == end_row and temp_y == end_column:
                        optimal_solution = temp_path
                        return True, total_nodes_visited, optimal_solution

    return False


"""
This method updates the given row or column value based off 
of the direction being passed in, for the next iteration
of search.
@r:param - the row number for the cell.
@c:param - the column number for the cell.
@direction:param - the direction the cell wants to go,
            in the format of 'U', 'D', 'L', 'R'.
@:returns - True if the cell has been visited, False if not.
"""


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


"""
This method checks to see if a given coordinate (cell) and direction
has been visited previously in the search.
@r:param - the row number for the cell.
@c:param - the column number for the cell.
@direction:param - the direction the cell wants to go,
            in the format of 'U', 'D', 'L', 'R'.
@:returns - True if the cell has been visited, False if not.
"""


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
myBoolean, path, num_of_nodes = bfs(9, 10)
if myBoolean is True:
    print("This map is solvable by Breadth First Search!")
    print("Optimal Path: {0}".format(path))
    print("Total Number of Nodes Visited: {0}".format(num_of_nodes))
else:
    print("This maze was NOT solvable by Breadth First Search!")

print()
print()
wipe_table()
myBoolean, num_of_nodes, path = dfs(start_position, 9, 10)
if myBoolean is True:
    print("This map is solvable by Depth First Search!")
    print("Optimal Path: {0}".format(path))
    print("Total Number of Nodes Visited: {0}".format(num_of_nodes))
else:
    print("This maze was NOT solvable by Depth First Search!")
print()
wipe_table()

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
myBoolean, path, num_of_nodes = bfs(9, 10)
if myBoolean is True:
    print("This map is solvable by Breadth First Search!")
    print("Optimal Path: {0}".format(path))
    print("Total Number of Nodes Visited: {0}".format(num_of_nodes))
else:
    print("This map was NOT solvable by Breadth First Search!")

print()
wipe_table()
myBoolean, num_of_nodes, path = dfs(start_position, 9, 10)
if myBoolean is True:
    print("This map is solvable by Depth First Search!")
    print("Optimal Path: {0}".format(path))
    print("Total Number of Nodes Visited: {0}".format(num_of_nodes))
else:
    print("This maze was NOT solvable by Depth First Search!")
