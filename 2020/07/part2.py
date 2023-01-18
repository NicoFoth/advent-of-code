with open("2020/Day7/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    rules = {}
    for rule in input:
        outer_bag, inner_bags =  rule.split(" bags contain ")
        inner_bags = inner_bags.split(", ")
        rules[outer_bag] = inner_bags


def getInnerBags(outer_bag):
    contents = rules[outer_bag]
    if "no other bags." in contents:
        return 0

    bag_amount = 0
    for content in contents:
        amount = int(content[:1])
        inner_bag = content[2:].split(" bag")[0]
        bag_amount += amount * getInnerBags(inner_bag) + amount
    return bag_amount


def partTwo():
    start = "shiny gold"
    res = getInnerBags(start)
    print(res)


partTwo()