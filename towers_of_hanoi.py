'''
Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.
The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.
The game follows three rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    3. No disk may be placed on top of a smaller disk.
'''

'''
This version adopts an example given by a user on the codecademy site. 
URL: https://discuss.codecademy.com/t/towers-of-hanoi-graphic-well-ascii-graphic-output/404060
'''
from stack import Stack

print("\nLet's play Towers of Hanoi!!!")

# Create the stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]

# Set up the game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {moves} moves.".format(moves=optimal_moves))

# Get user input

def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {ltr} for {nme}".format(ltr=letter, nme=name))
        
        user_input = input("")

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Play the game

def print_pix():
    # render current state as a list of lists of values
    show_list = []
    for stack in stacks:
        show_list.append(stack.print_items())
    # pad lists with leading zeros so all are length = num_disks
    for idx, item in enumerate(show_list):
        new_list = [0 for i in range(num_disks -len(item))]
        show_list[idx] = new_list + show_list[idx]
    # print num_disks lines, each comprised of
    # ... three columns, corresponding to "L", "M", and "R".
    # ... Each column will consist of a number of underscores
    # ... corresponding to the value of the node at that level.
    for i in range(num_disks):
        for item in show_list:
            mult = item[i]
            s = "_" * mult
            print("{:10}".format(s), end = '')
        print()
    print("{:10}{:10}{:10}\n".format("L","M","R"))

num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n...Current Stacks...")
    print_pix()
    # for stack in stacks:
    #     stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\n\nInvalid Move.  This stack is currently empty. Try Again.")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk.get_value())
            num_user_moves += 1
            break
        else:
            print("\nInvalid Move. Try Again.")

print("\nYou completed the game in {moves} moves, and the optimal number of moves is {optimal_moves}.".format(moves=num_user_moves, optimal_moves=optimal_moves))

''' Test / Debug Statements '''
#print(stacks)
#left_stack.print_items()
