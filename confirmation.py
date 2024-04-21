
from db import db
from sqlalchemy.sql import text

def save_appointment(appointment_time):
    sql = text("""
    UPDATE appointment
    SET reserved = True
    WHERE id = :appointment_id
    RETURNING id
    """)
    
    
    result = db.session.execute(sql, {"appointment_id": appointment_id})
    db.session.commit()
    return result.rowcount == 1




def fetch_appointment_id(appointment_date, appointment_time):
    sql = text("""
    SELECT id FROM appointment
    WHERE appointment_date = :appointment_date AND appointment_time = :appointment_time
    """)
    
    result = db.session.execute(sql, {"appointment_date": appointment_date, "appointment_time": appointment_time})
    appointment = result.fetchone()
    return appointment.id if appointment else None

    