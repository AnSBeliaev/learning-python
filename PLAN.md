# План изучения Python

Источник карты: [roadmap.sh/python](https://roadmap.sh/python) и PDF `C:\Users\dunice\Downloads\python.pdf`.

Опыт: около 4 лет React и JavaScript. Карта подходит как список тем Python, а программирование заново проходить не нужно. Время уходит на синтаксис, стандартную библиотеку и инструменты (`venv`, `pip`, `pytest`). База с PDF — несколько вечеров, не 3–4 недели. Дальше по умолчанию линия backend: небольшой API, который привычно отдать React-приложению. Если цель окажется данные или скрипты, этот выбор меняется после первого проекта.

Текст к темам — [The Python Tutorial](https://docs.python.org/3/tutorial/). Галочки отмечаются в этом файле.

## Этап 0. Интерпретатор — сделано

- [x] Python 3.15.2 стоит в `C:\Users\dunice\AppData\Local\Programs\Python\Python315\python.exe`
- [x] `LongPathsEnabled` равен 1
- [x] В текущем терминале Cursor PATH обновлён, `python --version` печатает `Python 3.15.2`

Cursor был открыт во время установки, поэтому новый терминал может снова увидеть заглушку Microsoft Store (ответ `Python` и код выхода 1). Тогда либо полностью перезапустить Cursor, либо в этом терминале:

```powershell
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
python --version
```

`hello.py` создаёте вы. Это проверка запуска, не урок про `print`. Файл в `C:\Users\dunice\Desktop\learning python`:

```python
print("Привет, Python")
```

```powershell
python hello.py
```

## Что переносится из JavaScript сразу

Идеи те же: значения, функции, ветки, циклы, коллекции, модули, исключения, классы, `async`/`await`, тесты, пакетный менеджер. Ниже только места, где рука пишет JS, а Python ждёт другое.

| JavaScript | Python |
| --- | --- |
| `const` / `let` | просто `name = value` |
| `camelCase` | `snake_case` |
| фигурные скобки и `;` | блок задаётся отступом в 4 пробела |
| `console.log` | `print` |
| `` `hello ${name}` `` | `f"hello {name}"` |
| `null`, `undefined` | одно `None`; проверка `x is None` |
| `===` | `==` для значений, `is` для того же объекта |
| `&&` `\|\|` `!` | `and` `or` `not` |
| `obj?.name ?? "x"` | нет `?.` и `??`. `or` считает пустую строку и `0` отсутствием значения |
| `else if` | `elif` |
| `try / catch`, `throw` | `try / except`, `raise` |
| `arr.push` | `items.append` |
| `arr[arr.length - 1]` | `items[-1]` |
| `for (const x of arr)` | `for x in items:` |
| `for (let i = 0; i < n; i++)` | `for i in range(n):` |
| `arr.map` / `filter` | list comprehension: `[f(x) for x in items if ok(x)]` |
| объект `{ id: 1 }` | словарь `{"id": 1}`, перебор `for key, value in item.items():` |
| деструктуризация | распаковка: `a, b = pair` |
| `function f(a, b = 1) {}` | `def f(a, b=1):` |
| стрелка `(x) => x * 2` | `lambda x: x * 2`, только одно выражение |
| `import { x } from "./a.js"` | `from a import x` |
| `export` | имя в модуле уже доступно для импорта |
| `JSON.parse` / `JSON.stringify` | `json.loads` / `json.dumps` |
| `fetch` | пакет `requests` или `urllib` |
| `process.env` | `os.environ` |
| `npm`, `package.json`, `node_modules` | `venv`, `pip`, `requirements.txt` |
| Prettier, ESLint | Ruff |
| Jest, Vitest | pytest |
| TypeScript проверяет до запуска | аннотации `def f(n: int) -> str` сами по себе в рантайме не проверяются |
| `class` и `this` | `class` и явный `self` первым аргументом метода |
| `async` / `await` | те же слова, другой цикл событий; это этап после обычных функций |

`True`, `False`, `None` пишутся с большой буквы. Деления `/` даёт `float`, целое деление — `//`. Комментарий — `#`.

## Этап 1. Один вечер, синтаксис

Папка `01-basics`. Один файл `from_js.py`, в котором вы переписываете привычные куски, а не набор задач «угадай число».

- [ ] Отступы, `print`, f-строки, `None`, `bool`
- [ ] `int`, `float`, `str`; `int("10")` и что будет на строке `"10px"`
- [ ] `if / elif / else`, `for`, `while`, `range`, `break`, `continue`
- [ ] Список, срез, `append`. Кортеж и распаковка. Множество. Словарь и `.items()`
- [ ] `def`, значения по умолчанию, `return`. `len`, `sorted`, `enumerate`
- [ ] `try / except` на `ValueError`
- [ ] В конце файла короткая функция, которую в JS вы бы покрыли тестом: например разобрать список задач и вернуть только невыполненные

К концу этапа файл запускается через `python 01-basics/from_js.py` и делает что-то читаемое в терминале.

## Этап 2. Следующий вечер, проектная обвязка

Папка `02-tooling`. Это ближайшие к JS-работе темы с PDF: модули, файлы, окружение, пакеты.

- [x] Модуль: `02-tooling/tasks.py` и `from tasks import ...` в `main.py`. Точка входа `if __name__ == "__main__":`. Запуск из папки `02-tooling`: `python main.py`. Уже печатает открытые задачи, summary, `3` и `None`.

- [ ] `save_tasks` и `load_tasks` — пауза. Черновик начат в `02-tooling/tasks.py`. Вернёмся после блока собеседований по желанию.
- [ ] Окружение и пакет. Аналог `npm install` в папке проекта:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install requests pytest ruff
python -m pip freeze > requirements.txt
```

- [ ] Один вызов `requests` к публичному API
- [ ] List comprehension и один `lambda` в `sorted`
- [ ] `ruff check` и `ruff format` на этих файлах
- [ ] 3–5 тестов pytest на функцию из этапа 1. Запуск: `python -m pytest`

Poetry, Pipenv, conda, uv, pyenv с карты пока не нужны. `venv` и `pip` закрывают тот же зазор, что `npm` на старте.

Задача этапа: список дел в JSON-файле, функции в модуле, тесты на них.

## Этап 3. Проект вашего уровня

Идеи с [roadmap.sh/python/projects](https://roadmap.sh/python/projects) уровня beginner для вас слишком мелкие, если делать их как единственную цель. Их можно брать как форму CLI, а содержание держать ближе к работе.

- [ ] CLI списка дел: добавить, показать, отметить, удалить. Данные в JSON, логика в функциях, pytest на логику
- [ ] Тот же список как HTTP API на FastAPI: `GET` и `POST`, один ресурс, запуск через `uvicorn`. Это прямой мост к React: с фронта вы уже ходите в такие ручки
- [ ] По желанию один скрипт к чужому API (`requests`). Ключ только в переменной окружения

Django, Flask и остальные фреймворки с PDF в этот заход не ставятся. Один сервер — FastAPI.

## Что на карте дальше

После рабочего API, по мере того как код начнёт в них упираться:

| Блок на PDF | Зачем вам |
| --- | --- |
| Classes, `self`, наследование, dunder | Модель уже знакома по JS. Новое — явный `self` и методы вроде `__init__`, `__str__` |
| Decorators | Ближайший аналог — обёртки и HOC. В FastAPI на них висят маршруты и зависимости |
| Type hints, pyright, Pydantic | Если пишете на TypeScript, это следующий вечер после голого синтаксиса. Pydantic здесь как схемы запроса |
| Context manager | `with` вы уже встретите на файлах. Свой менеджер — когда понадобится |
| Iterators, generators | Когда ленивая последовательность заменит список в памяти |
| pytest, ruff | С этапа 2, не «когда-нибудь» |
| Concurrency, GIL, `async` | После синхронного FastAPI. `async def` в эндпоинте выглядит как JS, а модель выполнения другая |
| Data Structures & Algorithms | Отдельная практика задач. К письменю API не привязана |
| Sphinx, Poetry, несколько фреймворков сразу | Когда появится проект, который это оправдывает |

Линия данных (NumPy, Pandas) на этом PDF нет, она на карте AI & Data Scientist. Имеет смысл открыть её, если Python нужен для анализа, а не для API рядом с React.

## Папка

```
learning python/
  PLAN.md
  .gitignore
  hello.py
  01-basics/
    from_js.py
  02-tooling/
  03-projects/
```

## GitHub

Удалённый репозиторий: https://github.com/AnSBeliaev/learning-python. Команды ниже остаются на вас, отсюда они не запускались.

Связать локальную папку с этим адресом:

```powershell
cd "C:\Users\dunice\Desktop\learning python"
git init
git branch -M main
git remote add origin https://github.com/AnSBeliaev/learning-python.git
```

Первый коммит и отправка. В коммит попадут `PLAN.md`, `.gitignore`, `hello.py` и `01-basics/from_js.py`. `.venv`, `__pycache__` и `.env` уже исключены.

```powershell
git add .
git status
git commit -m "Start Python learning plan and first exercises"
git push -u origin main
```

Если `git push` откажется, потому что на GitHub уже есть README или лицензия:

```powershell
git pull origin main --rebase
git push -u origin main
```

## Сейчас

Курс сменён: подготовка к собеседованиям на Python-бэкенд, Junior / Junior+ / Middle-.

Текущий блок лежит в `03-interview/01-language/TOPICS.md`. Это 10 пунктов по базе языка, без готовых ответов. Каждый пункт проверяется в интерпретаторе, объясняется вслух и сохраняется в отдельный `.py` рядом с этим файлом.

`02-tooling` не трогаем: там остаётся черновик `save_tasks`. Следующие блоки (генераторы, декораторы, ООП, потоки и asyncio, FastAPI, LLM и RAG) получат свои папки после разбора этого.