# This file needs to be not named __main__ because it causes issues with Gunicorn

from personal.web.app_tornado import App

app = App()

if __name__ == "__main__":
    app.serve()
