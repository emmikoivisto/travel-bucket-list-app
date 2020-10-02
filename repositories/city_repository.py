from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, visited) VALUES (%s, %s) RETURNING *"
    values = [city.name, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city