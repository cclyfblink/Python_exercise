import pandas as pd

def get_contents_of_file(continent_name):
    try:
        file = pd.read_csv(continent_name + ".csv")
        return file
    except Exception as e:
        print(f"Error: {e}")

def get_country_dict(country_list):
    country_dict = {}
    # loop over each row in the DataFrame
    for _, row in country_list.iterrows():
        country = row[0]
        city = row[1]
        country_dict[country] = city
    return country_dict

def print_results(continent_name, countries):
    print(continent_name)
    print("-" * len(continent_name))
    for country, city in countries.items():
        print(f"{country} ({city})")

# choose continent to show data for
continent_name = "Oceania"

# get text from file for given continent name
country_list = get_contents_of_file(continent_name)

# from this extract a dictionary with each country and its city
countries = get_country_dict(country_list)

# list them out
print_results(continent_name, countries)

