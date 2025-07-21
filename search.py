import re

def keyword_search(data, keyword):
    return [row for row in data if keyword.lower() in str(row).lower()]

def range_search(data, field_index, min_val, max_val):
    return [row for row in data if isinstance(row[field_index], (int, float)) and min_val <= row[field_index] <= max_val]

def pattern_search(data, pattern, field_index):
    return [row for row in data if re.search(pattern, str(row[field_index]))]
