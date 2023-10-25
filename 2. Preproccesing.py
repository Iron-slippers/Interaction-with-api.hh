def preproccesing_salaries(salaries, names):
    indexs_drop = []
    salaries_clean = []

    for index, salary in enumerate(salaries):
        if salary is None:
            indexs_drop.append(index)
            continue
        salaries_clean.append(get_right_salary(salary))
    
    indexs_drop.reverse()
    for index in indexs_drop:
        names.pop(index)

    return salaries_clean, names


# Salary including tax and currency
def get_right_salary(salary):
    currency_coefficient = get_currency_coefficient(salary)
    gross_coefficient = get_gross_coefficient(salary)

    salary_from = salary['from']
    salary_to = salary['to']

    if salary_from is None:
        return salary_to * currency_coefficient * gross_coefficient
    
    if salary_to is None:
        return salary_from * currency_coefficient * gross_coefficient
    
    return np.mean([salary_from, salary_to]) * currency_coefficient * gross_coefficient


# Transfer to rubles if required
def get_currency_coefficient(salary):
    if salary['currency'] == 'RUR':
        return 1
    return 100


# Tax accounting
def get_gross_coefficient(salary):
    if salary['gross']:
        return 1
    return 0.87


salaries_moscow, names_moscow = preproccesing_salaries(salaries_moscow, names_moscow)
salaries_saint_petersburg, names_saint_petersburg = preproccesing_salaries(salaries_saint_petersburg, names_saint_petersburg)
