countryToCapital = {'united kingdom':'london',
                    'russia':'moscow',
                    'india':'new delhi',
                    'japan':'tokyo'}
#dict comprehension
capitalToCountry = {capital:country for country, capital in countryToCapital.items()}
from pprint import pprint as pp #import to print the dict
pp(capitalToCountry)
