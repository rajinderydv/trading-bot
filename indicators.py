def calculate_pivot(high, low, close):
    pivot = (high + low + close) / 3

    r1 = (2 * pivot) - low
    s1 = (2 * pivot) - high

    return {
        "pivot": pivot,
        "r1": r1,
        "s1": s1
    }