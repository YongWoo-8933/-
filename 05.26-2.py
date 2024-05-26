"""
백준 11049 행렬 곱셈 순서

1. 평범한 greedy 알고리즘으로 가기에는 경우가 좀 더 많음
   (당장은 왼쪽발로 가는게 더 낫더라도, 전체적으로는 비용이 많은 경우도 있음)
2. 우선 방향 i > j로 가는 모든 경우에 대한 cost를 2차원 배열로 정리
   (costs[i][j] 형식)
3. 발의 방향이 상관없으므로, 발의 위치는 맨처음 (0, 0)을 제외하면 항상 아래 조합중 하나임
   (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
4. 따라서 눌러야할 각 방향표 버튼에 대해 모든 케이스의 누적 cost를 쌓아가는 방식으로 진행
   ex) (0, 1) -> (0, 2) 인경우 / (0, 1) -> (2, 1) 인경우 등을 각각 쌓음
   10가지 모든경우에 대해 나올수 있는 경우는 많아봐야 10가지, 중복되는 경우 cost가 낮은쪽 선택

크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다.
행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 
입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 
정답은 2^31-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 2^31-1보다 작거나 같다.

예제 입력 1 
3
5 3
3 2
2 6
예제 출력 1 
90
"""
from sys import stdin
N = int(stdin.readline())
lst = []
for i in stdin:
    a, b = map(int, i.split())
    if lst:
        lst.pop()
    lst.append(a)
    lst.append(b)
indexed_lst = [(lst[i], i) for i in range(1, N)]
indexed_lst.sort(reverse=True)
visited = set()
answer = 0
for value, idx in indexed_lst:
    visited.add(idx)
    lp, rp = idx-1, idx+1
    while lp in visited:
        lp -= 1
    while rp in visited:
        rp += 1
    answer += lst[lp]*lst[idx]*lst[rp]
print(answer)



