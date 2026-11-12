import json
from pathlib import Path

def open_tasks(tasks):
    return [task["title"] for task in tasks if not task["done"]]

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks

def summary(tasks):
    values = {"open": 0, "done": 0}
    for task in tasks:
        if task["done"]:
            values["done"] += 1
        else:
            values["open"] += 1
    return values

def parse_count(text):
    try:
        return int(text)
    except ValueError:
        return None

def save_tasks(tasks, path):
    path = Path(path)  
    with path.open("w", encoding="utf-8") as file: