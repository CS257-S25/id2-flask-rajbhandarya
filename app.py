'''Replace me with your flask app'''
from flask import Flask
import csv
from ProductionCode.data import get_data
from ProductionCode.random_recipe import get_random_recipes

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Hello, this is the homepage. To find a random recipe, go type /number after the current URL where number is the amount of random recipes you want."
@app.route('/<number>', strict_slashes=False)
def get_random(number):
    data = get_data()
    random = get_random_recipes(data, int(number))

    recipes_as_strings = [' - '.join(map(str, recipe)) for recipe in random]
    return "<br>----------------------------------<br>".join(recipes_as_strings)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, wrong format. Type /number after the current URL where number is the amount of random recipes you want"

@app.errorhandler(500)
def python_bug(e):
    return "Eek, a bug!"


if __name__ == '__main__':
    app.run()