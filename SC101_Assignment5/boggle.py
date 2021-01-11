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

word_dict = []


def main():
	# Set up boggle board
	boggle = []
	for i in range(1, 5):
		i = input(f'{i} row of letters: ')
		lst = i.split()
		if len(lst) != 4:
			print(f'illegal format')
			exit()
		boggle.append(lst)

	find_words(boggle)


def find_words(boggle):
	"""
	Find words from boggle board then search from dictionary
	:param boggle: get the boggle board
	:return: this function return nothing
	"""
	set_permutations = get_permutations(boggle)
	print(f'Searching from dictionary...')
	read_dictionary(set_permutations)


def get_permutations(boggle):
	"""
	Get all permutation
	:param boggle:
	:return:
	"""
	# ignore duplicate word in permutation list
	set_permutations = set()
	# read the row and column char from boggle board
	for row in range(4):
		for column in range(4):
			words = words_from(boggle, row, column, lst_word=[])
			if words:
				for word in words:
					set_permutations.add(word)
			words = None
	return sorted(list(set_permutations))


def words_from(boggle, row, column, current='', lst_word=[]):
	"""
	Calculate all possible words from a given starting position
	:param boggle: read boggle board and replace "-" as choose words from board
	:param row:	nested list from board
	:param column: list from board
	:param current:	choose words from board
	:param lst_word: choose recursion words and try possible permutations
	:return: return word list for all possible from board permutation
	"""
	# out of range so return
	if row in (4, -1) or column in (4, -1):
		return
	# only search 4 char words from the dictionary
	if len(current) > 4:
		return
	# replace "-" for the word has been choose
	if boggle[row][column] != '-':
		new_string = current + boggle[row][column]
		new_boggle = copy.deepcopy(boggle)
		new_boggle[row][column] = '-'
		# choose
		if len(new_string) >= 4:
			lst_word.append(new_string.lower())
		# explore
		neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		# un-choose
		for x, y in neighbors:
			words_from(new_boggle, row + x, column + y, new_string, lst_word)
		return lst_word


def read_dictionary(set_permutations):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_dict
	with open('dictionary.txt') as f:
		for line in f:
			line = line.strip()
			word_dict += line.split(',')

	count = 0
	for ans in set_permutations:
		if ans.lower() in word_dict:
			count += 1
			print(f'Found "{ans}"')
	print(f'There are {count} words in total.')


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	sub_string = ''
	for ele in sub_s:
		sub_string += ele
	for i in word_dict:
		if i.startswith(sub_string):
			return True


if __name__ == '__main__':
	main()
