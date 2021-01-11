"""
File: boggle.py
Name: Kevin Fang
----------------------------------------
TODO:
"""
import copy

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    # Set up boggle board
    boggle = []
    for i in range(1, 3):
        i = input(f'{i} row of letters: ')
        lst = i.split()
        boggle.append(lst)

    find_words(boggle)


def find_words(boggle):
    set_permutations = get_permutations(boggle)
    print(f'Searching from dictionary...')
    read_dictionary(set_permutations)


def get_permutations(boggle):
    # ignore duplicate word in permutation list
    set_permutations = set()
    # read the row and column char from boggle board
    for row in range(2):
        for column in range(2):
            words = words_from(boggle, row, column, lst_word=[])
            if words:
                for word in words:
                    set_permutations.add(word)
            words = None
    return sorted(list(set_permutations))


def words_from(boggle, row, column, current='', lst_word=[]):
    if row in (2, -1) or column in (2, -1):
        return
    if len(current) > 2:
        return
    if boggle[row][column] != '-':
        new_string = current + boggle[row][column]
        new_boggle = copy.deepcopy(boggle)
        new_boggle[row][column] = '-'
        if len(new_string) >= 1:
            lst_word.append(new_string.lower())
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x, y in neighbors:
            words_from(new_boggle, row + x, column + y, new_string, lst_word)
        return lst_word


def read_dictionary(set_permutations):

    word_dict = []
    with open('dictionary.txt') as f:
        for line in f:
            line = line.strip()
            word_dict += line.split(',')

    count = 0
    for ans in set_permutations:
        if ans.lower() in word_dict:
            count += 1
            print(ans)
    print(f'Total founds {count} words')


if __name__ == '__main__':
    main()
