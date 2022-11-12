def webster(total_votes, curr_seats, ratio):
    return total_votes / (curr_seats + ratio)


def divisorMethod(political_parties, curr_ratio, original=None):
    empty_seats = 120
    chosen_party = None
    while empty_seats > 0:
        curr_max = 0
        for pp in political_parties:
            result = webster(pp[0], pp[1], curr_ratio)
            if curr_max < result:
                curr_max = result
                chosen_party = pp
        chosen_party[1] += 1
        empty_seats -= 1
    result = []
    for pp in political_parties:
        result.append(pp[1])
    return result != original


if __name__ == '__main__':
    ## (votes number, curr_seats)
    a = [1066892, 0]
    b = [614112, 0]
    c = [316008, 0]
    d = [292257, 0]
    e = [273836, 0]
    f = [268767, 0]
    g = [248391, 0]
    h = [248370, 0]
    i = [225641, 0]
    j = [212583, 0]
    k = [209161, 0]
    l = [202218, 0]
    m = [167064, 0]
    parties = [a, b, c, d, e, f, g, h, i, j, k, l, m]
    ratio = 0.5
    results = []

    """
    Check results for a specific ratio (y)
    """
    divisorMethod(parties, ratio)
    for p in parties:
        results.append(p[1])
    print(f"The split with ratio: {ratio} is {results}")

    ## init all political parties to 0
    for pp in parties:
        pp[1] = 0
    """
        Check the highest ratio (y) that causes a change
    """
    ratio = 1
    results = []
    original = [31, 17, 9, 8, 7, 7, 7, 7, 6, 6, 6, 5, 4]
    while not divisorMethod(parties, ratio, original):
        ratio -= 0.001
        for pp in parties:
            pp[1] = 0
    for p in parties:
        results.append(p[1])
    print(f"Biggest Y that causes a change: {ratio}")
    print(f"The changes are: {results}")
