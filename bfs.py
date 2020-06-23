import queue
import time

start = list(map(int,input().split()))
goal = [1,2,3,4,5,6,7,8,0]

class Puzzle:     # 経過を示したいのでそれをオブジェクトに保存することにする
    def __init__(self, now, past):
        self.now = now
        self.past = past
        self.past.append(now)

memo = {} #　一度なった盤面を記憶

# 0の位置と、その位置に0があるときの移動可能位置を記述
move = {0:[1,3],
        1:[0,2,4],
        2:[1,5],
        3:[0,4,6],
        4:[1,3,5,7],
        5:[2,4,8],
        6:[3,7],
        7:[4,6,8],
        8:[5,7]
}

def bfs(start,goal):
    puzzle = Puzzle(start, [])
    q = queue.Queue()
    q.put(puzzle)
    memo[tuple(puzzle.now)] = True

    def new(puzzle, zero_posi, zero_neigh):
        new_puzzle = puzzle[:]
        new_puzzle[zero_posi], new_puzzle[zero_neigh] = new_puzzle[zero_neigh], new_puzzle[zero_posi]
        return new_puzzle

    while not q.empty():
        puzzle = q.get()
        zero_posi = puzzle.now.index(0)  # 0の位置取得

        for zero_neigh in move[zero_posi]:
            newtmp = new(puzzle.now, zero_posi, zero_neigh)
            new_puzzle = Puzzle(newtmp, puzzle.past[:])
            
            if tuple(new_puzzle.now) in memo:
                continue

            if new_puzzle.now == goal:
                return new_puzzle

            memo[tuple(new_puzzle.now)] = True
            q.put(new_puzzle)

t1 = time.time()

ans = bfs(start,goal)
for rec in ans.past:
    print("{}回目".format(ans.past.index(rec)))
    tmp = [str(a) for a in rec]
    for i in range(3):
        tmp[3*i:3*i+3] = "".join(tmp[3*i:3*i+3])
        print(*tmp[3*i:3*i+3])

t2 = time.time()
elapsed_time = t2 - t1
print("実行時間 {}s".format(elapsed_time))