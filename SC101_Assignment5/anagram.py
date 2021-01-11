"""
File: anagram.py
Name: Kevin Fang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

word_dict = []                # Global to store the word from dictionary
count = 0                     # Global to counts the numbers of anagrams
double_ans = []               # Global list to stores anagrams


def main():
    global count, double_ans
    while True:
        print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
        s = input(f'Find anagram for:')
        count = 0
        double_ans = []
        if s == EXIT:
            break
        else:
            read_dictionary()
            print('Searching...')
            find_anagrams(s)
        print(f"{count} anagrams found: {double_ans}")


#   The function read dictionary and store to list word_dict
def read_dictionary():
    global word_dict
    with open('dictionary.txt') as f:
        for line in f:
            line = line.strip()
            word_dict += line.split(',')


def find_anagrams(s):
    """
    :param s: get s from user input to find anagrams
    :return: the function return nothing
    """
    current = []
    for ele in s:
        current += ele
    find_anagrams_helper(s, current, [], word_dict)


def find_anagrams_helper(s, current, search, word_dicts):
    """
    :param s: helper function to get user input to find anagrams
    :param current: the list to handle user input word for recursion steps: choose, explore, un-choose
    :param search: the list to handle recursion permutation for user input string
    :param word_dicts: the list to store all words from dictionary
    :return: this function return nothing
    """
    global count, double_ans
    #   Base case is user input string length equals to the length of search list
    if len(s) == len(search):
        word = ''
        for ele in search:
            word += ele
        if word in word_dicts and word not in double_ans:
            count += 1
            print(f'Found:  {word}')
            print('Searching...')
            double_ans.append(word)

    else:
        for i in range(len(current)):
            if has_prefix(search):
                # choose
                search.append(current[i])
                current.pop(i)
                # explore
                find_anagrams_helper(s, current, search, word_dicts)
                # un-choose
                current.insert(i, search[len(search)-1])
                search.pop()


def has_prefix(sub_s):
    """
    :param sub_s: get the current list and search the word from dictionary
    :return: if the search exists in dictionary, return True bool
    """
    sub_string = ''
    for ele in sub_s:
        sub_string += ele
    for i in word_dict:
        if i.startswith(sub_string):
            return True


if __name__ == '__main__':
    main()
