def is_valid(x, y, orientation, grid, M, N):
    if orientation == 0:  # horizontal
        return 0 <= x < M and 0 <= y+1 < N and grid[x][y] != 'H' and grid[x][y+1] != 'H'
    else:  # vertical
        return 0 <= x+1 < M and 0 <= y < N and grid[x][y] != 'H' and grid[x+1][y] != 'H'

def can_rotate(x, y, grid, M, N):
    if x+1 >= M or y+1 >= N: 
        return False
    for i in range(2):
        for j in range(2):
            if grid[x+i][y+j] == 'H':
                return False
    return True

def solve():
    M, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(M)]

    # Find start and target sofa positions
    start = None
    target = None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 's':
                if start is None:
                    start = (i, j)
                else:
                    if start[0] == i:  # same row => horizontal
                        start_state = (i, min(j, start[1]), 0)
                    else:  # vertical
                        start_state = (min(i, start[0]), j, 1)
            if grid[i][j] == 'S':
                if target is None:
                    target = (i, j)
                else:
                    if target[0] == i:
                        target_state = (i, min(j, target[1]), 0)
                    else:
                        target_state = (min(i, target[0]), j, 1)

    # BFS
    q = deque([(start_state, 0)])
    visited = set([start_state])

    while q:
        (x, y, orient), steps = q.popleft()
        if (x, y, orient) == target_state:
            print(steps)
            return

        # Try moves
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if is_valid(nx, ny, orient, grid, M, N):
                state = (nx, ny, orient)
                if state not in visited:
                    visited.add(state)
                    q.append((state, steps+1))

        # Try rotation
        if can_rotate(x, y, grid, M, N):
            new_orient = 1 - orient
            state = (x, y, new_orient)
            if is_valid(x, y, new_orient, grid, M, N) and state not in visited:
                visited.add(state)
                q.append((state, steps+1))

    print("Impossible")