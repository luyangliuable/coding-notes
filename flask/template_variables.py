<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe }}</h1>
    <p>{{ template_description }}</p>
    <h3>Ingredients</h3>
    <ul>
      <!-- Ingredients list elements
      should fill the <li> tags -->
      <li>{{template_ingredients[0]}}</li>
      <li>{{template_ingredients[1]}}</li>
      <li>{{template_ingredients[2]}}</li>
    </ul>
  </body>
</html>


from flask import Flask, render_template
from helper import recipes, descriptions, ingredients

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
  #### Add template variables as 
  #### variable assignment arguments
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id])
