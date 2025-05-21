from app import myapp_obj, db, socketio
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, flash, abort, jsonify, request
from app.forms import LoginForm, RegistrationForm, PostForm, RecipeForm, CommentForm, DeleteForm, EditProfileForm
from app.models import User, Post, Recipe, Comment, Rating
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import send, emit

@myapp_obj.route("/")
def home():
    return render_template("homepage.html", user=current_user)

@myapp_obj.route("/accounts")
@login_required
def users():
    users = User.query.all()
    return render_template("accounts.html", users=users)

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
        login_user(new_user)
        flash(f'Welcome, {new_user.username}!', 'success')
        return redirect(url_for('home'))
    return render_template("registration.html", form=form)

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@myapp_obj.route("/showall", methods=['GET', 'POST'])
def createPost():
    form = PostForm()
    posts = Post.query.all()
    if form.validate_on_submit():
        p = Post(username=form.username.data, body=form.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect("/showall")
    return render_template("post.html", form=form, posts=posts)

@myapp_obj.route("/create-recipe", methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            username=current_user.username
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipes'))
    return render_template("create_recipe.html", form=form)

@myapp_obj.route("/recipes")
def recipes():
    query = request.args.get('q', '').strip()
    if query:
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
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.username != current_user.username:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe has been deleted.', 'info')
    return redirect(url_for('recipes', delete_form=DeleteForm()))

@myapp_obj.route('/edit-recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.username != current_user.username:
        abort(403)
    form = RecipeForm(obj=recipe)
    delete_form = DeleteForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        db.session.commit()
        flash('Recipe has been updated.', 'success')
        return redirect(url_for('recipes', delete_form=DeleteForm()))
    return render_template('edit_recipe.html', form=form, recipe=recipe, delete_form=DeleteForm())

@myapp_obj.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        results = Recipe.query.filter(
            Recipe.title.ilike(f"%{query}%") | 
            Recipe.ingredients.ilike(f"%{query}%")
        ).all()
    else:
        results = []
    return render_template("recipes.html", recipes=results)

@myapp_obj.route('/favorites', methods=['GET'])
@login_required
def favorites():
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

@myapp_obj.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            recipe_id=recipe.id,
            username=current_user.username
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("recipe_detail", recipe_id=recipe.id, delete_form=DeleteForm()))
    comments = Comment.query.filter_by(recipe_id=recipe.id).all()
    return render_template("recipe_detail.html", recipe=recipe, comments=comments, form=form, delete_form=DeleteForm())

@myapp_obj.route("/profile")
@login_required
def profile():
    user_recipes = Recipe.query.filter_by(username=current_user.username).all()
    user = User.query.get(current_user.id)
    return render_template("profile.html", user=user, recipes=user_recipes)

@myapp_obj.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("home"))
    return render_template("edit_profile.html", form=form)

@myapp_obj.route("/test-logo")
def test_logo():
    return render_template("test_logo.html")

@myapp_obj.route('/rate-recipe/<int:recipe_id>', methods=['POST'])
@login_required
def rate_recipe(recipe_id):
    value = int(request.form.get('rating', 0))
    if value < 1 or value > 5:
        flash('Invalid rating.', 'danger')
        return redirect(url_for('recipe_detail', recipe_id=recipe_id))
    rating = Rating.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
    if rating:
        rating.value = value
    else:
        rating = Rating(user_id=current_user.id, recipe_id=recipe_id, value=value)
        db.session.add(rating)
    db.session.commit()
    flash('Rating submitted!', 'success')
    return redirect(url_for('recipe_detail', recipe_id=recipe_id))

@socketio.on('message')
def handle_message(data):
    send({'username': current_user.username, 'message': data['message']}, broadcast=True)

@myapp_obj.route('/chat')
@login_required
def chat():
    return render_template('chat.html')
