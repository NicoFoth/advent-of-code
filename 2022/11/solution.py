with open("2022/Day11/input.txt") as inputFile:
    input = inputFile.read().splitlines()

class Monkey():
    def __init__(self, id, items, worry_operation, divisibility_condition, test_true, test_false):
        self.id = id
        self.items = items
        self.worry_operation = worry_operation
        self.divisibility_condition = divisibility_condition
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0

def generate_monkeys():
    monkeys = []
    for line_index in range(len(input)):
        if input[line_index].startswith("Monkey"):
            monkeys.append(Monkey(
                id=len(monkeys),
                items=input[line_index+1].lstrip().replace("Starting items: ", "").split(", "),
                worry_operation=input[line_index+2].replace("Operation: new = ", ""),
                divisibility_condition=int(input[line_index+3].replace("Test: divisible by ", "")),
                test_true=int(input[line_index+4].replace("If true: throw to monkey ", "")),
                test_false=int(input[line_index+5].replace("If false: throw to monkey ", "")),
            ))
    return monkeys


def one():
    local_monkeys = generate_monkeys()
    for round in range(20):
        for monkey in local_monkeys:
            for item_index in range(len(monkey.items)):
                monkey.inspections += 1
                old = int(monkey.items[item_index])
                new = eval(monkey.worry_operation)
                worry_level = new // 3
                if worry_level % monkey.divisibility_condition == 0:
                    local_monkeys[monkey.test_true].items.append(worry_level)
                else:
                    local_monkeys[monkey.test_false].items.append(worry_level)
            monkey.items.clear()
    
    inspection_counts = []
    for monkey_object in local_monkeys:
        inspection_counts.append(monkey_object.inspections)
    inspection_counts.sort(reverse=True)
    print(inspection_counts[0]*inspection_counts[1])


def two():
    prime_factor_shit = 9699690
    local_monkeys = generate_monkeys()
    for round in range(10000):
        for monkey in local_monkeys:
            for item_index in range(len(monkey.items)):
                monkey.inspections += 1
                old = int(monkey.items[item_index])
                new = eval(monkey.worry_operation)
                worry_level = new % prime_factor_shit
                if worry_level % monkey.divisibility_condition == 0:
                    local_monkeys[monkey.test_true].items.append(worry_level)
                else:
                    local_monkeys[monkey.test_false].items.append(worry_level)
            monkey.items.clear()
    
    inspection_counts = []
    for monkey_object in local_monkeys:
        inspection_counts.append(monkey_object.inspections)
    inspection_counts.sort(reverse=True)
    print(inspection_counts[0]*inspection_counts[1])


one()
two()