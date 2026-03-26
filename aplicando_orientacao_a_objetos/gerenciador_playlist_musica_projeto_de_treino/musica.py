class Musica:
    def __init__(self, musicas, artista_banda="", album="", duracao=0.0):
        self._musicas = musicas.title()
        self._artista_banda = artista_banda.title()
        self._album = album.title()
        self._duracao = duracao

    def __str__(self):
        return f"{self._musicas} | {self._artista_banda} | {self._album} | {self._duracao} min."
