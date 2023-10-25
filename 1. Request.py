import requests
import numpy as np


def get_salaries_and_names(city, amount_pages=1):
    salaries, names = [], []

    if amount_pages <= 0 or url(city, 0) is None:
        return salaries, names
    
    for index in range(amount_pages):
        items = requests.get(url(city, index)).json()['items']
        for item in items:
            salaries += [item['salary']]
            names += [item['name']]
    
    return salaries, names


def url(city, amount_pages):
    if city == 'Moscow':
        return f"https://api.hh.ru/vacancies?text=Аналитик&area=1&search_field=name&per_page=100&page={amount_pages}"

    if city == 'Saint-Petersburg':
        return f"https://api.hh.ru/vacancies?text=Аналитик&area=2&search_field=name&per_page=100&page={amount_pages}"

    return None


salaries_moscow, names_moscow = get_salaries_and_names('Moscow', n)
salaries_saint_petersburg, names_saint_petersburg = get_salaries_and_names('Saint-Petersburg', m)
