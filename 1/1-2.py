# Variables
puzzle = list(map(int, open('input.txt').read().split('\n')))
sums = []
prev = 0
counter = 0

# Get the sums
for i in range(len(puzzle)):
    try: 
        puzzle[i + 2] # check if theres room for sum
        sums.append(sum(puzzle[i:i+3])) # get the sum
    except IndexError: break # break if no room

# Go through sums
for i in sums:
    if i > prev and prev: counter += 1 # counter+1 if new number is bigger
    prev = i # save previous number

print(counter) # print the result