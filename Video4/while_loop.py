import random

# 1. choose random number
random_number = random.randint(0, 1000)
user_input = -1
has_quit = False

# 2. while user  doesn't find the numer
while user_input != random_number:

    # 2.1. ask the user the number
    instruction = input("what is the secret number? [Q: Quit] ") 
    if not instruction.isnumeric():
        if instruction == "Q":
            has_quit = True
            break
        else:
            print("Please, enter a number or Q for quit the game")
            continue
        
    user_input = int(instruction)

    # 2.2. if the number is too small, print the message "The number is bigger"
    if user_input < random_number:
        print("The secret number is bigger")
    # 2.3. if the number is too big, print the message "The number is smaller"
    if user_input > random_number:
        print("The secret number is smaller")

# 3. congratulate the user when he find the good number
if has_quit:
    print("You quit the game")
else:
    print("Congratulation, you found the secret number.")


