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


def partTwo():
    elves = parseElves()
    queue = ["N", "S", "W", "E"]
    round = 0
    while True:
        round += 1
        elf_moved = False
        proposals = makeProposals(elves, queue)

        for proposal, proposal_elves in proposals.items():
            if len(proposal_elves) > 1:
                continue
            elf_moved = True
            elves.remove(proposal_elves[0])
            elves.append(proposal)

        queue.append(queue.pop(0))
        if not elf_moved:
            break
    
    print(round)


partTwo()