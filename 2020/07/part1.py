with open("2020/Day7/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    bag_dict = {}
    for bag in input:
        bag_split = bag.split("bags contain")
        bag_dict[bag_split[0]] = bag_split[1]


def findParentBag(goal_bag, valid_bags=set()):
    for key, content in bag_dict.items():
        if goal_bag in content:
            findParentBag(key, valid_bags)
            valid_bags.add(key)
    return valid_bags


def partOne():
    valid_bags = findParentBag("shiny gold")
    print(len(valid_bags))


partOne()
