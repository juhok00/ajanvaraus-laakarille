from app import app
from flask import Flask, redirect, render_template, request, session
from users import login_user, register_user, logout
from db import db

from sqlalchemy.sql import text


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def login():
        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if login_user(username, password):
            return redirect("/location")
        else:
            return render_template("login.html", error= "Väärä käyttäjätunnus tai salasana")
    else:
        return redirect("login.html")



@app.route("/register",methods=["POST"])
def register():
    new_username = request.form["new_username"]
    new_password = request.form["new_password"]
    
    if register_user(new_username, new_password):
        return redirect("/")
    else:
        return render_template("login.html", error="Rekisteröinti epäonnistui")

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")



@app.route("/location")
def location():
    if "user_id" in session:
        sql = text("SELECT * FROM cities")
        cities = db.session.execute(sql).fetchall()
        return render_template("location.html", cities=cities)
    else:
        return redirect("/")


@app.route("/doctors", methods=["POST"])
def show_doctors():
    if "user_id" in session:
        city_id = request.form["city.id"]
        doctors = doctors_by_city(city_id)
        return render_template("doctors.html", doctors=doctors, city_id=city_id)
    else:
        return redirect("/")
