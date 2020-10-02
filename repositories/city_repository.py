from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, visited) VALUES (%s, %s) RETURNING *"
    values = [city.name, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    all_cities = []
    sql = "SELECT * FROM cities
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['visited'], row['id'])
        all_cities.append(city)
    return all_cities

def select(id)
    sql = 


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

    