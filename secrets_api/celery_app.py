from secrets_api.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("secrets_api.tasks.example",)
