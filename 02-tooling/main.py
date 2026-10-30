from tasks import add_task, open_tasks, summary, parse_count

def main():
    tasks = [
        {"title": "Написать hello.py", "done": True},
        {"title": "Открыть from_js.py", "done": False},
    ]
    add_task(tasks, "Пойти поесть")
    print(open_tasks(tasks))
    print(summary(tasks))
    print(parse_count("3"))
    print(parse_count("10px"))
if __name__ == "__main__":
    main()