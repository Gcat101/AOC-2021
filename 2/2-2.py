# Variables
puzzle = open('input.txt').read().split('\n')
# Position variables
horiz = 0
depth = 0
aim = 0

# Calculate position
for i in puzzle:
    val = int(i.split(' ')[1]) # how many?
    act = i.split(' ')[0] # what?

    if act=='forward': 
        horiz += val # horiz+ if forward
        depth += aim*val # depth+ if forward
    elif act=='down': aim += val # aim+ if down
    elif act=='up': aim -= val # aim- if up

print(horiz * depth) # Print the result