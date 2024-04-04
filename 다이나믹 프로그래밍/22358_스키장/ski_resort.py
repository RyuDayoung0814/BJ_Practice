from collections import defaultdict
import heapq

def max_ski_time(N, M, K, S, T, courses):
    # 그래프 구성
    graph = defaultdict(list)
    for a, b, t in courses:
        graph[a].append((b, t))
    
    # dp[state] = (time, lift_count), 여기서 state는 (current_position, remaining_lifts)
    dp = defaultdict(lambda: (-1, 0))
    dp[(S, K)] = (0, K)
    queue = [(-0, S, K)]  # 최대 힙을 사용, (-스키 타는 시간, 현재 위치, 남은 리프트 사용 횟수)

    while queue:
        neg_time, position, lifts = heapq.heappop(queue)
        time = -neg_time

        if position == T:
            return time
        
        # 스키 코스 이동
        for next_position, ski_time in graph[position]:
            next_time = time + ski_time
            if dp[(next_position, lifts)][0] < next_time:
                dp[(next_position, lifts)] = (next_time, lifts)
                heapq.heappush(queue, (-next_time, next_position, lifts))
        
        # 리프트 이용 이동 (역방향)
        if lifts > 0:
            for prev_position, _ in graph.items():
                if position in [b for b, t in graph[prev_position]]:
                    if dp[(prev_position, lifts-1)][0] < time:
                        dp[(prev_position, lifts-1)] = (time, lifts-1)
                        heapq.heappush(queue, (-time, prev_position, lifts-1))

    # T번 지점으로 갈 수 없는 경우
    return -1

# 예시 입력
N, M, K, S, T = 5, 5, 1, 1, 5
courses = [
    (1, 2, 4),
    (2, 3, 3),
    (3, 4, 2),
    (4, 5, 1),
    (2, 5, 10)
]

# 최대 스키 타는 시간 계산
print(max_ski_time(N, M, K, S, T, courses))
