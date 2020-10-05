from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/list-destinations", methods=['GET'])
def list_cities():
    all_cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = all_cities)


# NEW
@cities_blueprint.route("/list-destinations/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)


# CREATE
@cities_blueprint.route("/list-destinations", methods=['POST'])
def create_city():
    new_city = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(new_city, country, visited)
    city_repository.save(city)
    return redirect('/list-destinations')

# SHOW
@cities_blueprint.route("/list-destinations/<id>", methods=['GET'])
def show_cities(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city=city)



# EDIT
@cities_blueprint.route("/list-destinations/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/cities/edit.html', city=city, countries = countries)



# # UPDATE
# @cities_blueprint.route('/list-destinations/<id>', methods=['POST'])
# def update_city(id):
#     name = request.form['name']
#     country_id = request.form['country_id']
#     visited = request.form['visited']
#     country = country_repository.select(country_id)
#     city = City(name, country, visited)
#     city_repository.update(city)
#     return redirect('/list-destinations')



# DELETE
@cities_blueprint.route('/list-destinations/<id>/delete', methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/list-destinations')