from app import app
from flask import Flask, redirect, render_template, request, session#, flash, abort
from users import login_user, register_user, logout
from db import db
from doctors import doctors_by_city
from sqlalchemy.sql import text
from confirmation import save_appointment, fetch_appointment_id
from appointments import get_available_times
#import secrets

#def generate_csrf_token():
#    if "csrf_token" not in session:
#        session["csrf_token"] = secrets.token_hex(16)
#    return session["csrf_token"]

@app.route("/")
def index():
#    session["csrf_token"] = generate_csrf_token()
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def login():
        
#    return session["csrf_token"]

#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
            
            
    username = request.form["username"]
    password = request.form["password"]
        
    if login_user(username, password):
#        flash("Kirjautuminen onnistui", "success")
        return render_template("location.html")
        
    else:
#        flash("Väärä käyttäjätunnus tai salasana", "error")
        return render_template("login.html")



@app.route("/register",methods=["POST"])
def register():
    
#    return session["csrf_token"]
    
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
    
    new_username = request.form["new_username"]
    new_password = request.form["new_password"]
    
    if register_user(new_username, new_password):
#        flash("Rekisteröidyit onnistuneesti", "success")
        return redirect("/")
        
    else:
#        flash("Rekisteröinti epäonnistui", "error")
        return render_template("register.html")

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")



@app.route("/location")
def location():
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
    if "user_id" in session:
        sql = text("SELECT * FROM cities")
        cities = db.session.execute(sql).fetchall()
        print(cities)   #debug
        
        
        return render_template("location.html", cities=cities)
    else:
        return redirect("/")


@app.route("/doctors", methods=["POST"])
def show_doctors():
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
        
        
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
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
        
    doctor_id = request.form.get("doctor_id")

    if "user_id" in session:
        return render_template("date.html", doctor_id=doctor_id)
    else:
        return redirect("/")

    
    
    
    
@app.route("/appointments", methods=["POST"])
def book_appointment():
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
        
    selected_date = request.form.get("selected_date")
    doctor_id = request.form.get("doctor_id")
    if "user_id" in session and selected_date:
        available_times = get_available_times(doctor_id, selected_date)
        return render_template("appointments.html", date=selected_date, doctor_id=doctor_id, available_times=available_times)
        
    else:
        return redirect("/pick_date")
    
    
    

@app.route("/confirmation", methods=["POST"])
def confirm_appointment():
#    if session["csrf_token"] != request.form["csrf_token"]:
#        abort(403)
        
        
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
