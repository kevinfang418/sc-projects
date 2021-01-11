"""
File: largest_digit.py
Name: Kevin Fang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	largest = helper(n, 0)
	return largest


# Define helper to record largest value
def helper(n, largest):

	# Base case is n equals to 0, then return largest
	if n == 0:
		return largest

	else:
		if n < 0:
			n = -n
		current = n % 10
		if current > largest:
			largest = current
		new_n = int(n/10)
		# return new_n and largest for recursion
		return helper(new_n, largest)


if __name__ == '__main__':
	main()
