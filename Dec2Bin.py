
def dec2bin(dec_num):
	res = [];

	dec_num = int(dec_num);
	while int(dec_num) > 0:
		rem = int(dec_num % 2);
		dec_num = int(dec_num / 2);

		res.append(rem);


	j = len(res) - 1;
	while j >= 0:
		print(str(res[j]), end='');
		j = j - 1;


if __name__ == "__main__":
	print('Enter num: ');
	
	user_input = input();

	print("" + user_input + " in binary is ", end='');

	dec2bin(user_input);