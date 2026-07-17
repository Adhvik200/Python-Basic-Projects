def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)
        
    return sequence[n]

print(fibonacci(15)) 