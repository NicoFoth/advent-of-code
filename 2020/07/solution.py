# (input line removed)

file = open("input.txt")

input_raw = file.readlines()
input = [x.strip(".\n") for x in input_raw]

bag_dict = {}
for bag in input:
    bag_split = bag.split("bags contain")
    bag_dict[bag_split[0]] = bag_split[1]


valid_bags = set()
def partOne():
    findParentBag("shiny gold")
    print(len(valid_bags))

def findParentBag(goal_bag):
    for key in bag_dict:
        content = bag_dict[key]
        if goal_bag in content:
            findParentBag(key)
            valid_bags.add(key)
    return


partOne()
def recursionTry(bag_dict_two):
    for key in bag_dict_two:
        contents = bag_dict_two[key]
        for item in contents:
            for key in bag_dict_two:
                if item != key:
                    pass
                else:
                    break
            else:
                for rule in input:
                        if rule.startswith(item[2:]):
                            bag_split = rule.split("bags contain")
                            contents = bag_split[1].lstrip().split(", ")
                            bag_dict_two[item] = contents
                            recursionTry(bag_dict_two)
                            return bag_dict_two

def recursionTryTwo(result, new_result):
    for key in result:
        contents = result[key]
        for element in contents:
            if element != "no other bags":
                new_result[int(element[0])] = recursionTryTwo(new_result, new_result)
            else:
                return new_result

def partTwo(input):
    bag_dict_two = {}
    for rule in input:
        if rule.startswith("shiny gold"):
            bag_split = rule.split("bags contain")
            bag_dict_two[bag_split[0]] = bag_split[1].lstrip().split(", ")
            break
    
    result = recursionTry(bag_dict_two)

    total_bags = 0
    new_result = {}
    new_result = recursionTryTwo(result, new_result)
    
    print(result)



partTwo(input)