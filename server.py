from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route('/index', methods=['POST'])
def index():
    temp = request.form['ticker']
    return render_template('index.html', ticker=temp)

if __name__ == "__main__":
    app.run(debug = True)