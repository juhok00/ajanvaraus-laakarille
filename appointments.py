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
    times = [time[0] for time in result.fetchall()]
    return times

