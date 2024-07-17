from flask import Flask
app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
