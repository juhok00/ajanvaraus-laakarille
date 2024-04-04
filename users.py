from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text





def login_user(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        print("Ei löytynyt")     #       debug
        return False
    else:
        user_id, user_password_hash = user
        if check_password_hash(user_password_hash, password):
            session["user_id"] = user_id
            print("user id:", session["user_id"])    #       debug
            return True
        else:
            print("salasana epäonnistui")     #       debug
            return False
        
def logout():
    del session["user_id"]
    

def register_user(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return True
    except Exception as e:
        print("Database insertion error:", e)
        return False


def user_id():
    return session.get("user_id",0)
