# Body Weight Weblist

This is CRUD web. It was created for SIRCLO test using python and Django

## Installation
Please use virtual environment to avoid package installation errors during using the web.
Make sure python was already install on your system.

Open command prompt, activate the virtual env by change directory into Body Weight Test/env/Scripts/ then hit activate.bat until you see (env) on your cmd prompt

```bash
(env) <your-dir>/Body Weight Test/env/Scripts
```

## How to use
```bash
cd <your-dir>/Body Weight Test/BodyWeight
```
```bash
manage.py makemigrations curd_body_weight
```
```bash
manage.py migrate
```
```bash
manage.py runserver
```
If the program start normally, it will serve on your [localhost](http://127.0.0.1:8000/)
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 10, 2022 - 02:03:54
Django version 4.0.1, using settings 'BodyWeight.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## About
The main CURD function are in "curd_body_weight" project app.