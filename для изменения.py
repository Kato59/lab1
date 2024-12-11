def inc(obj):
    if 'n' in obj:
        obj['n'] += 1

# Пример использования
obj = {'n': 5}
inc(obj)
print(obj)  # Ожидаемый вывод: {'n': 6}
