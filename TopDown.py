def cut_rod(price, n):
    if n <= 0:
        return 0
    max_val = -1

    val = 0
    for i in range(0, n):
        val = price[i] + cut_rod(price, n - i - 1)
        if max_val < val:
            max_val = val
    return max_val


