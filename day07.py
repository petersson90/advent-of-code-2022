# day07.py

def build_file_structure(directory, file_structure={}):
    pass

if __name__ == "__main__":
    file_name = 'day07/input.txt'

    with open(file_name, "r") as file:
        directory = []
        file_structure = {}
        for row in file:
            content = row.strip()
            # print(content)
            info = content.split()
            if info[0] == '$':
                if info[1] == 'cd':
                    if info[2] == '/':
                        directory = ['/']
                    elif info[2] == '..':
                        directory.pop()
                    else:
                        directory.append(info[2])
                    # print(directory)
                continue
            if info[0] == 'dir':
                continue
            current_dir = ''
            for dir in directory:
                current_dir += dir
                if current_dir != '/':
                    current_dir += '/'
            # current_dir = '/' + '/'.join(directory)
                file_structure[current_dir] = file_structure.get(current_dir, [])
                file_structure[current_dir].append((info[1], int(info[0])))
    print(file_structure)

    directories = []
    first_answer = 0

    total_disk_space = 70000000
    min_unused_space = 30000000
    used_space = sum([file_size for _, file_size in file_structure['/']])
    min_space_to_delete = min_unused_space-(total_disk_space-used_space)
    min_folder_size = total_disk_space

    for directory, content in file_structure.items():
        # print(directory, file_size_sum)
        file_size_sum = sum([file_size for _, file_size in content])
        if file_size_sum <= 100000:
            first_answer += file_size_sum

        if file_size_sum < min_folder_size and file_size_sum >= min_space_to_delete:
            directory_to_delete = directory
            min_folder_size = file_size_sum

        second_answer = min_folder_size

    print(f'Answer 1: {first_answer}')

    print(f'Answer 2: {second_answer} ({directory_to_delete})')
        
