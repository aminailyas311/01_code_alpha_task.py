def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a  # yield the current Fibonacci number
        a, b = b, a + b  # calculate the next number in the sequence

# Example usage
fib_gen = fibonacci_generator()

# Printing the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
