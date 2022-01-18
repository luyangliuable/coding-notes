<!DOCTYPE html>
<html>
  <body>
    <div>
      <!-- Replace URL string with url_for -->
      <a href="{{url_for('recipes')}}">Recipes</a>
      |
      <!-- Replace URL string with url_for -->
      <a href="/about">About</a>
    </div>
    {% block content %}
    {% endblock %}
  </body>
</html>
