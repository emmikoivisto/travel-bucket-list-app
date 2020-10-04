from flask import Flask, render_template, request
from flask import Blueprint

from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/list-destinations")
def list_cities():
    all_cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = all_cities)

@cities_blueprint.route("/list-destinations/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)