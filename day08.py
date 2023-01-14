# day08.py

def visible_trees(tree_grid):
    columns = len(tree_grid)
    rows = len(tree_grid[0])

    visible = 0
    tree_count = 0
    best_view = 0
    
    for r in range(rows):
        for c in range(columns):
            tree_count += 1
            height = tree_grid[r][c]

            trees_above = [row[c] for row in tree_grid[:r]]
            trees_below = [row[c] for row in tree_grid[r+1:]]
            trees_left = tree_grid[r][:c]
            trees_right = tree_grid[r][c+1:]

            trees_above.reverse()
            trees_left.reverse()

            max_height_above = max(trees_above + [-1])
            max_height_below = max(trees_below + [-1])
            max_height_left = max(trees_left + [-1])
            max_height_right = max(trees_right + [-1])
            
            if height > max_height_above or height > max_height_below or height > max_height_left or height > max_height_right:
                # print('x', end='')
                visible += 1
            # else:
                # print('-', end='')

            view_above = 0
            if len(trees_above) > 0:
                for tree_height in trees_above:
                    view_above += 1
                    if tree_height >= height:
                        break
            # print(view_above, end='')
            view_below = 0
            if len(trees_below) > 0:
                for tree_height in trees_below:
                    view_below += 1
                    if tree_height >= height:
                        break
            # print(view_below, end='')
            view_left = 0
            if len(trees_left) > 0:
                for tree_height in trees_left:
                    view_left += 1
                    if tree_height >= height:
                        break
            # print(view_left, end='')
            view_right = 0
            if len(trees_right) > 0:
                for tree_height in trees_right:
                    view_right += 1
                    if tree_height >= height:
                        break
            # print(view_right, end='')

            view_total = view_above * view_below * view_left * view_right

            if view_total > best_view:
                best_view = view_total
        # print()

    return tree_count, visible, best_view


if __name__ == "__main__":
    file_name = 'day08/input.txt'

    with open(file_name, "r") as file:
        tree_grid = [[int(height) for height in row.strip()] for row in file]
        # print(tree_grid)

    tree_count, visible, best_view = visible_trees(tree_grid)
    first_answer = visible
    second_answer = best_view

    print(f'Answer 1: {first_answer}')

    print(f'Answer 2: {second_answer}')
        
