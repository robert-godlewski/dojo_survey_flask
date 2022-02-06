from flask import Flask, render_template


app = Flask(__name__)

app.secret_key = 'server_hello'

@app.route('/')
def counter(): return render_template("index.html")


if __name__ == "__main__": app.run(debug=True, port=8000)
