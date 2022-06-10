'''Given an integer, implement a function, called sum_of_digits(n) that calculates the sum of n's digits.
If a negative number is given, our function should work as if it was positive.'''


def sum_of_digits(n):
	n = abs(n);
	digits = [];

	ch_dg = list(str(n));

	for dig in ch_dg:
		digits.append(int(dig));

	return sum(digits);


if __name__ == "__main__":
	print(sum_of_digits(1234));