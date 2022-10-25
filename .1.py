#sum of numbers from 1 to 1000, including 1000

def sum():
    num = int(input("Please enter a whole number: "))
    sum = 0
    for values in range (1,num + 1):
        sum = sum + values
print(sum)
