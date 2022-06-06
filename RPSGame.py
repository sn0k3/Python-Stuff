import random


def computersTurn():
	random_number = random.randrange(3);

	computer_choice = '0';

	if random_number == 0:
		computer_choice = 'R';
	elif random_number == 1:
		computer_choice = 'P';
	else:
		computer_choice = 'S';

	return computer_choice;

if __name__ == "__main__":

	pc_choice = computersTurn();

	print('Pc choice is: ', pc_choice);

	print('[R]ock, [P]aper, [S]cissor: ');
	user_choice = input();

#	pc_choice = computersTurn();
#	print('Pc choice is: ', pc_choice);

	if user_choice == 'R' and pc_choice == 'P':
		print('PC win!');
	elif user_choice == 'R' and pc_choice == 'S':
		print('You win!');

	if user_choice == 'P' and pc_choice == 'R':
		print('You win!');
	elif user_choice == 'P' and pc_choice == 'S':
		print('PC win!');

	if user_choice == 'S' and pc_choice == 'R':
		print('PC win!');
	elif user_choice == 'S' and pc_choice == 'P':
		print('You win!');


	if user_choice == pc_choice:
		print('Draw game!');
