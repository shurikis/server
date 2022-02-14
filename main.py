import os

from flask import Flask
from threading import Thread as Fred

app = Flask(__name__)
a = True


def run_server():
    os.system(r'start.bat')


@app.route('/')
def hello_world():
    global a
    if a:
        print('run server')
        Fred(target=run_server).start()
        a = False
    return 'Hello from Flask!'


if __name__ == '__main__':
    app.run(debug=True)
