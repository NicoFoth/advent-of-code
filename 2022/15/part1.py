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


class Sensor():
    def __init__(self, sensor_coords, beacon_coords):
        self.y = sensor_coords[0]
        self.x = sensor_coords[1]
        self.beacon_y = beacon_coords[0]
        self.beacon_x = beacon_coords[1]


    def calculateDistance(self):
        distance = abs(self.y-self.beacon_y) + abs(self.x-self.beacon_x)
        return distance


def partOne():
    row = 2000000
    environment = set()
    beacons = set([x[1] for x in sensors if x[1][0] == row])
    for sensor in sensors:

        s = Sensor(sensor[0], sensor[1])
        distance = s.calculateDistance()
        distanceToRow = distance - abs(row - s.y)
        
        for column in range(s.x-distanceToRow, s.x+distanceToRow+1):
            environment.add((row, column))
    
    print(len(environment) - len(beacons))


partOne()