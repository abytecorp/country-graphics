import re

def get_population(country_dict):
    population_dict = {}
    pattern = re.compile(r'(\d{4}) Population')

    for key in country_dict:
        match = pattern.match(key)
        if match:
            year = match.group(1)
            population_dict[year] = int(country_dict[key])
    keys = population_dict.keys()
    values = population_dict.values()
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item:item['Country'] == country, data))
    return result
