def all_variants(text):
    """Генерирует все возможные непустые подпоследовательности строки."""
    n = len(text)

    # Генерируем все подмножества индексов символов строки
    for mask in range(1 << n):
        result = []
        for j in range(n):
            if mask & (1 << j):
                result.append(text[j])
        if result:
            yield ''.join(result)
a = all_variants("abc")
for i in a:
    print(i)
