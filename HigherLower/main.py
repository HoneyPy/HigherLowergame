from flask import Flask
import random

app = Flask(__name__)


random_number = random.randint(0, 9)

@app.route('/')
def home():
    return '''
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess a number">
    '''

@app.route('/<int:number>')
def guess_number(number):
    if number < random_number:
        response = '''
        <h1 style="color: blue;">{} is too low!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Too low">
        '''.format(number)
    elif number > random_number:
        response = '''
        <h1 style="color: red;">{} is too high!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Too high">
        '''.format(number)
    else:
        response = '''
        <h1 style="color: green;">{} is just right!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct">
        '''.format(number)
    return response

if __name__ == '__main__':
    app.run(debug=True)
