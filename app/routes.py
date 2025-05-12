from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import PostForm
from app.models import User
from app.models import Post
from app import db
from flask import flash


from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for
# Import Recipe model and RecipeForm
from app.models import Recipe
from app.forms import RecipeForm
from flask_login import login_required

from flask import abort  # Import abort to handle unauthorized deletes
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    return render_template("hello.html")

@myapp_obj.route("/accounts")
@login_required
def users():
    # user = 'Chloe Knott', 'chloeknott@sjsu.edu'
    users = User.query.all()
    return render_template("accounts.html", users=users)
    #header =  "<h2>My User Accounts</h2>"
    #usernames = ["<ol>"] + [f"<li>{user.username}</li>" for user in User.query.all()] + ["</ol>"]
    #return "\n".join([header] + usernames)


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main'))
        else:
            flash('Invalid email or password', 'danger')
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)

    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))

@myapp_obj.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        u = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password  # ✅ save hash into correct field
        )
        db.session.add(u)
        db.session.commit()
        return redirect("/login")  # Redirect to login instead of /
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
        return redirect(url_for('main'))  # Redirect to homepage after creation

    # If GET request or form not valid, render the create recipe page again
    return render_template("create_recipe.html", form=form)

@myapp_obj.route("/recipes")
@login_required
def recipes():
    all_recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=all_recipes)


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
    return redirect(url_for('main'))  # Redirect to homepage after deletion

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
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))  # Refresh the page

    comments = Comment.query.filter_by(recipe_id=recipe.id).all()  # Load all comments for this recipe
    return render_template("recipe_detail.html", recipe=recipe, comments=comments, form=form)

# Route for editing the currently logged-in user's profile
@myapp_obj.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    # Pre-fill the form with the current user's data
    form = RegistrationForm(obj=current_user)

    # If the user submits the form with valid data
    if form.validate_on_submit():
        # Update user fields
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = generate_password_hash(form.password.data)  # Securely hash new password

        db.session.commit()  # Save changes to the database
        flash("Profile updated successfully!", "success")
        return redirect(url_for("main"))  # Redirect to home

    return render_template("edit_profile.html", form=form)  # Show the form again


# @myapp_obj.route("/showall")
# def posts():
#     post = Post.query.all()
#     return render_template("post.html", post = post)

