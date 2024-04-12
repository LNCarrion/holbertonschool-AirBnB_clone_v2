<<<<<<< HEAD
#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)

def hello():
    return('Hello HBNB!') 

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return("HBNB")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 
>>>>>>> 7dec229b36a7573e937c1263a1aa885475f2649f
