from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import PostForm
from app.models import User
from app.models import Post
from app import db

from flask_login import logout_user
from flask import redirect, url_for
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "username"
    return render_template("hello.html", name=name)

@myapp_obj.route("/accounts")
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
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        u = User(username=form.username.data, email=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))

@myapp_obj.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        u = User(username=form.username.data, email=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO")
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
    logout_user()  # Logs out the user
    login_manager = LoginManager()
    login_manager.init_app(app)  # <-- This line connects Flask-Login to your 
    return redirect(url_for("login")) 

# @myapp_obj.route("/showall")
# def posts():
#     post = Post.query.all()
#     return render_template("post.html", post = post)

