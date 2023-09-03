# Read n, the number of elements in the list.
n = int(input())

# Read and convert a space-separated list of integers into a list.
arr = list(map(int, input().split()))

# Find the winner (maximum value) in the list.
winner = max(arr)

# Remove all instances of the winner from the list.
while winner in arr:
    arr.remove(winner)

# Find the runner-up (new maximum value after removing the winner).
runner_up = max(arr)

# Print the runner-up.
print(runner_up)
