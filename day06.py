# day06.py

def find_start(buffer, length=4):
    last_four = []
    for i, letter in enumerate(buffer):
        # print(i)
        last_four.append(letter)
        if len(last_four) > length:
            del last_four[0]
            list_count = []
            for char in last_four:
                list_count.append(last_four.count(char))
            if list_count == [1 for _ in range(length)]:
                return i + 1 #, last_four

        # print(last_four)

if __name__ == "__main__":
    file_name = 'day06/input.txt'

    with open(file_name, "r") as file:
        for row in file:
            buffer = row.strip()
            first_answer = find_start(buffer)
            second_answer = find_start(buffer, 14)


    print(f'Answer 1: {first_answer}')

    print(f'Answer 2: {second_answer}')
        
