import random


def run_guess(guess, ans):
    if 0 < guess < 11:
        if guess == ans:
            print(f'Nice! You got it! It was {ans}!')
            return True
    else:
        print(f'Bruh, I meant a number from 1 to 10')
        return False


if __name__ == '__main__':
    ans = random.randint(1, 10)
    print(ans)
    while True:
        try:
            guess = int(input('Enter a number 1 - 10: '))
            if (run_guess(guess, ans)):
                break
        except ValueError:
            print('Please Enter a Number')
            continue
