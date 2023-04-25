def tiaosheng(failed_counter):
    total_jumps = 0
    time_left = 60
    for i, failure in enumerate(failed_counter):
        if failure - total_jumps <= time_left:
            if i == 0:
                time_left -= failure
            else:
                time_left -= (failure - failed_counter[i - 1])
        else:
            break
        time_left -= 3
        total_jumps = failure
    if time_left >= 0:
        total_jumps += time_left
    return total_jumps


print(tiaosheng([10, 20, 30, 40, 47, 60]))

