count = 0
ans_str = input()
try:
    ans = int(ans_str)
    if ans < 0 or ans > 50:
        print("Error: number out of range")
        print("You guessed 0 times.")
        exit()
except ValueError:
    if ans_str.replace('.', '', 1).lstrip('-').isdigit():
        print("Error: please enter an integer")
    else:
        print("Error: please enter a number")
    print("You guessed 0 times.")
    exit()

while True:
    guess_str = input()
    try:
        guess = int(guess_str)
        if guess < 0 or guess > 50:
            print("Error: number out of range")
            count += 1
        elif guess < ans:
            print("You are too low!")
            count += 1
        elif guess > ans:
            print("You are too high!")
            count += 1
        else:
            print("You got it!")
            count += 1
            break
    except ValueError:
        if guess_str.replace('.', '', 1).lstrip('-').isdigit():
            print("Error: please enter an integer")
        else:
            print("Error: please enter a number")
        count += 1

print(f"You guessed {count} times.")
