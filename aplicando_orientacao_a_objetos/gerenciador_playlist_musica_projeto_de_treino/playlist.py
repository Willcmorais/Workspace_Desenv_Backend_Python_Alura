from musica import Musica


class Playlist:
    def __init__(self, nome_playlist=""):
        self._nome_playlist = nome_playlist
        self._musicas = []

    def __str__(self):
        return f"{self._nome_playlist}"

    def adicionar_musica_na_playlist(self, musica):
        if not self._nome_playlist:
            return "Nenhuma playlist criada."
        else:
            self._musicas.append(musica)

    def remover_musica_da_playlist():
        pass

    def mostrar_playlist(self):
        print("=" * 10, f"{self._nome_playlist}", "=" * 10)
        if not self._musicas:
            print("A playlist está vazia!")
        else:
            for musica in self._musicas:
                print(musica)
