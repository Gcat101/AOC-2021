# Variables
puzzle = open('input.txt').read().split('\n')
# Position variables
horiz = 0
depth = 0

# Calculate position
for i in puzzle:
    val = int(i.split(' ')[1]) # how many?
    act = i.split(' ')[0] # what?

    if act=='forward': horiz += val # horiz+ if forward
    elif act=='down': depth += val # depth+ if down
    elif act=='up': depth -= val # depth- if up

print(horiz * depth) # Print the result