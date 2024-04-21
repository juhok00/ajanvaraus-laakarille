from db import db
from sqlalchemy.sql import text


def doctors_by_city(city_id):
    sql = text("""
    SELECT d.id, d.doctor_name, s.specialization_name
    FROM doctors d
    JOIN doctor_specialization ds ON d.id = ds.doctor_id
    JOIN specialization s on ds.specialization_id = s.id
    WHERE d.city_id = :city_id
    """)
    
    
    result = db.session.execute(sql, {"city_id": city_id}).fetchall()
    return result