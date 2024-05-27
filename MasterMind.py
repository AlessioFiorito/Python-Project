
import random

letters = ["R", "B", "Y", "W", "O", "P"]
tries = 10
code_length = 4

def generate_code():
    code = []
    for _ in range(code_length):
        ltr = random.choice(letters)
        code.append(ltr)
    return code

def guess_code():
    while True:
        guess = input("Guess the code: ").upper().split()  # split() to ignore spaces

        if len(guess) != code_length:
            print(f"Code must be {code_length} letters!")
            continue

        for ltr in guess:
            if ltr not in letters:
                print(f"Invalid letter: {ltr}. Valid letters are: {', '.join(letters)}. Try again.")
                break
        else:
            return guess

def check_code(guess, real_code):
    ltr_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for ltr in real_code:
        if ltr not in ltr_count:
            ltr_count[ltr] = 0
        ltr_count[ltr] += 1

    for guess_ltr, real_ltr in zip(guess, real_code):
        if guess_ltr == real_ltr:
            correct_pos += 1
            ltr_count[guess_ltr] -= 1

    for guess_ltr, real_ltr in zip(guess, real_code):
        if guess_ltr != real_ltr and guess_ltr in ltr_count and ltr_count[guess_ltr] > 0:
            incorrect_pos += 1
            ltr_count[guess_ltr] -= 1

    return correct_pos, incorrect_pos

def game():
    code = generate_code()
    print(f"Welcome to Mastermind, you have {tries} tries to guess the code!")
    print("The valid letters are: ", " ".join(letters))
    
    for attempt in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print(f"You guessed the code in {attempt} tries! The code was: {' '.join(code)}")
            break
        else:
            print(f"Correct positions: {correct_pos}, Incorrect positions: {incorrect_pos}")

    else:
        print(f"You ran out of tries! The code was: {' '.join(code)}")

if __name__ == "__main__":
    game()







