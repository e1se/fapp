from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/notnews')
def notnews():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
