#1202 program alarm

f = open("in_day_2.txt")
lines = f.readlines()
original_array = lines[0].strip().split(",")
original_array = [int(i) for i in original_array]


output = 19690720

for noun in range(0,100):
	for verb in range(0,100):
		original_array[1] = noun
		original_array[2] = verb
		array = original_array.copy()
		n = 0

		while (array[n] != 99):
			if (array[n] == 1):
					array[array[n+3]] = array[array[n+1]] + array[array[n+2]]
			if (array[n] == 2):
					array[array[n+3]] = array[array[n+1]] * array[array[n+2]]
			n = n + 4

		if (array[0] == output):
			print(str(100*array[1] + array[2]))