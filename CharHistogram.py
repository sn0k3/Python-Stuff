def count_char(character, array):
	counter = int(0);

	for element in array:
		if character == element:
			counter = counter + 1;


	return counter;

def char_hist(str_inp):
	histogram_res = {};

	for i in range(0, len(str_inp)):
		current_char = str_inp[i];

		counter = count_char(current_char, str_inp);

		histogram_res[str_inp[i]] = counter;

	return histogram_res;


if __name__ == '__main__':
	print(char_hist("pe6ooo be, kvo mi se praish"));

	print('\n');
