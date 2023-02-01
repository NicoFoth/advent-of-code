with open("2022/Day15/input.txt") as inputFile:
    input = inputFile.read().splitlines()
    sensors = set()
    for line in input:
        split = line.split(":")
        sensor_split = split[0].replace("Sensor at x=", "").split(", y=")
        sensor_split.append(sensor_split.pop(0))
        sensor_split = [int(x) for x in sensor_split]
        beacon_split = split[1].replace(" closest beacon is at x=", "").split(", y=")
        beacon_split.append(beacon_split.pop(0))
        beacon_split = [int(x) for x in beacon_split]
        sensors.add((tuple(sensor_split), tuple(beacon_split)))


def calculateDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = abs(x1-x2)+abs(y1-y2)
    return distance


def partOne():
    row = 2000000
    environment = set()
    beacons = set([x[1] for x in sensors if x[1][0] == row])
    for sensor in sensors:

        beacon_distance = calculateDistance(sensor[0], sensor[1])
        distanceToRow = beacon_distance - abs(row - sensor[0][0])
        
        for column in range(sensor[0][1]-distanceToRow, sensor[0][1]+distanceToRow+1):
            environment.add((row, column))
    
    print(len(environment) - len(beacons))


partOne()