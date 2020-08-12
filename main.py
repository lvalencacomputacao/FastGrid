import pygame, random
from button import Button
from musica import Musica
from logic import Logic
from pygame.locals import *

pygame.init()


#setting basic info
screen = pygame.display.set_mode((1366, 768))
dimensions = pygame.display.get_surface().get_size()
horizontal = dimensions[0]
vertical = dimensions[1]
print(horizontal, vertical)
pygame.display.set_caption("FastGrid: Mental Math Training")

#resources loading
bgMenu = pygame.image.load("background/menu.png")
bgMenu = pygame.transform.scale(bgMenu, (horizontal, vertical - 30))
bgStart = pygame.image.load("background/play.png")
bgStart = pygame.transform.scale(bgStart, (horizontal, vertical - 30))
pygame.mixer.init()
pygame.mixer.music.load("musica/Pressure.mp3")
pygame.mixer.music.play(-1)

# Font loading
font = pygame.font.Font("FreeSansBold.ttf", 75)

# Creating menu buttons using class "Button"
buttonStart = Button(399, 178, 534, 90)
buttonTutorial = Button(399, 320, 530, 90)
buttonOptions = Button(399, 462, 530, 90)
buttonCredits = Button(399, 605, 530, 90)

# Creating start buttons using class "Button"
buttonSomar = Button(1177, 316, 113, 89)
buttonSubtrair = Button(1177, 423, 113, 89)
buttonMultiplicar = Button(1177, 520, 113, 89)
buttonDividir = Button(1177, 618, 113, 89)
buttonLevelUpOn = Button(50, 508, 155, 46)
buttonLevelUpOff = Button(50, 554, 155, 46)

# Cria objeto para ser usado na lógica do jogo
logicNow = Logic()

#FSMControl
running = 1
menu = 1
start = 0
tutorial = 0
options = 0
credits = 0

#Lógica adicional para o start
gerar = True
a = 0
b = 0
userString = ""
showAnswer = 0
correctAnswer = 0
op = "somar"

def userInput(digit):
    global userString
    if pygame.K_0 <= digit <= pygame.K_9:
        userString += event.unicode
        print(userString)
    elif digit == pygame.K_MINUS or digit == pygame.K_BACKSPACE:
        userString = userString[:len(userString) - 1]
        print(userString)

def drawUserInput(userString):
    userNumber = font.render(userString, True, (0, 0, 0))
    number_rect = userNumber.get_rect()
    number_rect.center = (925 - len(userString) * 21, 550)

    screen.blit(userNumber, number_rect)

def showResult(isCorrect):
    t = font.render("Wrong", True, (255, 0, 0))
    if isCorrect:
        t = font.render("Correct!!", True, (0, 255, 0))
    t_rect = t.get_rect()
    t_rect.center = (670, 390)
    screen.blit(t, t_rect)

def drawNumbers(a, b, op):

    symbolMap = {"somar": "+", "subtrair": "-", "multiplicar": "*", "dividir": "/"}

    textoA = font.render(str(a), True, (255, 255, 255))
    texto_rectA = textoA.get_rect()
    texto_rectA.center = (300, 150)
    screen.blit(textoA, texto_rectA)

    textoOP = font.render(symbolMap[op], True, (255, 255, 255))
    texto_rectOP = textoOP.get_rect()
    texto_rectOP.center = (650, 150)
    screen.blit(textoOP, texto_rectOP)

    textoB = font.render(str(b), True, (255, 255, 255))
    texto_rectB = textoB.get_rect()
    texto_rectB.center = (1075 - len(str(b)) * 20, 150)
    screen.blit(textoB, texto_rectB)

while running:
    while menu:
        pygame.display.flip()
        screen.blit(bgMenu, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = 0
                menu = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                start = 1
                menu = 0
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(x, y)

                if buttonStart.isOn(x, y):
                    #click.play()
                    #click.stop()

                    print(x, y)
                    menu = 0
                    start = 1

                elif buttonTutorial.isOn(x, y):
                    print(x, y)
                    print('tutorial')
                    menu = 0
                    start = 1

                elif buttonOptions.isOn(x, y):
                    print(x, y)
                    print('Options')
                    menu = 0
                    start = 1

                elif buttonCredits.isOn(x, y):
                    print(x, y)
                    print('Credits')
                    menu = 0
                    start = 1
            if event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    number = int(event.unicode)
                    Musica.jukebox(number)
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    print("hey")
                    Musica.setVolume(event.key)

    while start:
        pygame.display.flip()

        if gerar:
            a, b = logicNow.pairGenerator(op)
            print(a, b)
            gerar = 0

        screen.blit(bgStart, (0, 0))
        drawNumbers(a, b, op)
        drawUserInput(userString)

        if showAnswer:
            showResult(correctAnswer)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                start = 0
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_m):
                menu = 1
                start = 0
            if event.type == pygame.KEYDOWN:
                print('alo')
                if pygame.K_0 <= event.key <= pygame.K_9 or event.key == pygame.K_MINUS or event.key == pygame.K_BACKSPACE:
                    print('h')
                    userInput(event.key)
                elif (event.key == pygame.K_SPACE or pygame.K_KP_ENTER) and userString:
                    isCorrect = logicNow.solve(a, b, int(userString), op)
                    gerar = 1
                    userString = ""
                    showAnswer = 1
                    if isCorrect:
                        print("Correct")
                        correctAnswer = 1
                    else:
                        print("Incorrect")
                        correctAnswer = 0
                    if logicNow.correct != 0 and logicNow.correct % 10 == 0 and logicNow.levelUp:
                        print("incrementing")
                        logicNow.incrementModifier()
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    logicNow.manualDifficulty(event.key)

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(x, y)

                if buttonSomar.isOn(x, y):
                    op = "somar"
                    print("somar")
                    gerar = 1
                elif buttonSubtrair.isOn(x, y):
                    op = "subtrair"
                    print("subtrair")
                    gerar = 1
                elif buttonMultiplicar.isOn(x, y):
                    op = "multiplicar"
                    print("multiplicar")
                    gerar = 1
                elif buttonDividir.isOn(x, y):
                    op = "dividir"
                    print("dividir")
                    gerar = 1
                if buttonLevelUpOn.isOn(x, y):
                    logicNow.levelUp = True
                    print("Level Up On")
                if buttonLevelUpOff.isOn(x, y):
                    logicNow.levelUp = False
                    print("Level Up False")

pygame.quit()