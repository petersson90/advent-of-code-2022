# day04.py

if __name__ == "__main__":
    file_name = 'day04/input.txt'

    full_overlaps = 0
    overlaps = 0

    with open(file_name, "r") as file:
        for row in file:
            row = row.replace('\n', '')
            parts = row.split(',')
            first_low = int(parts[0].split('-')[0])
            first_high = int(parts[0].split('-')[1])
            second_low = int(parts[1].split('-')[0])
            second_high = int(parts[1].split('-')[1])
            first_range = range(first_low, first_high+1)
            second_range = range(second_low, second_high+1)
            # print(first_low, first_high, second_low, second_high)

            if (first_low in second_range and first_high in second_range):
                # print(second_range)
                # print(f'Second range fully overlaps first.')
                full_overlaps += 1
            elif (second_low in first_range and second_high in first_range):
                # print(first_range)
                # print(f'First range fully overlaps second.')
                full_overlaps += 1

            if (first_low in second_range or first_high in second_range):
                # print(second_range)
                # print(f'Second range overlaps first.')
                overlaps += 1
            elif (second_low in first_range or second_high in first_range):
                # print(first_range)
                # print(f'First range overlaps second.')
                overlaps += 1

        print(f'Answer 1: {full_overlaps}')

        print(f'Answer 2: {overlaps}')
