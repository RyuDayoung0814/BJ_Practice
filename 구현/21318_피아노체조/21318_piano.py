def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Parsing input data
    index = 0
    N = int(data[index])
    index += 1
    difficulties = list(map(int, data[index:index+N]))
    index += N
    Q = int(data[index])
    index += 1
    queries = []
    for _ in range(Q):
        x = int(data[index])
        y = int(data[index+1])
        queries.append((x, y))
        index += 2
    
    # Preprocess to calculate the number of mistakes
    mistakes = [0] * (N - 1)
    for i in range(N - 1):
        if difficulties[i] > difficulties[i + 1]:
            mistakes[i] = 1
    
    # Prefix sum array of mistakes
    cumulative_mistakes = [0] * (N - 1)
    if N > 1:
        cumulative_mistakes[0] = mistakes[0]
        for i in range(1, N - 1):
            cumulative_mistakes[i] = cumulative_mistakes[i - 1] + mistakes[i]
    
    # Answer each query
    output = []
    for x, y in queries:
        if x == y:
            output.append(0)
        else:
            x -= 1  # Convert to zero-based index
            y -= 1  # Convert to zero-based index
            if x == y:
                output.append(0)
            else:
                # Sum of mistakes from x to y-1
                if x == 0:
                    mistakes_count = cumulative_mistakes[y - 1]
                else:
                    mistakes_count = cumulative_mistakes[y - 1] - cumulative_mistakes[x - 1]
                output.append(mistakes_count)
    
    # Print all results
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

