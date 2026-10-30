def open_tasks(tasks):
    return [task["title"] for task in tasks if not task["done"]]

tasks = [
    {"title": "Написать hello.py", "done": True},
    {"title": "Открыть from_js.py", "done": False},
    {"title": "Запустить файл", "done": False},
]

# for task in open_tasks(tasks):
#     print(task)

# for number, task in enumerate(open_tasks(tasks), start=1):
#     print(f"{number}. {task}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks

add_task(tasks, "Пойти поесть")

def summary(tasks):
    values = {"open": 0, "done": 0}
    for task in tasks:
        if task["done"]:
            values["done"] += 1
        else:
            values["open"] += 1
    return values

print(summary(tasks))