class Musica:
    nome = ""
    artista = ""
    duracao = 00.00


musica_sertanejo1 = Musica()
musica_sertanejo1.nome = "Choram as Rosas"
musica_sertanejo1.artista = "Bruno e Marrone"
musica_sertanejo1.duracao = 3.23
print(vars(musica_sertanejo1))
print(
    f"Banda: {musica_sertanejo1.nome} - Artista: {musica_sertanejo1.artista} - Duração: {musica_sertanejo1.duracao}"
)

print()

# No caso abaixo como não instanciamos o nome da banda ele vai ter como padrão uma string vazia.
musica_rock1 = Musica()
musica_rock1.artista = "Evanescence"
musica_rock1.duracao = 3.45
print(vars(musica_rock1))
print(
    f"Banda: {musica_rock1.nome} - Artista: {musica_rock1.artista} - Duração: {musica_rock1.duracao}"
)
