# day09.py

def move(instruction, head_position, tail_position, previous_tail_positions: list):
    direction = instruction[0]
    distance = instruction[1]
    print(direction, distance)

    x, y = head_position
    for _ in range(distance):
        print(f'H: {head_position} -> ', end='')
        if direction == 'R': x += 1
        elif direction == 'U': y += 1
        elif direction == 'L': x -= 1
        elif direction == 'D': y -= 1
    
        head_position = (x, y)
        print(f'{head_position}')
        tail_position, previous_tail_positions = move_tail(tail_position, head_position, previous_tail_positions)

    return head_position, tail_position, previous_tail_positions

def move_tail(taiL_position, head_position, previous_tail_positions: list):
    tail_x, tail_y = taiL_position
    head_x, head_y = head_position

    
    print(f'T: {taiL_position} -> ', end='')

    if head_x == tail_x:
        if abs(head_y - tail_y) > 1:
            if head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1
    elif head_y == tail_y:
        if abs(head_x - tail_x) > 1:
            if head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1
    elif abs((head_x - tail_x) * (head_y - tail_y)) > 1:
        if head_x > tail_x and head_y > tail_y:
            tail_x += 1
            tail_y += 1
        elif head_x < tail_x and head_y < tail_y:
            tail_x -= 1
            tail_y -= 1
        elif head_x > tail_x and head_y < tail_y:
            tail_x += 1
            tail_y -= 1
        else:
            tail_x -= 1
            tail_y += 1

    tail_position = (tail_x, tail_y)
    print(f'{tail_position}')
    if tail_position not in previous_tail_positions:
        previous_tail_positions.append(tail_position)

    return tail_position, previous_tail_positions


if __name__ == "__main__":
    file_name = 'day09/input.txt'

    with open(file_name, "r") as file:
        instructions = [(row.split()[0], int(row.split()[1])) for row in file]
    
    head_position = (0, 0)
    tail_position = (0, 0)
    previous_tail_positions = []
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for instruction in instructions:
        head_position, tail_position, previous_tail_positions = move(instruction, head_position, tail_position, previous_tail_positions)
        
    print(f'{len(previous_tail_positions)}: {previous_tail_positions}')
        

    #     if y > max_y:
    #         max_y = y
    #     elif y < min_y:
    #         min_y = y
    #     if x > max_x:
    #         max_x = x
    #     elif x < min_x:
    #         min_x = x
    # columns = max_x - min_x
    # rows = max_y - min_y
    # for r in range(rows):
    #     for c in range(columns):
    #         print('.', end='')
    #     print()
        
        
        

    #         first_answer = find_start(buffer)
    #         second_answer = find_start(buffer, 14)


    # print(f'Answer 1: {first_answer}')

    # print(f'Answer 2: {second_answer}')
        
