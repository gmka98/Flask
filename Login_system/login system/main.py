from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.data import db, User

app = Flask(__name__, template_folder='templates')
app.secret_key = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.form["username"]
    password = request.form["password"]

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        # Store the user's ID in the session
        session["user_id"] = user.id
        return redirect("/dashboard")
    else:
        error = "Incorrect username or password."
        return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).first()
        return render_template("dashboard.html", username=user.username)
    else:
        return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            error = "Passwords do not match."
            return render_template("register.html", error=error)

        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            error = "Username already exists. Please choose a different username."
            return render_template("register.html", error=error)

        # Create a new user
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.")
        return redirect("/login")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
