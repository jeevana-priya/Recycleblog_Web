
from flask import Flask, render_template,url_for,redirect

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def Contact():
    return render_template('contact.html')


@app.route('/methods')
def methods():
    return render_template('methods.html')
if __name__ == "__main__":
    app.run(debug=True)













    