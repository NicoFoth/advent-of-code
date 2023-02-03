class Sensor():
    def __init__(self, sensor_coords, beacon_coords):
        self.y = sensor_coords[0]
        self.x = sensor_coords[1]
        self.beacon_y = beacon_coords[0]
        self.beacon_x = beacon_coords[1]


    def calculateDistance(self):
        distance = abs(self.y-self.beacon_y) + abs(self.x-self.beacon_x)
        return distance



with open("2022/Day15/input.txt", encoding="utf8") as inputFile:
    inputData = inputFile.read().splitlines()
    sensors = []
    for line in inputData:
        split = line.split(":")
        sensor_split = split[0].replace("Sensor at x=", "").split(", y=")
        sensor_split.append(sensor_split.pop(0))
        sensor_split = [int(x) for x in sensor_split]
        beacon_split = split[1].replace(" closest beacon is at x=", "").split(", y=")
        beacon_split.append(beacon_split.pop(0))
        beacon_split = [int(x) for x in beacon_split]
        s = Sensor(tuple(sensor_split), tuple(beacon_split))
        sensors.append(s)


def partTwo():
    pos_lines = []
    neg_lines = []

    for sensor in sensors:
        dist = sensor.calculateDistance()
        neg_lines.extend([sensor.x + sensor.y - dist, sensor.x + sensor.y + dist])
        pos_lines.extend([sensor.x - sensor.y - dist, sensor.x - sensor.y + dist])

    for i in range(2*len(sensors)):
        for j in range(i+1, 2*len(sensors)):
            a, b = pos_lines[i], pos_lines[j]

            if abs(a - b) == 2:
                pos = min(a, b) + 1

            a, b = neg_lines[i], neg_lines[j]

            if abs(a - b) == 2:
                neg = min(a, b) + 1
    x, y = (pos + neg) // 2, (neg-pos) // 2
    solution = x * 4000000 + y
    print(solution)


partTwo()
