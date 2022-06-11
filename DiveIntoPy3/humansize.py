SUFFIXES = {1000: ['KB', 'MB', 'GB'],
			1024: ['KiB', 'MiB', 'GiB']};

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
	if size < 0:
		raise ValueError('Number must be greater or equal to 0!');

	multiple = 1024 if a_kilobyte_is_1024_bytes else 1000;

	for suffix in SUFFIXES[multiple]:
		size = size / multiple;

		if size < multiple:
			return '{0:.1f} {1}'.format(size, suffix);

	raise ValueError('Num too big!');		


if __name__ == "__main__":
	print(approximate_size(2102, True));
