import pygame

class Musica:
    @staticmethod
    def jukebox(number):
        if number == 0:
            pygame.mixer.music.stop()
        elif number == 1:
            pygame.mixer.music.load("musica/lullabyGhostInYourPiano.mp3")
            pygame.mixer.music.play(-1)
        elif number == 2:
            pygame.mixer.music.load("musica/adventureGhostInYourPiano.mp3")
            pygame.mixer.music.play(-1)
        elif number == 3:
            pygame.mixer.music.load("musica/liebestrau.mp3")
            pygame.mixer.music.play(-1)
        elif number == 4:
            pygame.mixer.music.load("musica/Kiss_the_Sky.mp3")
            pygame.mixer.music.play(-1)
        elif number == 5:
            pygame.mixer.music.load("musica/Lullaby.mp3")
            pygame.mixer.music.play(-1)
        elif number == 6:
            pygame.mixer.music.load("musica/Gentle_Breeze.mp3")
            pygame.mixer.music.play(-1)
        elif number == 7:
            pygame.mixer.music.load("musica/Eternal_Hope.mp3")
            pygame.mixer.music.play(-1)
        elif number == 8:
            pygame.mixer.music.load("musica/Pressure.mp3")
            pygame.mixer.music.play(-1)
        elif number == 9:
            pygame.mixer.music.load("musica/01 To the Moon - Main Theme.mp3")
            pygame.mixer.music.play(-1)

    @staticmethod
    def setVolume(command):
        volumeAtual = pygame.mixer.music.get_volume()
        print(volumeAtual)
        if command == pygame.K_UP and volumeAtual < 1.0:
            pygame.mixer.music.set_volume(min(volumeAtual + 0.25, 1.0))
            print(volumeAtual)
        elif command == pygame.K_DOWN and volumeAtual > 0.0:
            pygame.mixer.music.set_volume(max(volumeAtual - 0.25, 0.0))
