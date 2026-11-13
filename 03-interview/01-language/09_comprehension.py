# Comprehension — цикл, записанный одним выражением.
# Слева стоит, что положить в результат. Потом откуда брать элементы.
# if в конце оставляет только подходящие, как filter.
# Список собирает значения по порядку. Словарь собирает пары ключ: значение.
# Множество собирает уникальные значения.

tasks = [
    {"title": "Написать hello.py", "done": True},
    {"title": "Открыть from_js.py", "done": False},
    {"title": "Запустить файл", "done": False},
]

open_titles = []
for task in tasks:
    if not task["done"]:
        open_titles.append(task["title"])
print("loop", open_titles)

print("list", [task["title"] for task in tasks if not task["done"]])
print("dict", {task["title"]: task["done"] for task in tasks})
print("set", {task["done"] for task in tasks})
