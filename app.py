from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/priya')
def priya():
    return "wrgrgr"


# @app.route('/')
# def homepage():
#     return render_template('index.html')


# @app.route('/')
# def homepage():
#     return render_template('index.html')


# @app.route('/')
# def homepage():
#     return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)













    