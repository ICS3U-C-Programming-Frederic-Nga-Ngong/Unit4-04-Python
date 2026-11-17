#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Check if an number is the correct guess or not

import random


def main():

    random_variable = random.randint(1, 9)  # a number between 1 and 9

    while True:

        # Get number from he user
        usernum_str = input("\nEnter a number between 0 and 9 : ")
        try:

            # Cast it into an integer
            user_num = int(usernum_str)

            # Check if the number is equal to the random number
            if user_num == random_variable:
                print("{} is the correct guess.".format(user_num))
                break

            # Appears when the casting failed
            else:
                print(
                    "{} is not the correct guess. Please, enter a new number".format(
                        user_num
                    )
                )
        except ValueError:
            print(
                "{} is not a valid number. Please, enter a new one".format(usernum_str)
            )
            break


if __name__ == "__main__":

    main()
