class Musica:
    musicas = []

    def __init__(self, nome_da_musica="", artista="", duracao=0.0):
        self.nome_da_musica = nome_da_musica
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def listar_musicas():
        print("Listagem de músicas(Nome, Artista, Duração)\n")
        for musica in Musica.musicas:
            print(f"{musica.nome_da_musica} | {musica.artista} | {musica.duracao}")


musica_reggae1 = Musica("Three Little Birds", "Bob Marley")
musica_reggae2 = Musica("Permanent Holiday", "Mike Love", 4.21)
musica_rock2 = Musica("Under Pressure", "Queen", 3.53)

Musica.listar_musicas()
