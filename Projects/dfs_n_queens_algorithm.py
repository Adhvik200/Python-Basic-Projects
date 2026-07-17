def dfs_n_queens(n: int) -> list:
    if n < 1:
        return []
        
    solutions = []
    
    def is_safe(state, col):
        row = len(state)
        for r, c in enumerate(state):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(state):
        if len(state) == n:
            solutions.append(list(state))
            return
            
        for col in range(n):
            if is_safe(state, col):
                dfs(state + [col])

    dfs([])
    return solutions

print(f"N=3 solutions: {dfs_n_queens(3)}")

print(f"N=4 solutions: {dfs_n_queens(4)}")

eight_queens = dfs_n_queens(8)
print(f"N=8 total solutions found: {len(eight_queens)}")