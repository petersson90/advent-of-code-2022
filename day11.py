# day11.py

def get_monkey(record, monkeys):
    details = [row.strip() for row in record.split('\n')]
    # print(details)
    
    for row in details:
        if row.startswith('Monkey'):
            monkey_no = row.replace('Monkey ', '').replace(':', '')
            monkeys[monkey_no] = {}
        else:
            identifier = row[:row.find(':')]
            words = identifier.split(' ')
            monkeys[monkey_no][words[-1]] = row.replace(identifier + ': ', '')
        
    monkeys[monkey_no]['items'] = [int(item) for item in monkeys[monkey_no]['items'].split(', ')]
    monkeys[monkey_no]['Operation'] = monkeys[monkey_no]['Operation'].replace('new = ', '')
    monkeys[monkey_no]['Test'] = int(monkeys[monkey_no]['Test'].replace('divisible by ', ''))
    monkeys[monkey_no]['true'] = monkeys[monkey_no]['true'].replace('throw to monkey ', '')
    monkeys[monkey_no]['false'] = monkeys[monkey_no]['false'].replace('throw to monkey ', '')

    return monkeys

if __name__ == "__main__":
    file_name = 'day11/input_test.txt'

    with open(file_name, 'r') as file:
        file_contents = file.read()

    monkeys = {}
    for record in file_contents.split('\n\n'):
        monkeys = get_monkey(record, monkeys)

    # print(monkeys)
    for round in range(1):
        print(round)
        for monkey_no, monkey_details in monkeys.items():
            items_to_inspect = len(monkey_details['items'])
            # print(f'Monkey {monkey_no}: {items_to_inspect}')
            monkey_details['inspections'] = monkey_details.get('inspections', 0) + items_to_inspect
            
            for item in monkey_details['items']:
                old = item
                new = eval(monkey_details['Operation'])
                # new = int(new / 3)
                if new % monkey_details['Test'] == 0:
                    throw_to_monkey = monkey_details['true']
                else:
                    throw_to_monkey = monkey_details['false']
                # print(f'Item with value {new} -> {throw_to_monkey}')
                monkeys[throw_to_monkey]['items'].append(new)
            monkey_details['items'] = []
                

        for monkey_no, monkey_details in monkeys.items():
            items = [str(item) for item in monkey_details['items']]
            items = ', '.join(items)
            inspections = monkey_details['inspections']
            # print(f'Monkey {monkey_no}: {items}')
            print(f'Monkey {monkey_no}: {inspections}')
    
    inspections = []
    for monkey_no, monkey_details in monkeys.items():
        inspections.append(monkey_details['inspections'])
    
    inspections.sort(reverse=True)
    first_answer = 1
    for inspection in inspections[:2]:
        first_answer *= inspection


    print(f'Answer 1: {first_answer}')
