from app import app
from flask import Flask, redirect, render_template, request, session
from users import login_user, register_user, logout
from db import db
from doctors import doctors_by_city
from sqlalchemy.sql import text
from confirmation import save_appointment, fetch_appointment_id
from appointments import get_available_times


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
    print("city id: ", request.form.get("city_id"))        # debug
    if "user_id" in session:
        city_id = request.form.get("city_id")
        doctors = doctors_by_city(city_id)
        print(doctors)      # debug
        return render_template("doctors.html", doctors=doctors)
    else:
        return redirect("/")
    

    
    
@app.route("/pick_date", methods=["POST"])
def pick_date():
    doctor_id = request.form.get("doctor_id")

    if "user_id" in session:
        return render_template("date.html", doctor_id=doctor_id)
    else:
        return redirect("/")

    
    
    
    
@app.route("/appointments", methods=["POST"])
def book_appointment():
    selected_date = request.form.get("selected_date")
    doctor_id = request.form.get("doctor_id")
    if "user_id" in session and selected_date:
        available_times = get_available_times(doctor_id, selected_date)
        return render_template("appointments.html", date=selected_date, doctor_id=doctor_id, available_times=available_times)
        
    else:
        return redirect("/pick_date")
    
    
    

@app.route("/confirmation", methods=["POST"])
def confirm_appointment():
    doctor_id = request.form.get("doctor_id")
    details = request.form.get("details")
    date = request.form.get("appointment_date")
    appointment_time = request.form.get("appointment_time")
    
    if "user_id" in session:
        appointment_id = fetch_appointment_id(appointment_date, appointment_time)
        if appointment_id and confirm_appointment(appointment_id):
            return render_template("confirmation.html", appointment_date=appointment_date, appointment_time=appointment_time, details=details)
        else:
            return redirect("/appointments")
    else:
        return redirect("/")
