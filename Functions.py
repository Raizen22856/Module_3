data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data):
    final_sum = 0
    if isinstance(data, int):
        final_sum += data
    elif isinstance(data, str):
        final_sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            final_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            final_sum += calculate_structure_sum(key)
            final_sum += calculate_structure_sum(value)
    return final_sum
result = calculate_structure_sum(data_structure)
print(result)


