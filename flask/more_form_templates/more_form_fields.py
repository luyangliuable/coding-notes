from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
#### Note the new import statement
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


class CommentForm(FlaskForm):
  #### Add a validator argument in the StringField
  comment =  StringField("Comment", validators=[DataRequired()])
  recipe_type = RadioField("Type", choices=recipe_categories)
  recipe_categories = "choices"
  submit = SubmitField("Add Comment")

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html", template_recipes=recipes)


@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  #### Replace 'True' with form validation
  # if True:
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)


@app.route("/about")
def about():
  return render_template("about.html")
