from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/prompt_name')
def prompt_name():
    return render_template('prompt_name.html')


@app.route('/say_hello', methods=['POST'])
def say_hello():
    name_of_user = str(request.form['username']).capitalize()
    greeting = 'How are you doing today mate?'
    return render_template('greeting.html', name_of_user=name_of_user, greeting=greeting)


if __name__ == '__main__':
    app.run(debug=True)
