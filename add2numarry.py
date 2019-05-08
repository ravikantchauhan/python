N = int(input())

# Get the array 
numArrayA = list(map(int, input().split()))
numArrayB = list(map(int, input().split()))

sumArray = []

# Write the logic here:
for i in range(0, N):
    sumArray.append(numArrayA[i]+numArrayB[i])


# Print the sumArray
for element in sumArray:
    print(element, end=" ")

print("")