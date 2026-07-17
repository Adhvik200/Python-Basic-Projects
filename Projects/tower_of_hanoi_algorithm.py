def hanoi_solver(n):
    def solve(n, source, target, auxiliary, steps):
        if n > 0:
            solve(n - 1, source, auxiliary, target, steps)
            target.append(source.pop())
            steps.append(f"{rods[0]} {rods[1]} {rods[2]}")
            solve(n - 1, auxiliary, target, source, steps)

    rods = [list(range(n, 0, -1)), [], []]
    results = [f"{rods[0]} {rods[1]} {rods[2]}"]

    solve(n, rods[0], rods[2], rods[1], results)

    return "\n".join(results)

print(hanoi_solver(3))