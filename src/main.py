import random

def validate_input(input_num):
    if not input_num.isdigit():
        print('Invalid input. Please enter a number.')
        return False

    input_num = int(input_num)
    if input_num < 1 or input_num > 100:
        print('Your input is out of range. Please enter a number between 1 and 100.')
        return False

    return True


def main():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        input_num = input('Please enter your guess between 1 and 100:')

        if input_num == 'q':
            break
        
        if not validate_input(input_num):
            continue

        input_num = int(input_num)
        if input_num == rand_num:
            print(f'You win! Your score is:{score}')
            wanna_play = input('Do you want to play again? (y/n)')
            if wanna_play == 'y':
                rand_num = random.randint(1, 100)
                score = 100
                continue
            else:
                print('Goodbye!')
                break
        elif input_num > rand_num:
            print('Enter a smaller number.')
        
        else:
            print('Enter a grater number.')

        score -= 10
        score = max(score, 0)


if __name__ == '__main__':
    main()