def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

for i in range(10):
    print(fibonacci_recursive(i), end=" ")
