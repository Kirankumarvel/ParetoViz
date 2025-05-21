def calculate_cumulative_percent(values):
    total = sum(values)
    cumulative = []
    running_total = 0
    for val in values:
        running_total += val
        percent = (running_total / total) * 100
        cumulative.append(percent)
    return cumulative
