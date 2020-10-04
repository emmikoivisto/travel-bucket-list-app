from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    all_cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], country, row['visited'], row['id'])
        all_cities.append(city)
    return all_cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        city = City(result['name'], country, result['visited'], result['id'])
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    city = None
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country, city.visited, city.id]
    print(values)
    run_sql(sql, values)