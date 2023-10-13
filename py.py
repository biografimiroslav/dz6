import logging

# Налаштовуємо логування, виводячи повідомлення про винятки у консоль
logging.basicConfig(level=logging.ERROR)

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a менше за b")
        if b > 100:
            raise IndexError("b більше за 100")
        return a / b
    except (ValueError, IndexError) as e:
        logging.error(f"Помилка: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
result = []

for key, value in data.items():
    res = divider(key, value)
    if res is not None:
        result.append(res)

print(result)
