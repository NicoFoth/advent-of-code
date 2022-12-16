with open ("2022/Day12/input.txt") as inputFile:
    input = [[*line] for line in inputFile.read().splitlines()]

def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    # -2 allowing only single steps down the mountain
    node_height = ord(matrix[x][y]) - 2

    neighbors = []

    # ensure X isn't an edge and left isn't lower than - 1 height
    if (x_min < x) and (node_height < ord(matrix[x - 1][y])):
        neighbors.append((x - 1, y))

    # same for right
    if (x < x_max) and (node_height < ord(matrix[x + 1][y])):
        neighbors.append((x + 1, y))

    # same for top
    if (y_min < y) and (node_height < ord(matrix[x][y - 1])):
        neighbors.append((x, y - 1))

    # same for bottom
    if (y < y_max) and (node_height < ord(matrix[x][y + 1])):
        neighbors.append((x, y + 1))

    return neighbors


def solve():
    for row_index in range(len(input)):
        for char_index in range(len(input[row_index])):
            if input[row_index][char_index] == "S":
                starting_position = (row_index, char_index)
                input[row_index][char_index] = "a"
            elif input[row_index][char_index] == "E":
                ending_position = (row_index, char_index)
                input[row_index][char_index] = "z"

    queue = [ending_position]

    level = dict()
    level[ending_position] = 0

    while queue:
        current_position = queue.pop(0)
        
        for n in get_neighbors(input, current_position):
            if n not in level:
                queue.append(n)
                level[n] = level[current_position] + 1
    print(level[starting_position])


solve()