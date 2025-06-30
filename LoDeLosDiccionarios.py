# ------

films = {"Love Actually" : "Richard Curtys",
"Kill Bill" : "Quentin Tarantino",
"Fargo" : "Coen Brothers"
}

print(films)
films.pop("Love Actually")
print(films)

# ------
films["Inception"] = "Christopher Nolan"
print(films)

films.popitem()
print(films)

# ------
copyDic = films.copy()
print(copyDic)

# ------

child1 = {
    "Name" : "Artorias"
}

child2 = {
    "Name" : "Orstein"
}

family = {
    "child1" : child1,
    "child2" : child2
}

print(family["child1"])