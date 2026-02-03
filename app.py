from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, User, Challenge, Submission
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()

    # Add sample challenges if empty
    if Challenge.query.count() == 0:

        challenges = [
            Challenge(
                name="Basic Crypto",
                description="Decode Base64: ZmxhZ3tCYXNlNjRfSXNfRnVuIX0=",
                flag="flag{Base64_Is_Fun!}",
                points=100
            ),
            Challenge(
                name="HTML Source Flag",
                description="View page source of example.com and find hidden flag (demo).",
                flag="flag{view_source_master}",
                points=150
            )
        ]

        db.session.add_all(challenges)
        db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("register"))

        hashed = generate_password_hash(password)
        new_user = User(username=username, password=hashed)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))

        flash("Invalid credentials")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
@login_required
def dashboard():

    challenges = Challenge.query.all()

    return render_template(
        "dashboard.html",
        username=current_user.username,
        challenges=challenges,
        score=current_user.score
    )


# LEADERBOARD
@app.route("/leaderboard")
@login_required
def leaderboard():
    # Show all users sorted by score descending
    users = User.query.order_by(User.score.desc()).all()
    return render_template("leaderboard.html", users=users)


# Create challenge compatibility route
@app.route("/new_challenge")
@login_required
def new_challenge():
    # redirect to /create for compatibility with UI
    return redirect(url_for('create'))


# CREATE CHALLENGE (simple admin version)
@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        flag = request.form.get("flag")
        points = request.form.get("points")

        # Basic validation
        if not name or not description or not flag or not points:
            flash("All fields are required")
            return redirect(url_for("create"))

        try:
            pts = int(points)
        except ValueError:
            flash("Points must be a number")
            return redirect(url_for("create"))

        new_ch = Challenge(name=name, description=description, flag=flag, points=pts)
        db.session.add(new_ch)
        db.session.commit()

        flash("Challenge created")
        return redirect(url_for("dashboard"))

    return render_template("create.html")


# VIEW CHALLENGE + SUBMIT FLAG
@app.route("/challenge/<int:challenge_id>", methods=["GET", "POST"])
@login_required
def challenge(challenge_id):

    challenge = Challenge.query.get_or_404(challenge_id)

    if request.method == "POST":
        submitted_flag = request.form.get("flag")

        already = Submission.query.filter_by(
            user_id=current_user.id,
            challenge_id=challenge.id,
            correct=True
        ).first()

        if already:
            flash("Already solved")
            return redirect(url_for("challenge", challenge_id=challenge.id))

        if submitted_flag == challenge.flag:
            submission = Submission(
                user_id=current_user.id,
                challenge_id=challenge.id,
                correct=True
            )

            current_user.score += challenge.points

            db.session.add(submission)
            db.session.commit()

            flash("Correct Flag! Points Added")
        else:
            flash("Wrong Flag")

    return render_template("challenge.html", challenge=challenge)


# LOGOUT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
