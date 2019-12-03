#1202 program alarm

f = open("in_day_2.txt")
lines = f.readlines()
array = lines[0].strip().split(",")
array = [int(i) for i in array]


array[1] = 12
array[2] = 2
n = 0
while (array[n] != 99):
	if (array[n] == 1):
			array[array[n+3]] = array[array[n+1]] + array[array[n+2]]
	if (array[n] == 2):
			array[array[n+3]] = array[array[n+1]] * array[array[n+2]]
	n = n + 4

print(array[0])





