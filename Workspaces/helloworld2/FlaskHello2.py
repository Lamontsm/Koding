from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! From Flask Tutorial"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # from Flask tutorial
    # added host='0.0.0.0' to host - that worked!