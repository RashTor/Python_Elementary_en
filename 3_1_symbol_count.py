def char_count(same_string):
    same_string=same_string.lower()
    for char_in_ascii in range(97,123):
        print chr(char_in_ascii)," - ",same_string.count(chr(char_in_ascii))


def main():
    some_string="""Write a simple game guess the number. The program will randomly choose a \n
number within specified range and will wait for user to input a number.  \n
If the number is less or greater than the right one system should tell that to the user.  \n
If the guessed number is correct, then the game is over and the program  \n
should write the number of iterations taken."""
    print "The define string is:\n"+some_string
    char_count(some_string)


if __name__ == '__main__':
    main()