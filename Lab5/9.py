import re

def insert_spaces(text):
    pattern = r'(?<=\b)([A-ZА-Я][a-zа-я]*)'
    result = re.sub(pattern, r' \1', text)
    return result

text = "Это Пример Текста с заглавными Словами. Еще Один Пример."
result_text = insert_spaces(text)

print(result_text)
