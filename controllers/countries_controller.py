from flask import Flask, render_template, Blueprint

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint("countries", __name__)

@country_blueprint.route('/list-countries')
def list_countries():
    all_countries = country_repository.select_all()
    return render_template('/countries/index.html', all_countries=all_countries)

