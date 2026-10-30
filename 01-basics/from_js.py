def open_tasks(tasks):
    return [task["title"] for task in tasks if not task["done"]]

tasks = [
    {"title": "Написать hello.py", "done": True},
    {"title": "Открыть from_js.py", "done": False},
    {"title": "Запустить файл", "done": False},
]

# for task in open_tasks(tasks):
#     print(task)

for task in enumerate(tasks, start=0):
    print(task)