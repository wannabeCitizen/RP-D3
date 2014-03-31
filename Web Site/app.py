from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/hackathon', methods=['POST', 'GET'])
def hackathon():
    return render_template('hackathon.html')

@app.route('/journal', methods=['POST', 'GET'])
def journal():
    return render_template('journal.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(debug=True)