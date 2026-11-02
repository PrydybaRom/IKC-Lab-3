from flask import Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Flask Docker image version 2.0!</h1>"

if __name__ == "__main__":
    app.run(host="db", port=5000)
