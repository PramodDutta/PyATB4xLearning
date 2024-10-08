from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    # I can do whatever I want to
    # request.status = 404;
    return '{"name" :"pramod"}'

if __name__ == '__main__':
    app.run(debug=True)