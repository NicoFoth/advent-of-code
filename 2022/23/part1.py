from collections import defaultdict


with open("2022/Day23/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def parseElves():
    elves = []
    for row_index in range(len(input)):
        for char_index in range(len(input[0])):
            if input[row_index][char_index] == "#":
                elves.append((row_index, char_index))
    return elves


def makeProposals(elves, queue):
    proposals = defaultdict(list)
    elves = set(elves)
    directions = {
        "N": [(-1, 0), (-1, 1), (-1, -1)],
        "S": [(1, 0), (1, 1), (1, -1)],
        "W": [(0, -1), (1, -1), (-1, -1)],
        "E": [(0, 1), (1, 1), (-1, 1)],
    }
    all_directions = set(directions["N"] + directions["S"] + directions["W"] + directions["E"])
        
    for elf in elves:
        for neighbor in all_directions:
            neighbor_cell = tuple([a+b for a,b in zip(elf, neighbor)])
            if neighbor_cell in elves:
                break
        else:
            continue
        
        for char in queue:
            direction = directions[char]
            occupied = False
            for cell in direction:
                temp_pos = tuple([a+b for a,b in zip(elf, cell)])
                if temp_pos in elves:
                    occupied = True
            if not occupied:
                proposed_pos = [a+b for a,b in zip(elf, direction[0])]
                proposals[tuple(proposed_pos)].append(elf)
                break
    return proposals


def partOne():
    elves = parseElves()
    queue = ["N", "S", "W", "E"]
    for round in range(10):
        proposals = makeProposals(elves, queue)

        for proposal, proposal_elves in proposals.items():
            if len(proposal_elves) > 1:
                continue
            elves.remove(proposal_elves[0])
            elves.append(proposal)

        queue.append(queue.pop(0))

    max_x, min_x = max([x[0] for x in elves]), min([x[0] for x in elves])
    max_y, min_y = max([x[1] for x in elves]), min([x[1] for x in elves])
    solution = (max_x-min_x + 1) * (max_y-min_y + 1) - len(elves)
    print(solution)


partOne()