from flask import Flask, render_template, url_for, request, session
from captcha.image import ImageCaptcha
import base64
import uuid
import pymongo

app = Flask(__name__)
app.secret_key = '13d2d83e-43b1-4055-a993-0ee84ebc1eba'

from pymongo import MongoClient
client = MongoClient()
db = client['test-database']
captcha_collection = db['captcha_mappings']


@app.before_request
def before_request():
    """ This makes sure every visitor is assigned a unique identifier,
    so that we can ID them when needed. One such case is when we want to
    know if they have entered the correct captcha which was only generated
    for them.
    """
    if 'user_uid' not in session:
        session['user_uid'] = str(uuid.uuid4())


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


def generate_new_captcha_image(captcha_text):
    image = ImageCaptcha()
    image_data = str(base64.b64encode(image.generate(captcha_text).getvalue())).replace("b'", "", 1).replace("'", "")
    return image_data


@app.route('/show_captcha')
def show_captcha():
    captcha_text = str(uuid.uuid4())[:5]
    image_data = generate_new_captcha_image(captcha_text)
    if captcha_collection.find_one({'user_uid' : session['user_uid']}):
        captcha_collection.update({'user_uid': session['user_uid']}, {'$set': {'captcha_text':captcha_text}})
    else:
        captcha_collection.insert_one({'user_uid':session['user_uid'],'captcha_text':captcha_text})
    return render_template('show_captcha.html', data=image_data)


@app.route('/check_captcha', methods=['POST'])
def check_captcha():
    user_provided_captcha_text = request.form['captcha']
    expected_captcha_text = captcha_collection.find_one({'user_uid' : session['user_uid']})['captcha_text']
    if user_provided_captcha_text == expected_captcha_text:
        captcha_passed = True
        captcha_collection.delete_one({'user_uid' : session['user_uid']})
    else:
        captcha_passed = False
    return render_template('captcha_check_result.html', captcha_passed=captcha_passed)


if __name__ == '__main__':
    app.run(debug=True)
