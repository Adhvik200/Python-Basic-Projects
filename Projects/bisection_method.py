def square_root_bisection(square_target, tolerance=1e-7, maximum_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)

    for _ in range(maximum_iterations):
        midpoint = (low + high) / 2

        if (high - low) / 2 < tolerance:
            print(f"The square root of {square_target} is approximately {midpoint}")
            return midpoint

        if midpoint * midpoint < square_target:
            low = midpoint
        else:
            high = midpoint

    print(f"Failed to converge within {maximum_iterations} iterations")
    return None

square_root_bisection(0.001, 1e-7, 50)