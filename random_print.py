import argparse
import random


# The function to shuffle the numbers and print
def shuffle_and_print(start, end):
    numbers = list(range(start, end+1))
    random.shuffle(numbers)
    print("### Here is the list of numbers in random order ###")
    for num in numbers:
        print (num)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print random numbers within a specified range.')
    parser.add_argument('-s', '--start', type=int, help='Starting number', default=1)
    parser.add_argument('-e', '--end', type=int, help='Ending number', default=10)
    args = parser.parse_args()

    start = args.start
    end = args.end

    shuffle_and_print(start, end)
