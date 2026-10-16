# Django Todo App

A small task manager built with Django. Add tasks with descriptions, view them in a list, mark them complete, edit them, and remove them with a confirmation step. Tasks are stored in a local SQLite database.

## Features

- Create tasks with a title and optional description
- View tasks, newest first
- Mark tasks complete or incomplete
- Edit task details
- Delete tasks after confirming
- See when each task was created
- Bootstrap-based layout

## Built with

- Python and Django
- SQLite
- HTML and Bootstrap 5

## Project structure

```text
todo-django/
├── manage.py
├── myproject/
│   ├── settings.py
│   └── urls.py
├── todo/
│   ├── migrations/
│   ├── templates/
│   │   └── todo/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_delete_confirm.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

## Run locally

Run these commands from the directory containing `manage.py`.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install dependencies, prepare the database, and start Django:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## Main routes

| Route | Purpose |
| --- | --- |
| `/` | List tasks |
| `/add/` | Create a task |
| `/edit/<task-id>` | Edit a task |
| `/delete/<task-id>/` | Confirm and delete a task |
| `/toggle/<task-id>` | Toggle task completion |
| `/admin/` | Django admin site |

## Author

Manish Gupta
