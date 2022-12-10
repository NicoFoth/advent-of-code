with open("input.txt") as inputFile:
    input = inputFile.read().splitlines()


def one():
    count = 0
    for row_index in range(len(input)):
        for tree_index in range(len(input[row_index])):
            tree_height = input[row_index][tree_index]
            visible_left = True
            visible_right = True
            visible_top = True
            visible_bottom = True
            for other_tree_index in range(len(input[row_index])):
                if other_tree_index == tree_index:
                    continue
                if input[row_index][other_tree_index] >= tree_height:
                    if other_tree_index < tree_index:
                        visible_left = False
                    else:
                        visible_right = False
            for other_row_index in range(len(input)):
                if other_row_index == row_index:
                    continue
                if input[other_row_index][tree_index] >= tree_height:
                    if other_row_index < row_index:
                        visible_top = False
                    else:
                        visible_bottom = False
            if visible_top == True or visible_bottom == True or visible_left == True or visible_right == True:
                count += 1
    print(count)


def two():
    highest_scenic_score = 0
    for row_index in range(len(input)):
            for tree_index in range(len(input[row_index])):
                tree_height = input[row_index][tree_index]
                viewing_distance_top = 0
                viewing_distance_bottom = 0
                viewing_distance_left = 0
                viewing_distance_right = 0

                # Viewing distance to the right
                for i in range(tree_index+1, len(input[row_index])):
                    viewing_distance_right += 1
                    if input[row_index][i] >= tree_height:
                        break

                # Viewing distance to the left
                for i in range(1, tree_index+1):
                    viewing_distance_left += 1
                    if input[row_index][tree_index-i] >= tree_height:
                        break

                # Viewing distance to the bottom
                for i in range(row_index+1, len(input)):
                    viewing_distance_bottom += 1
                    if input[i][tree_index] >= tree_height:
                        break
                
                # Viewing distance to the top
                for i in range(1, row_index+1):
                    viewing_distance_top += 1
                    if input[row_index-i][tree_index] >= tree_height:
                        break
                
                current_scenic_score = viewing_distance_top * viewing_distance_bottom * viewing_distance_right * viewing_distance_left
                if current_scenic_score > highest_scenic_score:
                    highest_scenic_score = current_scenic_score

    print(highest_scenic_score)


one()
two()