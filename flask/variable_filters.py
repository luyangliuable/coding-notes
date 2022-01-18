<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <!-- Make template_recipe title case -->
    <h1>{{ template_recipe | title}}</h1>
    <!-- Ensure a default description -->  
    <p>{{ template_description | default("A " + template_recipe + " recipe")}}</p>
    <!-- Output number of ingredients --> 
    <h3>Ingredients - {{template_ingredients | length}}</h3>
    <ul>
      <li>{{ template_ingredients[0] }}</li>
      <li>{{ template_ingredients[1] }}</li>
      <li>{{ template_ingredients[2] }}</li>
    </ul>
    <h3>Instructions</h3>
    <ol>
      <!-- Ensure sorted instruction dictionary -->
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
  </body>
</html>
