tupla = ("William", "Victoria", "Ana")
lista = ["Mário", "Sérgio", "Wilson"]

a, b, c = tupla
d, e, f = lista

print(tupla)
print(lista)
print(a, b, c)
print(d, e, f)

print()
cidade1 = ("São Paulo", -23.5505, -46.6333)
cidade2 = ("Rio de Janeiro", -22.9068, -43.1729)
cidade3 = ("Brasília", -15.701, -47.9292)

cidades = [cidade1, cidade2, cidade3]

print(cidades)
print()

for cidade in cidades:
    nome, latitude, longitude = cidade
    print(f"Cidade: {nome} | Latitude: {latitude} | Longitude: {longitude}.")
