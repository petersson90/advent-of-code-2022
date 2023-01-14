# day10.py

def signal_strength(cycle, value_X):
    if (cycle - 20) % 40 != 0:
        return 0
    
    # print(cycle, value_X)    
    return cycle * value_X

def draw_CRT(cycle, value_X):
    position = cycle - int((cycle-1)/40) * 40 - 1
    if position > value_X + 1 or position < value_X - 1:
        return '.'
    return '#'

def add_cycle(cycle, value_X, sum_signal, CRT_drawing):
    cycle += 1
    sum_signal += signal_strength(cycle, value_X)
    CRT_row = int((cycle-1)/40)
    if len(CRT_drawing) < CRT_row + 1:
        CRT_drawing.append([])
        print(CRT_drawing)
    CRT_drawing[CRT_row].append(draw_CRT(cycle, value_X))
    return cycle, sum_signal, CRT_drawing

if __name__ == "__main__":
    file_name = 'day10/input.txt'

    cycle = 0
    value_X = 1
    sum_signal = 0
    CRT_drawing = []

    with open(file_name, 'r') as file:
        for row in file:
            cycle, sum_signal, CRT_drawing = add_cycle(cycle, value_X, sum_signal, CRT_drawing)
            if row.split()[0] == 'addx':
                cycle, sum_signal, CRT_drawing = add_cycle(cycle, value_X, sum_signal, CRT_drawing)
                value_X += int(row.split()[1])
    
    for row in CRT_drawing:
        print(''.join(row))
            
    first_answer = sum_signal

    print(f'Answer 1: {first_answer}')

    # print(f'Answer 2: {second_answer}')
