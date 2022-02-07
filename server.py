from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

app.secret_key = 'server_hello'

@app.route('/')
def counter(): return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = str(request.form['name'])
    session['location'] = str(request.form['location'])
    session['fav_lang'] = str(request.form['fav_lang'])
    session['comment'] = str(request.form['comment'])
    # print(f"session details are: {str(session)}")
    return redirect('/result')

@app.route('/result')
def result(): return render_template("result.html")

# This section is only used for debugging
'''@app.route('/clear')
def clear_session():
    session.clear()
    print(f"Cleared session: {str(session)}")
    return redirect('/')'''


if __name__ == "__main__": app.run(debug=True, port=8000)
