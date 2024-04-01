if __name__ == '__main__':
    n, k = map(int, input().split())
    unique_numbers = set()
    ans = 1  # 결과값 초기화

    for _ in range(n):
        t = int(input())
        unique_numbers.add(t)  # 현재 숫자 추가

        # 모든 가능한 숫자가 등장했는지 확인
        if len(unique_numbers) == k:
            ans += 1  # 조건을 만족하면 결과값 증가
            unique_numbers.clear()  # 집합 초기화

    print(ans)