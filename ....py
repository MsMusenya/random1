#sum of natural numbers(1-1000, +1000) up to num

num = int(input("Please enter the number: "))

sum = 0

for value in range(1, num + 1):
    sum = sum + value

print(sum)
