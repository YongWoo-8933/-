"""
문제 1. => 이분 탐색
구멍막기?

일렬로 나열된 수직선이 있음 여기서 특정 좌표에 구멍이 남.
[1, 4, 6, 7, 11] 이런식으로 구멍이 난 자리를 알려줌.
N은 구멍의 수, x는 뚫린 좌표값이라고 할 때,
1 <= N <= 100,000  /  0 <= x <= 10^9 를 만족.

여기서 구멍을 메우기 위해 특정한 길이만큼의 보수를 함.
예를 들어 길이 1짜리 보수를 한다면,
1, 4, 6, 7, 11 다섯 구멍을 모두 막아야 하므로 5개 필요.
길이 2짜리 보수를 한다면,
1, 4, 6-7, 11 이런식으로 막으면 4개 필요.
길이 4짜리 보수를 한다면,
1-4, 6-7, 11 이런식으로 막으면 3개 필요. 

이때 사용할 수 있는 보수자재의 갯수가 K로 제한될 때,
각 자재의 길이가 최소가 되게 하고싶다.
이 길이를 구하시오.



문제 2. => 비트마스킹+BFS?
배터리 배치하기

1 <= H, W <= 10
8 <= H*W <= 16
-1,000 <= 에너지 출력값 <= 1,000

H * W 격자가 있을 때, 이어진 5칸을 고르면 첫번째 배터리 배치가 됨
이 5칸중 딱 2칸만 겹치게 하고 두번째 배터리 5칸을 배치
차지한 모든 칸의 값을 합치면 효율값인데, 이 값이 최대가 되게 하시오.
"""
