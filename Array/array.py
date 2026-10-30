# Program to process an array of scores

scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum =", total)
print("Average =", average)

maximum = max(scores)
minimum = min(scores)

print("Maximum =", maximum)
print("Minimum =", minimum)