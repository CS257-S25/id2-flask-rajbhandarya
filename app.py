''' This is the main file of the Flask app.'''
from flask import Flask
from ProductionCode.data import get_data
from ProductionCode.random_recipe import get_random_recipes

app = Flask(__name__)
@app.route('/')
def homepage():
    ''' Defines the homepage of the app. '''
    return "Hello, this is the homepage. To find a random recipe, "+ \
        "go type /number after the current URL where number " + \
              "is the amount of random recipes you want."

@app.route('/<number>', strict_slashes=False)
def get_random(number):
    ''' Returns a random recipe from the list of recipes. '''
    data = get_data()
    recipes = get_random_recipes(data, int(number))
    random = parse_random(recipes)
    return random

def parse_random(recipes):
    ''' Parses the random recipes into a string. '''
    recipes_as_strings = [' - '.join(map(str, recipe)) for recipe in recipes]
    return "<br>----------------------------------<br>".join(recipes_as_strings)

@app.errorhandler(404)
def page_not_found(e):
    ''' Returns a 404 error message. '''
    print(e)
    return "Sorry, wrong format. Type /number after the current URL."

@app.errorhandler(500)
def python_bug(e):
    ''' Returns a 500 error message. '''
    print(e)
    return "Eek, a bug!"


if __name__ == '__main__':
    app.run()
