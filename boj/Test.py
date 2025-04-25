def solve():
    n = int(input())
    trash_list = [input() for _ in range(n)]
    costs = list(map(int, input().split()))
    other_cost = int(input())

    total_cost = 0
    recyclable_types = {'P': 0, 'C': 1, 'V': 2, 'S': 3, 'G': 4, 'F': 5}

    for trash in trash_list:
        trash_size = len(trash)
        unique_chars = set(trash)
        recyclable = False
        recycle_bin = ''
        recycle_cost = float('inf')

        if len(unique_chars) == 1 and unique_chars.issubset(recyclable_types):
            recyclable = True
            recycle_bin = unique_chars.pop()
            recycle_cost = trash_size * costs[recyclable_types[recycle_bin]]

        other_trash_cost = trash_size * other_cost

        if recyclable:
            total_cost += min(recycle_cost, other_trash_cost)
        else:
            total_cost += other_trash_cost

    print(total_cost)

solve()