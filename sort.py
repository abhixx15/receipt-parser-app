def bubble_sort(data, field_index, reverse=False):
    sorted_data = data[:]
    n = len(sorted_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = sorted_data[j][field_index]
            b = sorted_data[j + 1][field_index]
            if a is None or b is None:
                continue
            if reverse:
                if a < b:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
            else:
                if a > b:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data
