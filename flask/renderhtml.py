from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter')
def reporter():
    """
    Navigate to http://localhost:5000/ 
    """
    return """
    <h2>Reporter Bio</h2>
    <a href="/">Return to home page</a>
    """
