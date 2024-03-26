if __name__ == '__main__':
    # initialize
    nb_item, total_weight = map(int, input('물품의 수 / 버틸 수 있는 무게: ').split())
    max_value = 0
    
    items = []
    for i in range(nb_item):
        weight, value = map(int, input(f'{i+1}번째 물품의 무게, 가치: ').split())
        items.append((weight, value))

    # Dynamic Prograiming
    dp = [[0] * (total_weight+1) for _ in range(nb_item+1)]

    for i in range(1, nb_item+1):
        for j in range(1, total_weight+1):
            weight, value = items[i-1]
            if j >= weight:
                # i번째 물품을 넣는 경우와 넣지 않는 경우 중 더 큰 값 선택
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            else:
                # i번째 물품을 넣을 수 없는 경우
                dp[i][j] = dp[i-1][j]
    
    max_value = dp[nb_item][total_weight]

    print(f'배낭에 넣을 수 있는 물건들의 가치합의 최댓값: {max_value}')