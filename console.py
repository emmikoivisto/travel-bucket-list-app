import pdb
from models.country import Country
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("China")
country_repository.save(country1)
country2 = Country("Japan")
country_repository.save(country2)
country3 = Country("Denmark")
country_repository.save(country3)


city1 = City("Beijing", country1, False)
city_repository.save(city1)
city2 = City("Tokyo", country2, True)
city_repository.save(city2)
city3 = City("Copenhagen", country3, True)
city_repository.save(city3)
city4 = City("Osaka", country2, True)
city_repository.save(city4)

# country_repository.delete(3)

# city_repository.select_all()
country_repository.select_all()



pdb.set_trace()