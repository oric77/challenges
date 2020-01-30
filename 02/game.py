#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random

NUM_LETTERS = 7

# get an iterable dictionary of words, return dict of lists of words of same size sorted alphapetically
# keys are strings si
def split_by_len(sort_dict = None):
    if not sort_dict:
        sort_dict = sorted(DICTIONARY, key=len)

    buckets_list = {}
    next_list = []
    size = 1
    for word in sort_dict:
        if len(word) == size:
            next_list.append(word)
        else:
            next_list.sort()
            buckets_list[size] = next_list
            size = len(word)
            next_list = [word]

    next_list.sort()
    buckets_list[size] = next_list
    return buckets_list

SORTED_DICT = split_by_len()

def is_word_in_dict(in_word, mydict = None):
    if not mydict:
        mydict = SORTED_DICT

    for word in mydict[len(word)]:
        if in_word == word:
            return True
        elif in_word < word:
            return False

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def get_best_word(use_letters):


def game():
    use_letters = random.choices(POUCH, k=NUM_LETTERS)
    user_word_score = 0
    user_word = input(f"Welcome to Scrabble, please for a word out of these letters: {use_letters}:\n").upper()

    # validate user input
    if not all(l in use_letters for l in user_word):
        print("You used letters which are not in the provided set")
    elif user_word not in DICTIONARY:
        print("Your word does not exist in the dictionary")
    else:
        # calculate and print user results
        user_word_score = calc_word_value(user_word)
        print(f"Your word score is: {user_word_score}")

    # calculate and print machines result and final scores
    best_word = get_best_word(use_letters)
    best_word_score = calc_word_value(best_word)
    print(f"Best word is: {best_word} with value {best_word_score}")
    print(f"Your final score is: {user_word_score/best_word_score}")


def main():
    game()


if __name__ == "__main__":
    main()
