input_array = [True, 'hello', 5, 12, -200, False, False, 'word', None, 3.14, [1, 2], {'key': 'value'}]
type_counts = {}

for item in input_array:
    item_type = type(item).__name__ 
    if item_type not in type_counts:
        type_counts[item_type] = 0  
    type_counts[item_type] += 1  

print(type_counts)  # Пример вывода: {'bool': 3, 'str': 2, 'int': 3, 'NoneType': 1, 'float': 1, 'list': 1, 'dict': 1}
