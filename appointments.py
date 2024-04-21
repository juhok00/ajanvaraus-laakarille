from db import db
from sqlalchemy.sql import text


def get_available_times(date, doctor_id):

    sql = text("""
    SELECT appointment_time
    FROM appointment
    WHERE appointment_date = :date AND doctor_id = :doctor_id AND reserved = False
    ORDER BY appointment_time
    """)
    
    
    
    result = db.session.execute(sql, {"date": date, "doctor_id": doctor_id})
    return [time[0] for time in result.fetchall()]



def save_appointment(doctor_id, date, time, details):
    sql = text("""
    INSERT INTO appointment (doctor_id, appointment_date, appointment_time, reserved, details)
    VALUES (:doctor_id, :date, :time, True, :details)
    RETURNING id
    """)
    result = db.session.execute(sql, {"doctor_id": doctor_id, "date": date, "time": time, "details": details})
    db.session.commit()
    return result.fetchone()[0]
