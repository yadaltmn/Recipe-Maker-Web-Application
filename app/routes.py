from app import myapp_obj, db
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm, PostForm, RecipeForm, CommentForm, DeleteForm, EditProfileForm
from app.models import User, Post, Recipe, Comment, Rating
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from flask import abort
from flask import jsonify
from flask import request
from flask import abort  # Import abort to handle unauthorized deletes
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    return render_template("hello.html")

@myapp_obj.route("/accounts")
@login_required
def users():
    users = User.query.all()
    return render_template("accounts.html", users=users)
    #header =  "<h2>My User Accounts</h2>"
    #usernames = ["<ol>"] + [f"<li>{user.username}</li>" for user in User.query.all()] + ["</ol>"]
    #return "\n".join([header] + usernames)


@myapp_obj.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Welcome, {user.username}!', 'success')  
            return redirect(url_for('home')) 
        else:
            flash('Invalid username or password.', 'danger')

    return render_template("login.html", form=form)

@myapp_obj.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)  # Auto-login after registration
        flash(f'Welcome, {new_user.username}!', 'success')
        return redirect(url_for('home'))  # Redirect to homepage
    
    return render_template("registration.html", form=form)


@myapp_obj.route("/showall", methods=['GET', 'POST'])
def createPost():
    form = PostForm()
    posts = Post.query.all()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.body.data}")
        p = Post(username=form.username.data, body=form.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect("/showall")
    else:
        print("MOOOO MOOO")
    return render_template("post.html", form=form, posts=posts)


@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


# Route for creating a new recipe
@myapp_obj.route("/create-recipe", methods=['GET', 'POST'])
@login_required  # Only allow logged-in users to access this page
def create_recipe():
    form = RecipeForm()  # Initialize the recipe form

    if form.validate_on_submit():  # Check if the form was submitted correctly
        # Create a new Recipe object using form data
        recipe = Recipe(
            title=form.title.data,  # Recipe title from form input
            description=form.description.data,  # Recipe description
            ingredients=form.ingredients.data,  # Ingredients from form
            instructions=form.instructions.data,  # Instructions from form
            username=current_user.username  # Store the username of the creator
        )
        db.session.add(recipe)  # Add the new recipe to the database session
        db.session.commit()  # Commit/save the new recipe to the database
        flash('Recipe created successfully!', 'success')  # Show a success message to user
        return redirect(url_for('recipes'))  # Redirect to homepage after creation

    # If GET request or form not valid, render the create recipe page again
    return render_template("create_recipe.html", form=form)


#View all recipes
@myapp_obj.route("/recipes")
def recipes():
    query = request.args.get('q', '').strip()
    if query:
        # Filter by title or ingredients, case-insensitive
        filtered_recipes = Recipe.query.filter(
            (Recipe.title.ilike(f"%{query}%")) |
            (Recipe.ingredients.ilike(f"%{query}%"))
        ).all()
    else:
        filtered_recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=filtered_recipes, delete_form=DeleteForm())


