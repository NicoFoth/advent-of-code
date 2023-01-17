import itertools
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


def makeProposals(elves, round):
    proposals = defaultdict(list)
    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
        [(0, -1), (1, -1), (-1, -1)],
        [(0, 1), (1, 1), (-1, 1)],
        ]
    cycling_directions = itertools.cycle(directions)
    
    for _ in range(round % 4):
        next(cycling_directions)

    for elf in elves:
        for counter in range(4):
            direction = next(cycling_directions)
            if counter >= 3:
                break
            occupied = False
            for cell in direction:
                temp_pos = [a+b for a,b in zip(elf, cell)]
                if temp_pos in elves:
                    occupied = True
            if not occupied:
                proposed_pos = [a+b for a,b in zip(elf, direction[0])]
                proposals[tuple(proposed_pos)].append(elf)
                break
    return proposals


def partOne():
    elves = parseElves()
    
    for round in range(10):
        proposals = makeProposals(elves, round)

        for proposal, proposal_elves in proposals.items():
            if len(proposal_elves) > 1:
                continue
            elves.remove(proposal_elves[0])
            elves.append(proposal)
    
    max_x = max([x[0] for x in elves])
    min_x = min([x[0] for x in elves])
    max_y = max([x[1] for x in elves])
    min_y = min([x[1] for x in elves])
    solution = (max_x-min_x+1) * (max_y-min_y+1) - len(elves)
    print(solution)


partOne()