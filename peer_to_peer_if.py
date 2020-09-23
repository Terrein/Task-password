cities = ['Орел','Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[1], 'city': cities[1]},
            {'user': users[0], 'city': cities[0]},
            {'user': users[2], 'city': cities[2]}]

# Введенная переменная приводится к виду членов словаря cities
city = input('Введите город: ').strip().capitalize()

if city in cities:
    for tourist in tourists:
        if tourist['city'] == city:
            print(f"Турист {tourist['user']['name']} возраст {tourist['user']['age']}. Посетил город {tourist['city']}")
        else:
            print(f"Турист {tourist['user']['name']} не посещал {city}")           
else:
    print("Город не найден")     


  # Проверяется содержится ли горд в списке
"""if city in cities:
    index_num = cities.index(city)  # определяю индеск найденого члена списка
    print(
        f"Турист {tourists[index_num]['user']['name']} возраст {tourists[index_num]['user']['age']}. Посетил город {tourists[index_num]['city']}")
else:
    print("Город не найден") 
  """