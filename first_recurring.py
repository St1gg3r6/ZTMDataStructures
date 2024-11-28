
def first_recurring_character(input):
    distance = len(input)
    first = None
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                if j - i < distance:
                    first = input[i]
                    distance = j - i
                if distance == 1:
                    return first
    if first:
        return first
    return None


def first_recurring_character2(input):
    map = {}
    for i in range(len(input)):
        if input[i] not in map:
            map[input[i]] = len(input)
        else:
            if map[input[i]] == len(input):
                map[input[i]] = i
    print(map)
    return min(map, key=lambda v: map[v])


print(first_recurring_character([2, 5, 4, 6, 4, 5, 1, 2, 4]))
print(first_recurring_character2([2, 5, 4, 6, 4, 5, 1, 2, 4]))
print(first_recurring_character2([2, 5, 4, 2, 4, 5, 1, 2, 4]))
print(first_recurring_character2([2, 5, 5, 2, 4, 5, 1, 2, 4]))