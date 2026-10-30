# Program to calculate sum and average of scores

scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum =", total)
print("Average =", average)