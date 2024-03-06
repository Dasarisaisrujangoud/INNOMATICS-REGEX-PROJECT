from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    txt = request.form['txt']
    patn = request.form['patn']
    matches = [(match.start(), match.end(), match.group()) for match in re.finditer(patn, txt)]

    return render_template('index.html', matches=matches)


@app.route('/email', methods=['POST'])
def email():
    email = request.form['email']
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return 'Valid email address.'
    else:
        return 'Invalid email address.'
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
