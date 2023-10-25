def get_names_max_salaries_moscow(salaries, names):
    names_max_salaries = dict()

    for salary, name in zip(salaries, names):
        if name not in names_max_salaries:
            names_max_salaries[name] = salary

        names_max_salaries[name] = max(names_max_salaries[name], salary)
    
    return names_max_salaries


def get_names_max_salaries_saint_petersburg(salaries, names):
    names_max_salaries = dict()
    for salary, name in zip(salaries, names):

        if name in names_max_salaries_moscow and names_max_salaries_moscow[name] > salary:
            continue

        if name not in names_max_salaries:
            names_max_salaries[name] = []

        names_max_salaries[name].append(salary)

    return names_max_salaries


names_max_salaries_moscow = get_names_max_salaries_moscow(salaries_moscow, names_moscow)
names_max_salaries_saint_petersburg = get_names_max_salaries_saint_petersburg(salaries_saint_petersburg, names_saint_petersburg)
