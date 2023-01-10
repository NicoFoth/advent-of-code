with open("2022/Day16/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def takeAction(timeLeft, currentValve, connectedValves, totalFlow=0, currentFlow=0, openedValves = []):
    if timeLeft == 0:
        return totalFlow
    if currentValve not in openedValves:
        totalFlow += currentFlow
        currentFlow += connectedValves[currentValve][0]
        openedValves.append(currentValve)
        timeLeft -= 1
        return takeAction(timeLeft, currentValve, connectedValves, totalFlow, currentFlow, openedValves)
    else:
        for valve in connectedValves[currentValve][1]:
            if valve not in openedValves:
                totalFlow += currentFlow
                timeLeft -= 1
                return takeAction(timeLeft, valve, connectedValves, totalFlow, currentFlow, openedValves)
            

def partOne():
    valve_dict = {}
    for valve in input:
        connectedValves = valve.split("valve")[1]
        if connectedValves.startswith("s"):
            connectedValves = connectedValves[2:].split(", ")
        else:
            connectedValves = [connectedValves[1:]]
        valve_split = valve.split()
        valve_dict[valve_split[1]] = (int(valve_split[4].strip("rate=;")), connectedValves)
    print(takeAction(30, "AA", valve_dict))


partOne()