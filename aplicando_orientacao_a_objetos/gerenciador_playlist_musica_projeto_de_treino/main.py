from musica import Musica
from playlist import Playlist


def main():
    # ============= PLAYLIST 1 ==============

    # Criando playlist1
    playlist1 = Playlist("Playlist Aerosmith")

    # Criando músicas que vao para a playlist1
    musica_aerosmith_1 = Musica(
        "toys in the attic", "aerosmith", "toys in the attic", 3.05
    )
    musica_aerosmith_2 = Musica("uncle salty", "aerosmith", "toys in the attic", 4.10)
    musica_aerosmith_3 = Musica("adam's apple", "aerosmith", "toys in the attic", 4.34)
    musica_aerosmith_4 = Musica("walk this way", "aerosmith", "toys in the attic", 3.40)
    musica_aerosmith_5 = Musica(
        "big ten inch record", "aerosmith", "toys in the attic", 2.16
    )
    musica_aerosmith_6 = Musica("sweet emotion", "aerosmith", "toys in the attic", 4.34)
    musica_aerosmith_7 = Musica(
        "no more no more", "aerosmith", "toys in the attic", 4.34
    )
    musica_aerosmith_8 = Musica(
        "round and round", "aerosmith", "toys in the attic", 5.03
    )
    musica_aerosmith_9 = Musica(
        "you see me crying", "aerosmith", "toys in the attic", 5.12
    )

    # Adicionando as músicas à playlist1
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_1)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_2)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_3)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_4)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_5)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_6)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_7)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_8)
    playlist1.adicionar_musica_na_playlist(musica_aerosmith_9)

    # Removendo uma música da playlist
    # playlist1.remover_musica_da_playlist(musica_aerosmith_1)

    # Mostrando a playlist1
    playlist1.mostrar_playlist()

    print()

    # ================ PLAYLIST 2 ==============

    # Criando a playlist2
    playlist2 = Playlist("Playlist AC/CD")

    # Criando a playlist2
    musica_acdc_1 = Musica("hells bells", "AC/DC", "back in black", 5.10)
    musica_acdc_2 = Musica("shoot to thrill", "AC/DC", "back in black", 5.17)
    musica_acdc_3 = Musica(
        "what do you do for money honey", "AC/DC", "back in black", 3.33
    )
    musica_acdc_4 = Musica("givin' the dog a bone", "AC/DC", "back in black", 3.30)
    musica_acdc_5 = Musica(
        "let me put my love into you", "AC/DC", "back in black", 4.16
    )
    musica_acdc_6 = Musica("back in black", "AC/DC", "back in black", 4.14)
    musica_acdc_7 = Musica(
        "you shook me all night long", "AC/DC", "back in black", 3.30
    )
    musica_acdc_8 = Musica("have a drink on me", "AC/DC", "back in black", 3.57)
    musica_acdc_9 = Musica("shake a leg", "AC/DC", "back in black", 4.06)
    musica_acdc_10 = Musica(
        "rock an roll ain't noise pollution", "AC/DC", "back in black", 4.15
    )

    # Adicionando músicas à playlist2
    playlist2.adicionar_musica_na_playlist(musica_acdc_1)
    playlist2.adicionar_musica_na_playlist(musica_acdc_2)
    playlist2.adicionar_musica_na_playlist(musica_acdc_3)
    playlist2.adicionar_musica_na_playlist(musica_acdc_4)
    playlist2.adicionar_musica_na_playlist(musica_acdc_5)
    playlist2.adicionar_musica_na_playlist(musica_acdc_6)
    playlist2.adicionar_musica_na_playlist(musica_acdc_7)
    playlist2.adicionar_musica_na_playlist(musica_acdc_8)
    playlist2.adicionar_musica_na_playlist(musica_acdc_9)
    playlist2.adicionar_musica_na_playlist(musica_acdc_10)

    # Mostrando a playlist2
    playlist2.mostrar_playlist()

    print()
    # ============ PLAYLIST 3 ==============

    playlist3 = Playlist("Playlist Iron Maiden")

    # Mostrando a playlist3
    playlist3.mostrar_playlist()


if __name__ == "__main__":
    main()
