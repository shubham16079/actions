from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! this will be integrated by github actions"

if __name__ == '__main__':
    app.run(debug=True)