@myapp_obj.route('/delete-recipe/<int:recipe_id>', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Get the recipe or 404 error if not found
    # Check if the current user owns the recipe
    if recipe.username != current_user.username:
        abort(403)  # Forbidden error if not the owner

    db.session.delete(recipe)  # Delete the recipe
    db.session.commit()  # Save the change to the database
    flash('Recipe has been deleted.', 'info')  # Show a message
    return redirect(url_for('recipes', delete_form=DeleteForm()))  # Redirect to recipes page after deletion


@myapp_obj.route('/edit-recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Get the recipe or 404 error if not found
    # Check if the current user owns the recipe
    if recipe.username != current_user.username:
        abort(403)  # Forbidden error if not the owner
    form = RecipeForm(obj=recipe)
    delete_form = DeleteForm() 

    if form.validate_on_submit():
        # Update recipe fields from form data
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data

        db.session.commit()  # Save the changes to the database
        flash('Recipe has been updated.', 'success')
        return redirect(url_for('recipes', delete_form=DeleteForm()))  # Redirect to recipes page after editing

    return render_template('edit_recipe.html', form=form, recipe=recipe, delete_form=DeleteForm())


# Route for searching recipes by title or ingredient
@myapp_obj.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # Get search term from query string (?q=...)
    if query:
        # Filter recipes whose title or ingredients contain the query (case-insensitive)
        results = Recipe.query.filter(
            Recipe.title.ilike(f"%{query}%") | 
            Recipe.ingredients.ilike(f"%{query}%")
        ).all()
    else:
        results = []  # No search term provided
    # Reuse recipes.html to display results
    return render_template("recipes.html", recipes=results)


# Route to view favorited recipes
@myapp_obj.route('/favorites', methods=['GET'])
@login_required
def favorites():  
    # Get only the current user's favorited recipes
    favorite_recipes = current_user.favorite_recipes
    return render_template("favorites.html", favorites=favorite_recipes)


@myapp_obj.route('/favorite/<int:recipe_id>', methods=['POST'])
@login_required
def favorite_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe in current_user.favorite_recipes:
        current_user.favorite_recipes.remove(recipe)
        db.session.commit()
        return jsonify({'status': 'unfavorited'})
    else:
        current_user.favorite_recipes.append(recipe)
        db.session.commit()
        return jsonify({'status': 'favorited'})



# Route to view a recipe's details and submit comments
@myapp_obj.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Fetch the recipe or show 404
    form = CommentForm()  # Create a comment form instance
    # When user submits a comment
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            recipe_id=recipe.id,
            username=current_user.username  # Associate comment with current user
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("recipe_detail", recipe_id=recipe.id, delete_form=DeleteForm()))  # Refresh the page

    comments = Comment.query.filter_by(recipe_id=recipe.id).all()  # Load all comments for this recipe
    return render_template("recipe_detail.html", recipe=recipe, comments=comments, form=form, delete_form=DeleteForm())


#Route for viewing your profile
@myapp_obj.route("/profile")
@login_required
def profile():  
    #Get the current user's recipes
    user_recipes= Recipe.query.filter_by(username=current_user.username).all()
    
    #Get user details from the database
    user = User.query.get(current_user.id)
    return render_template("profile.html", user=user, recipes=user_recipes)


# Route for editing the currently logged-in user's profile
@myapp_obj.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    
    form = EditProfileForm(obj=current_user)

    # If the user submits the form with valid data
    if form.validate_on_submit():
        # Update user fields
        current_user.username = form.username.data
        #current_user.email = form.email.data
        current_user.bio = form.bio.data
        current_user.password = generate_password_hash(form.password.data)  # Securely hash new password

        db.session.commit()  # Save changes to the database
        flash("Profile updated successfully!", "success")
        return redirect(url_for("main"))  # Redirect to home

    return render_template("edit_profile.html", form=form)  # Show the form again


@myapp_obj.route("/test-logo")
def test_logo():
    return render_template("test_logo.html")


@myapp_obj.route("/")
def home():
    return render_template("homepage.html", user=current_user)


# Recipe rating route
@myapp_obj.route('/rate-recipe/<int:recipe_id>', methods=['POST'])
@login_required
def rate_recipe(recipe_id):
    value = int(request.form.get('rating', 0))
    if value < 1 or value > 5:
        flash('Invalid rating.', 'danger')
        return redirect(url_for('recipe_detail', recipe_id=recipe_id))

    rating = Rating.query.filter_by(
        user_id=current_user.id,
        recipe_id=recipe_id
    ).first()

    if rating:
        rating.value = value
    else:
        rating = Rating(
            user_id=current_user.id,
            recipe_id=recipe_id,
            value=value
        )
        db.session.add(rating)
    
    db.session.commit()
    flash('Rating submitted!', 'success')
    return redirect(url_for('recipe_detail', recipe_id=recipe_id))




