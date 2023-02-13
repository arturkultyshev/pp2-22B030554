movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def func1(film):
    for i in movies:
        if i['name'] == film:
            if i['imdb'] > 5.5:
                return True
            break
    return False


def func2():
    new_list = []
    for i in movies:
        if i['imdb'] > 5.5:
            new_list.append(i['name'])
    return new_list


def func3(category):
    new_list = []
    for i in movies:
        if i['category'] == category:
            new_list.append(i['name'])
    return new_list


def func4(arr):
    imdb = []
    for i in arr:
        for j in movies:
            if j['name'] == i:
                imdb.append(float(j['imdb']))

    return sum(imdb) / len(imdb)


def func5(category):
    imdb = []
    for j in movies:
        if j['category'] == category:
            imdb.append(float(j['imdb']))

    return sum(imdb) / len(imdb)


def func6(movies, start, end):
    for i in movies:
        if i['imdb'] > start and i['imdb'] < end:
            print(i['name'], i[])



print(func1('We Two'))
print(func2())
print(func3("Romance"))
print(func4(["We Two", "Exam"]))
print(func5('Suspense'))
