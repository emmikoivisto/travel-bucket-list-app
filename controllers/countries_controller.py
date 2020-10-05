from flask import Flask, render_template, Blueprint, request, redirect

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint("countries", __name__)

# INDEX
@country_blueprint.route('/list-countries', methods=['GET'])
def list_countries():
    all_countries = country_repository.select_all()
    return render_template('/countries/index.html', all_countries=all_countries)

# NEW
@country_blueprint.route('/list-countries/new', methods=['GET'])
def new_country():
    return render_template('/countries/new.html')

# create
@country_blueprint.route('/list-countries', methods=['POST'])
def create_country():
    new_country = request.form['name']
    country = Country(new_country)
    country_repository.save(country)
    return redirect('/list-countries')

# SHOW
@country_blueprint.route('/list-countries/<id>', methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('/countries/show.html', country=country)


# EDIT
@country_blueprint.route('/list-countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country=country)




# UPDATE
@country_blueprint.route('/list-countries/<id>', methods=['POST'])
def update_country(id):
    name = request.form['name']
    country = Country(name, id)
    country_repository.update(country)
    return redirect('/list-countries')


# DELETE
@country_blueprint.route('/list-countries/<id>/delete', methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/list-countries')