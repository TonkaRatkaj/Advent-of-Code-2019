# total fuel requirement

def fuel_requirements(x):
	fr = int(x/3) - 2
	if (fr>0):
		return fr + fuel_requirements(fr)
	else:
		return 0

f = open("in_day_1.txt")
masses = f.readlines()
suma = 0

for mass in masses:
	suma = suma + fuel_requirements(int(mass))

print(suma)
