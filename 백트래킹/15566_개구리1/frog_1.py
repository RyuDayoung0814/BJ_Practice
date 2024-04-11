from itertools import permutations

def can_communicate(frog_prefs, log_topics, frog_pos):
    for (a, b, topic) in log_topics:
        if frog_prefs[frog_pos[a-1]-1][topic-1] != frog_prefs[frog_pos[b-1]-1][topic-1]:
            return False
    return True

def is_valid_placement(frog_preferences, frog_lotus_prefs, log_topics):
    for perm in permutations(range(1, N+1)):
        valid = True
        for i, frog in enumerate(perm):
            if i+1 not in frog_lotus_prefs[frog-1]:
                valid = False
                break
        if valid and can_communicate(frog_preferences, log_topics, perm):
            return True, perm
    return False, []

# Example Input
N, M = 8, 10
frog_preferences = [
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [2, 2, 3, 1],
    [2, 5, 4, 4],
    [1, 5, 5, 2],
    [4, 4, 4, 2],
    [4, 1, 5, 5],
    [4, 4, 4, 4]
]
frog_lotus_prefs = [
    [1, 5],
    [7, 2],
    [6, 3],
    [4, 4],
    [8, 5],
    [6, 6],
    [7, 1],
    [8, 6]
]
log_topics = [
    (1, 2, 1),
    (2, 3, 3),
    (2, 8, 4),
    (3, 4, 1),
    (4, 8, 4),
    (4, 5, 2),
    (8, 6, 1),
    (5, 6, 4),
    (7, 8, 1),
    (6, 7, 1)
]

valid, placement = is_valid_placement(frog_preferences, frog_lotus_prefs, log_topics)

if valid:
    print("YES")
    print(" ".join(map(str, placement)))
else:
    print("NO")
