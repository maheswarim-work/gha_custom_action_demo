# Create a function that create a random word of specified length
import os
import random
import string


def main():
    length = 5 #if os.environ['INPUT_WORD_LENGTH']
    letters = string.ascii_lowercase
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "w") as f:
            print("{}={}".format("random_word", ''.join(random.choice(letters) for i in range(length))), file=f)


if __name__ == '__main__':
    main()
