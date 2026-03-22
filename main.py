# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def get_random_number():
    random_int = random.randint(1, 100)
    return random_int

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target = get_random_number()
    print("guess the number 0-100")
    num = -1
    count = 0
    while num != target:
        num = int(input("put number: "))
        count = count + 1
        if num < target:
            print("this number is less. Try again.")
        elif num > target:
            print("this number is bigest. Try again")
        else:
            print(f"congratulation! Your attemps is {count}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
