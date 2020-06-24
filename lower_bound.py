from queue import LifoQueue
import time

start = list(map(int,input().split()))
goal = [1,2,3,4,5,6,7,8,0]

class Puzzle:     # 経過を示したいのでそれをオブジェクトに保存することにする
    def __init__(self, now, past):
        self.now = now
        self.past = past
        self.past.append(now)

"""
ヒューリスティック関数f(x)としてマンハッタン距離をもちいる。
"""
def Manhattan(puzzle): 
    dista = 0
    for i,item in enumerate(puzzle):
        now_row,now_col = i // 3 , i % 3
        goal_row,goal_col = (item - 1) // 3, (item + 2) % 3
        dista += abs(now_row-goal_row) + abs(now_col - goal_col)
    return dista

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

def lower_bound(start,goal):
    puzzle = Puzzle(start, [])
    q = LifoQueue()
    q.put(puzzle)
    memo[tuple(puzzle.now)] = True
    expa = 0

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
            expa += 1
            
            if expa == 77777:
                tmp = 0
                ans = "答えを見つけるには時間がかかりすぎてしまいます。"
                return tmp, ans

            if tuple(new_puzzle.now) in memo:
                continue

            if len(puzzle.past) + Manhattan(new_puzzle.now) > 31: #最大手は31手
                continue

            if new_puzzle.now == goal:
                return new_puzzle, expa

            memo[tuple(new_puzzle.now)] = True
            q.put(new_puzzle)

t1 = time.time()


ans, expa_ans = lower_bound(start,goal)
if type(expa_ans) == int:
    for rec in ans.past:
        print("{}回目".format(ans.past.index(rec)))
        tmp = [str(a) for a in rec]
        for i in range(3):
            tmp[3*i:3*i+3] = "".join(tmp[3*i:3*i+3])
            print(*tmp[3*i:3*i+3])
    t2 = time.time()
    elapsed_time = t2 - t1
    print("実行時間 {}s".format(elapsed_time))
    print("ノードの展開回数 {}回".format(expa_ans))

else:
    print(expa_ans)