from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for initial testing
recipes = [
    {"id": 1, "title": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "bacon", "parmesan cheese"], "instructions": "1. Cook spaghetti. 2. Fry bacon. 3. Mix eggs and cheese. 4. Combine all."},
    {"id": 2, "title": "Chocolate Chip Cookies", "ingredients": ["flour", "sugar", "butter", "chocolate chips"], "instructions": "1. Mix ingredients. 2. Bake at 350°F. 3. Enjoy!"}
]

# CRUD operations

# Read all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

# Read one recipe by id
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == id), None)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({"message": "Recipe not found"}), 

# Create a new recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = {
        "id": len(recipes) + 1,
        "title": data['title'],
        "ingredients": data['ingredients'],
        "instructions": data['instructions']
    }
    recipes.append(new_recipe)
    return jsonify(new_recipe), 

# Update a recipe
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == id), None)
    if recipe:
        data = request.json
        recipe.update(data)
        return jsonify(recipe)
    else:
        return jsonify({"message": "Recipe not found"}), 404

# Delete a recipe
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe['id'] != id]
    return jsonify({"message": "Recipe deleted"}), 200

if __name__ == '__main__':
    app.run = True