from app import app
from flask import redirect, render_template, request, session
from users import login, register, logout


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/login",methods=["GET", "POST"])
def login():
        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if login(username, password):
            session["username"] = username
            return redirect("/location")
        else:
            return render_template("welcome.html", error= "Väärä käyttäjätunnus tai salasana")
    else:
        return redirect("welcome.html")



@app.route("/register",methods=["POST"])
def register():
    new_username = request.form["new_username"]
    new_password = request.form["new_password"]
    
    if register(new_username, new_password):
        return redirect("/login")
    else:
        return render_template("welcome.html", error="Rekisteröinti epäonnistui")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")



@app.route("/location")
def location():
    if "username" in session:
        return render_template("location.html")
    else:
        return redirect("/")
