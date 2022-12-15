with open("2022/Day14/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    environment = set()
    for path in input:
        path = path.split(" -> ")
        path = [pos.split(",") for pos in path]
        for i in range(len(path)-1):
            one = [int(x) for x in path[i]]
            two = [int(x) for x in path[i+1]]
            environment.add(tuple(one))
            for coord in range(2):
                for k in range(abs(one[coord]-two[coord])):
                    new = one.copy()
                    if two[coord] > one[coord]:
                        new[coord] += k+1
                    else:
                        new[coord] -= k+1
                    if tuple(new) not in environment:
                        environment.add(tuple(new))


class Sand():
    def __init__(self, lowest_y):
        self.position = [500, 0]
        self.lowest_y = lowest_y
        self.resting = False
    
    def move(self):
        moves = [[0, 1], [-1, 1], [1, 1]]
        if self.position[1] == self.lowest_y+1:
            self.resting = True
            return None
        for move in moves:
            new_pos = self.position.copy()
            for i in range(2):
                new_pos[i] += move[i]
            if tuple(new_pos) not in environment:
                self.position = new_pos
                break
        else:
            self.resting = True
            if self.position == [500, 0]:
                return True


def getLowestY(environment):
    lowest_y = 0
    for entity in environment:
        if entity[1] > lowest_y:
            lowest_y = entity[1]
    return lowest_y


def partTwo():
    current_sand = None
    counter = 0
    lowest_y = getLowestY(environment)
    while True:
        if current_sand == None:
            current_sand = Sand(lowest_y)
        if current_sand.move():
            counter += 1
            break
        if current_sand.resting:
            environment.add(tuple(current_sand.position))
            counter += 1
            if counter % 500 == 0:
                print(counter)
            current_sand = None
    print(counter)


partTwo()