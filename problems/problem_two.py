def is_even(x):
    if x % 2 == 0:
        return 1
    return 0

def fibonacci_loop():
    n0 = 1
    n1 = 2
    n2 = None
    sum = 0
    while n1 < 4000000:
        n2 = n0 + n1
        n0 = n1
        if is_even(n1):
            sum += n1
        n1 = n2
    return sum

if __name__ == "__main__":
    sum = fibonacci_loop()
    print("The answer is {}".format(sum))