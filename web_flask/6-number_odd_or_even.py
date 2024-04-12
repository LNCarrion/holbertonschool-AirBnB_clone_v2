#!/usr/bin/python

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return('Hello HBNB!') 


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def text(text):
    text = text.replace("_", " ")
    return( "C {}".format(text))

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text):
    text = text.replace("_", " ")
    return("python {}".format(text))

@app.route("/number/<n>", strict_slashes=False)
def n_is_number(n):
    if n.isdigit():
        return("{} is a number".format(n))
    else:
        abort(404)

@app.route('/number_template/<n>', strict_slashes=False)
def num_temp(n):
    if n.isdigit():
        return(render_template('5-number.html', n=n))
    else:
        abort(404)

@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_or_odd(n):
    if n.isdigit():
        n = int(n)
        text = "even" if (n % 2) == 0 else "odd"
        return(render_template('6-number_odd_or_even.html', n=n, text=text))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return("""
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    """, 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
