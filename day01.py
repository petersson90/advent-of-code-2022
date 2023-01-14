# day01.py

if __name__ == "__main__":
    file_name = 'day01/input.txt'
    with open(file_name, "r") as file:
        elf_list = [sum([int(value) for value in elf.split('\n') if value != '']) for elf in file.read().split('\n\n')]

        print(f'Answer 1: {max(elf_list)}')

        elf_list.sort(reverse=True)
        print(f'Answer 2: {sum(elf_list[:3])}')

