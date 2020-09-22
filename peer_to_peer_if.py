cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ').capitalize()

if city in cities:
    index_num = cities.index(city)
    print(
        f"Турист {users[index_num]['name']} возраст {users[index_num]['age']}. Посетил город {tourists[index_num]['city']}")
else:
    print("Город не найден")
