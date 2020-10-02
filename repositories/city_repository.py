from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (city_name) VALUES (%s) RETURNING *"
    values = [city.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city