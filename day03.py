# day03.py

if __name__ == "__main__":
    file_name = 'day03/input.txt'
    letter_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    total_priority = 0

    with open(file_name, "r") as file:
        for row in file:
            row = row.replace('\n', '')
            row_length = len(row)
            half_count = int(row_length/2)
            # print(row_length, half_count)
            first_compartment = row[:half_count]
            second_compartment = row[half_count:]
            # print(row)
            # print(first_compartment, second_compartment)
            letters_found = []
            for letter in first_compartment:
                if letter in letters_found:
                    continue
                if letter in second_compartment:
                    total_priority += letter_list.find(letter) + 1
                    # print(letter, letter_list.find(letter) + 1, total_priority)
                    letters_found.append(letter)

        print(f'Answer 1: {total_priority}')

    total_priority_2 = 0

    with open(file_name, "r") as file:
        all_rucksacks = file.read().split('\n')
        groups = int(len(all_rucksacks)/3)
        
        for group_no in range(groups):
            common_letters = []
            start = group_no * 3
            end = (group_no + 1) * 3
            group_rucksacks = all_rucksacks[start:end]
            for letter in group_rucksacks[0]:
                if letter in group_rucksacks[1] and letter in group_rucksacks[2] \
                    and letter not in common_letters:
                    common_letters.append(letter)
                    total_priority_2 += letter_list.find(letter) + 1
            # print(common_letters, total_priority_2)

        print(f'Answer 2: {total_priority_2}')
