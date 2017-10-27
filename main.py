import random
import math

def return_coordinate(n):
	#returns co-ordinates assuming start at 0,0 for n blocks of walk
	x,y = 0,0

	for walking_block_size in range(n):
		(dx,dy) = random.choice([[0,1],[0,-1],[1,0],[-1,0]])
		x+= dx
		y+= dy
	return (x,y)


sample_size = 10000
stats = []  #for holding [walking_block_size, average_walked, average_paid] for a given walking_block_size

'''for a given block size, run given number of simulations and append statistics to stats'''
for walking_block_size in range(100):
	#used to calculate average_walked and average_paid
	total_walked = 0		
	total_paid = 0
	for sample in range(sample_size):
		coordinates = return_coordinate(walking_block_size)
		distance = abs(coordinates[0]) + abs(coordinates[1])
		if distance <=6:
			total_walked += distance
		else:
			total_paid += 10
		
	if total_paid == 0:
		total_paid = 1   #to avoid divide by zero, we assume minumum total payment of 1 for e
	#append stats for the particular walking_block_size
	stats.append([walking_block_size,total_walked/sample_size,total_paid/sample_size])

key = 0
for x in stats:
	if x[1]/x[2] > key:
		key = x[0]
	print(x)

print("The highest walking value can be obtained by walking ", key, " blocks.")
print("By walking ",key," blocks, you can expect to walk ", stats[key][1]," blocks while", \
			" expecting to pay", stats[key][2]," dollars for Lyft.")
