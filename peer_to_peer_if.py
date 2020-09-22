cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

# Введенная переменная приводится к виду членов словаря cities
city = input('Введите город: ').capitalize()

# Проверяется содержится ли горд в списке
if city in cities:
    index_num = cities.index(city)  # определяю индеск найденого члена списка
    print(
        f"Турист {tourists[index_num]['user']['name']} возраст {tourists[index_num]['user']['age']}. Посетил город {tourists[index_num]['city']}")
else:
    print("Город не найден")
