#Manhattan distance
import math

f = open("in_day_3.txt")
line1, line2 = f.readlines()
line1 = line1.strip().split(",")
line2 = line2.strip().split(",")

path1 = []
path1.append([0,0])
path2 = []
path2.append([0,0])

def move(direction,lenght,path):
	if (direction == 'R'):
		for i in range(1, lenght+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x+1,y])
	elif (direction == 'L'):
		for i in range(1, lenght+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x-1,y])
	elif (direction == 'U'):
		for i in range(1, lenght+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x,y+1])
	elif (direction == 'D'):
		for i in range(1, lenght+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x,y-1])


for command in line1:
	direction = command[0] #direction = prvi znak npr.R1000, direction je R
	lenght = int(command[1:]) #lenght je ostali dio i on je integer (1-kraja)
	move(direction,lenght,path1)

for command in line2:
	direction = command[0] 
	lenght = int(command[1:]) 
	move(direction,lenght,path2)

minimum = math.inf
for point in path1:
	if point in path2:
		steps  = path1.index(point) + path2.index(point) #index je adresa (pozicija) u polju
		print (steps)
		if steps == 0:
			print("no")

		elif minimum > steps:
			minimum = steps

print(minimum)