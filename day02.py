# day02.py

if __name__ == "__main__":
    file_name = 'day02/input.txt'

    points = {
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3   # Scissors
    }

    map_plays = {
        'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},  # Win
        'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},  # Draw
        'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'}   # Loss
    }

    with open(file_name, "r") as file:
        total_score = 0
        total_score_2 = 0

        for row in file:
            play = tuple(row.split())
            # print(play)
            if play == ('A', 'Y') or play == ('B', 'Z') or play == ('C', 'X'):
                total_score += 6
            elif play == ('A', 'X') or play == ('B', 'Y') or play == ('C', 'Z'):
                total_score += 3
            
            if play[1] == 'Z':
                total_score_2 += 6
            elif play[1] == 'Y':
                total_score_2 += 3
            
            total_score += points[play[1]]
            # print(total_score)

            your_move = map_plays[play[1]][play[0]]
            
            total_score_2 += points[your_move]
            # print(total_score_2)

        print(f'Answer 1: {total_score}')

        print(f'Answer 2: {total_score_2}')
