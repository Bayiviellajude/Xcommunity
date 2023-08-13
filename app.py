from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/forums')
def forums():
    return render_template('forums.html')

@app.route('/groups')
def groups():
    return render_template('groups.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
