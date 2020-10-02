import pdb
from models.country import Country
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()

city1 = City("Beijing", False)
city_repository.save(city1)
city2 = City("Tokyo", True)
city_repository.save(city2)

pdb.set_trace()