boek = {
    "Titel": "Moby Dick", "Auteur": "Herman Melville", "Jaar": 1964,
    "Jaar": 1965, "Pagina's": 1965
}

# boek["Jaar"] = 1902
boek["ISBN"] = "AYUI892938729837"
print(boek["Titel"], boek["Jaar"], boek["ISBN"])

for field in boek:
    value = boek[field]
    print(field, ":", value)
    print(field, ":", value)
    print(field, ":", value)

# for field, value in boek.items():
#   print(field + ":", value)
