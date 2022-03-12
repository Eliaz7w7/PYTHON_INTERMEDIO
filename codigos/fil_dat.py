DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # FILTER Y MAP
    # USAN PYTHON
    print("Usan python")
    leng_py = list(filter(lambda x: x["language"] == "python", DATA))
    leng_py = list(map(lambda x: x["name"], leng_py))
    print(leng_py)
    print()

    # TRABAJAN PLATZI
    print("Trabajadores de Platzi")
    trab_plat = list(filter(lambda x: x["organization"] == "Platzi", DATA))
    trab_plat = list(map(lambda x: x["name"], trab_plat))
    print(trab_plat)
    print()

    # LIST COMPREHENSION
    # OLD PEOPLE
    print("Adultos mayores de 70")
    oldPe = [x | {"old": x["age"] >= 70} for x in DATA]
    oldPe = [x["name"] for x in oldPe if x["old"] == True]
    print(oldPe)
    print()

    # ADULTS
    print("Mayores de 18")
    ad = [x["name"] for x in DATA if x["age"] >= 18]
    print(ad)
    print()


if __name__ == "__main__":
    run()
