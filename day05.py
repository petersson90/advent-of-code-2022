# day05.py

def stack_creator(stacks):
    stacks = stacks.split('\n')
    n = len(stacks[0])
    # print(n)
    i = 0
    stack_dict = {}
    while i < n:
        stack_no = stacks[-1][i+1:i+2]
        stack_dict[stack_no] = []
        for row in stacks[:len(stacks)-1]:
            # print(row)
            value = row[i+1:i+2]
            if value == ' ':
                continue
            # print(value)
            stack_dict[stack_no].append(value)
        i += 4
    for _, stack in stack_dict.items():
        stack.reverse()
    return stack_dict

def move_9000(move_list, stack_dict):
    move_list = move_list.replace('move ', '').replace('from ', '').replace('to ', '')
    move_count, from_stack, to_stack = move_list.split()

    for _ in range(int(move_count)):
        value_to_move = stack_dict[from_stack][-1]
        # print(stack_dict[from_stack], '=>', stack_dict[to_stack])
        stack_dict[to_stack].append(value_to_move)
        stack_dict[from_stack].pop()
        # print(f'{value_to_move} moved from stack {from_stack} to {to_stack}')
        # print(stack_dict[from_stack], '=>', stack_dict[to_stack])
        # print()
    
    return stack_dict
    
def move_9001(move_list, stack_dict):
    move_list = move_list.replace('move ', '').replace('from ', '').replace('to ', '')
    move_count, from_stack, to_stack = move_list.split()
    move_count = int(move_count)

    values_to_move = stack_dict[from_stack][-move_count:]
    stack_dict[to_stack] += values_to_move
    stack_dict[from_stack] = stack_dict[from_stack][:-move_count]
    
    return stack_dict

if __name__ == "__main__":
    file_name = 'day05/input.txt'

    with open(file_name, "r") as file:
        stacks, steps = file.read().split('\n\n')
        stack_dict = stack_creator(stacks)
        print(stack_dict)
        stack_dict2 = stack_creator(stacks)
        print(steps)
        steps = steps.split('\n')
        for step in steps:
            move_9000(step, stack_dict)
            move_9001(step, stack_dict2)

        first_answer = ''
        for _, stack in stack_dict.items():
            first_answer += stack[-1]
        
        second_answer = ''
        for _, stack2 in stack_dict2.items():
            if stack2 == []:
                continue
            second_answer += stack2[-1]


        print(f'Answer 1: {first_answer}')

        print(f'Answer 2: {second_answer}')
