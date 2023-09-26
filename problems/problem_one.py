# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000

def divider(x):
    if x % 3 == 0 or x % 5 == 0:
        return 1
    return 0

def loop():
    sum = 0
    i = 1
    while i < 1000:
        if divider(i):
            sum += i
        i += 1
    return sum

if __name__ == "__main__":
    sum = loop()
    print("The sum of all multiples of 3 and 5 below 1000 is {}".format(sum))   