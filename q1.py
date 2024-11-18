
info_dict = {"name": "Israel",
             "birth": 1948,
             "capital": "Jerusalem",
             "population_millions": 9.3,
             "language": "Hebrew",
             "cities":["Jerusalem",'Tel Aviv' 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
             "currency": "ILS",
             "area_Kilometer": 22_145,
              "gdp_billion": 450}
print(info_dict)

print("isreal info:",  info_dict.get("capital"))

print('keys', list(info_dict.keys()))

print('value', list(info_dict.values()))

print(info_dict.items())
print('from items:', dict(info_dict.items()))

info_dict_dup = info_dict.copy()

gdp_billion = info_dict_dup.pop("gdp_billion")
print("after pop:", info_dict_dup)

keys = ['name', 'birth', 'population_millions', 'capital', 'language', 'cities', 'currency', 'area_Kilometer', 'gdp_billion']
new_dict = dict.fromkeys(keys, None)

new_dict['name'] = input("Enter the country name: ")
new_dict['birth'] = int(input("Enter the year of establishment: "))
new_dict['population_millions'] = float(input("Enter the population in millions: "))
new_dict['capital'] = input("Enter the capital city: ")
new_dict['language'] = input("Enter the official language: ")
new_dict['cities'] = [
    input("Enter city 1: "),
    input("Enter city 2: "),
    input("Enter city 3: ")
]
new_dict['currency'] = input("Enter the currency: ")
new_dict['area_Kilometer'] = float(input("Enter the area in square kilometers: "))
new_dict['gdp_billion'] = float(input("Enter the GDP in billions: "))

print("The updated dictionary:")
print(new_dict)