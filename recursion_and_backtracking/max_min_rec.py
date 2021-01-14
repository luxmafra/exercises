from random import shuffle


def max_min(lst):
    n = len(lst)
    if n == 0:
        raise ValueError('Empty List')
    max_value = min_value = lst[-1]

    def max_min_rec(cursor):
        nonlocal max_value, min_value
        if cursor < 0:
            return max_value, min_value
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor - 1)

    return max_min_rec(n - 1)


print(max_min([1]))  # 1,1
print(max_min([1, 2]))  # 2,1

random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(random_list))

print(max_min([]))  # Error: 'Empty List'
