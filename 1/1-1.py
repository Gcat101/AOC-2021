# Variables
puzzle = list(map(int, open('input.txt').read().split('\n')))
prev = 0
counter = 0

# Go through numbers
for i in puzzle:
    if i > prev and prev: counter += 1 # counter+1 if new number is bigger
    prev = i # save previous number

print(counter) # print the result