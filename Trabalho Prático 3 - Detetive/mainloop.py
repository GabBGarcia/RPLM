import pygame
import sys

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((840, 480))

pygame.display.set_caption("Detective")

icon = pygame.transform.scale(pygame.image.load('Game_spirite\\CG\\Inicial.png'), (840, 480))
icon.set_colorkey(icon.get_at((0, 0)))
win.blit(icon, (0, 0))


pygame.display.update()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def dialog(string, color):
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render(string, False, color)
    text_canvas = pygame.transform.scale(pygame.image.load(
        'Game_spirite\\Text_canvas\\Moldura.png'), (1000, 200))
    text_canvas.set_colorkey(text_canvas.get_at((0, 0)))
    win.blit(text_canvas, (-80, 300))
    win.blit(textsurface, (70, 360))


def print_on_screen(string, color, delay_time=10):
    for i in range(len(string)):
        dialog(string[:(i+1)], color)
        pygame.display.update()
        pygame.time.delay(delay_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            break


class game_map(object):
    def __init__(self, scroll_x, scroll_y, picture):
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y
        self.picture = picture

    def winblit(self, x, y):
        win.blit(self.picture, (self.scroll_x-x, self.scroll_y-y, 50, 50))


class game_player(object):
    def __init__(self, path, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.picture = []
        for i in range(4):
            toAppend = []
            for j in range(3):
                if i == 0:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\nave.png').convert(), (300, 250)))
                elif i == 1:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\nave.png').convert(), (300, 250)))
                elif i == 2:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\nave.png').convert(), (300, 250)))
                elif i == 3:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\nave.png').convert(), (300, 250)))
            self.picture.append(toAppend)
        for i in range(4):
            for j in range(3):
                self.picture[i][j].set_colorkey(
                    self.picture[i][j].get_at((0, 0)))
        self.step_costume = [1, 0]

    def winblit(self):
        win.blit(self.picture[self.step_costume[0]]
                 [self.step_costume[1]], (250, 100, 50, 50))


class game_player2(object):
    def __init__(self, path, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.picture = []
        for i in range(4):
            toAppend = []
            for j in range(3):
                if i == 0:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\dentronave.jpg').convert(), (840, 480)))
                elif i == 1:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\dentronave.jpg').convert(), (840, 480)))
                elif i == 2:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\dentronave.jpg').convert(), (840, 480)))
                elif i == 3:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\dentronave.jpg').convert(), (840, 480)))
            self.picture.append(toAppend)
        for i in range(4):
            for j in range(3):
                self.picture[i][j].set_colorkey(
                    self.picture[i][j].get_at((0, 0)))
        self.step_costume = [1, 0]

    def winblit(self):
        win.blit(self.picture[self.step_costume[0]]
                 [self.step_costume[1]], (0, 0, 50, 50))


class game_player3(object):
    def __init__(self, path, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.picture = []
        for i in range(4):
            toAppend = []
            for j in range(3):
                if i == 0:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\naveterra.jpg').convert(), (840, 480)))
                elif i == 1:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\naveterra.jpg').convert(), (840, 480)))
                elif i == 2:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\naveterra.jpg').convert(), (840, 480)))
                elif i == 3:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\naveterra.jpg').convert(), (840, 480)))
            self.picture.append(toAppend)
        for i in range(4):
            for j in range(3):
                self.picture[i][j].set_colorkey(
                    self.picture[i][j].get_at((0, 0)))
        self.step_costume = [1, 0]

    def winblit(self):
        win.blit(self.picture[self.step_costume[0]]
                 [self.step_costume[1]], (0, 0, 50, 50))


class game_player4(object):
    def __init__(self, path, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.picture = []
        for i in range(4):
            toAppend = []
            for j in range(3):
                if i == 0:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\pergunta.png').convert(), (840, 480)))
                elif i == 1:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\pergunta.png').convert(), (840, 480)))
                elif i == 2:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\pergunta.png').convert(), (840, 480)))
                elif i == 3:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\pergunta.png').convert(), (840, 480)))
            self.picture.append(toAppend)
        for i in range(4):
            for j in range(3):
                self.picture[i][j].set_colorkey(
                    self.picture[i][j].get_at((0, 0)))
        self.step_costume = [1, 0]

    def winblit(self):
        win.blit(self.picture[self.step_costume[0]]
                 [self.step_costume[1]], (0, 0, 50, 50))


class game_player5(object):
    def __init__(self, path, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.picture = []
        for i in range(4):
            toAppend = []
            for j in range(3):
                if i == 0:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\espaço.png').convert(), (840, 480)))
                elif i == 1:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\espaço.png').convert(), (840, 480)))
                elif i == 2:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\espaço.png').convert(), (840, 480)))
                elif i == 3:
                    toAppend.append(pygame.transform.scale(pygame.image.load(
                        'Game_spirite\\Spirite\\espaço.png').convert(), (840, 480)))
            self.picture.append(toAppend)
        for i in range(4):
            for j in range(3):
                self.picture[i][j].set_colorkey(
                    self.picture[i][j].get_at((0, 0)))
        self.step_costume = [1, 0]

    def winblit(self):
        win.blit(self.picture[self.step_costume[0]]
                 [self.step_costume[1]], (0, 0, 50, 50))


maps_full = []
maps = []

for i in range(0, 4):
    toAppend = []
    for j in range(0, 4):
        toAppend.append(game_map(j*500, i*500, pygame.transform.scale(
            pygame.image.load('Game_spirite\\CG\\espaço.png').convert(), (840, 480))))
    maps.append(toAppend)

maps_full.append(maps)

maps = pygame.transform.scale(pygame.image.load(
    'Game_spirite\\Map\\espaço.png').convert(), (300, 750))
maps.set_colorkey(maps.get_at((0, 0)))
maps = game_map(0, 0, maps)

maps_full.append(maps)

spirite = game_player('Game_spirite\\CG\\espaço.png', 840, 480, 0)
spirite2 = game_player2('Game_spirite\\CG\\dentronave.jpg', 840, 480, 0)
spirite3 = game_player3('Game_spirite\\CG\\naveterra.jpg', 840, 480, 0)
spirite4 = game_player4('Game_spirite\\CG\\pergunta.png', 840, 480, 0)
spirite5 = game_player5('Game_spirite\\CG\\espaço.png', 840, 480, 0)

pygame.mixer.music.load('Game_music\\song18.mp3')
pygame.mixer.music.play(-1)

plot = 1

delay_time = 100

maps = maps_full[0]

while True:
    if plot == 1:
        talk = ["Você está em uma nave espacial com uma tripulação de 10 integrantes",
                "rumo ao planeta Party para o evento Fantasy... "
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite.x, spirite.y)

            spirite.winblit()

            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

        plot = 2

    elif plot == 2:
        talk = ["Quando a nave começa a apresentar problemas..."]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite2.x, spirite2.y)

            spirite2.winblit()

            if i == 0:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()
            plot = 3

    elif plot == 3:
        talk = ["A tripulação se vê obrigada a pousar no planeta Terra",
                "para realizar um reparo na nave."
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite3.x, spirite3.y)

            spirite3.winblit()
            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

            plot = 4

    elif plot == 4:
        talk = ["...",
                "Em meio a confusão ninguém notou o desaparecimento",
                " repentino de dois tripulantes. "
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

            plot = 5

    elif plot == 5:
        talk = ["Ao término do reparo todos voltam para a nave",
                "dando continuidade a viagem...",
                "Durante o embarque, dois humanos se infiltram na nave",
                "Fazendo com que ninguém perceba que dois companheiros desapareceram...",
                "Todos dão continuidade em suas tarefas na nave!"
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite.x, spirite.y)

            spirite.winblit()

            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()
            plot = 6

    elif plot == 6:
        talk = ["Quando você, ao entrar na elétrica",
                "se depara com o corpo de um de seus companheiros",
                "...",
                "CHEWBACCA está morto!"
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))
            spirite5.winblit()

            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

            plot = 7

    elif plot == 7:
        talk = ["Então você aciona o botão de emergência ",
                "para relatar o ocorrido",
                "...",
                "Os tripulantes tentam se justificar",
                "dizendo onde estavam e o que estavam fazendo..."
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))
            spirite5.winblit()

            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

        plot = 8

    elif plot == 8:
        win.fill((0, 0, 0))
        spirite4.winblit()
        pygame.display.update()
        pygame.time.delay(delay_time*30)

        plot = 9

    elif plot == 9:
        pygame.mixer.music.load('Game_music\\gambit.mp3')
        pygame.mixer.music.play(-1)

        win.fill((0, 0, 0))
        for i in range(len(talk)):
            pygame.time.delay(delay_time)
            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite.x, spirite.y)
                    spirite.winblit()

        pygame.display.update()

        pygame.time.delay(delay_time*30)
        talk = ["Sua jornada começa agora!"
                ]

        for i in range(len(talk)):
            pygame.time.delay(delay_time)

            win.fill((0, 0, 0))

            for j in range(0, 4):
                for k in range(0, 4):
                    maps[j][k].winblit(spirite5.x, spirite5.y)

            spirite5.winblit()
            if i == 0:
                print_on_screen(talk[i], WHITE)
            else:
                print_on_screen(talk[i], WHITE)

            pygame.display.update()

            plot = 10

    elif plot == 10:
        win.fill((0, 0, 0))
        spirite5.winblit()
        font = pygame.font.SysFont('Times New Roman', 17)
        font_2 = pygame.font.SysFont('Comic Sans MS', 15)
        textsurface_intro = font.render(
            'ESSAS FORAM AS DECLARAÇÕES DADAS PELOS TRIPULANTES:', False, RED)
        textsurface_one = font.render(
            'Chewbacca foi encontrado morto na elétrica.', False, WHITE)
        textsurface_two = font.render(
            'Tobi estava na administração comprando bebidas ou Darth Vader é cúmplice;', False, WHITE)
        textsurface_three = font.render(
            'Se Tobi não estava na administração comprando bebidas, então Venom não é um dos assassinos de Chewbacca;', False, WHITE)
        textsurface_four = font.render(
            'Inosuk estava na sala do café limpando mesa ou Iron-man estava na administração fazendo checagem de exame;', False, WHITE)
        textsurface_five = font.render(
            'Se Spider-Man estava na sala de controle observando as câmeras, então Sonic estava na sala do café limpando mesa;', False, WHITE)
        textsurface_version = font_2.render(
            'Press "a" para novas pistas...', False, GREEN)
        win.blit(textsurface_intro, (15, 50))
        win.blit(textsurface_one, (15, 100))
        win.blit(textsurface_two, (15, 150))
        win.blit(textsurface_three, (15, 200))
        win.blit(textsurface_four, (15, 250))
        win.blit(textsurface_five, (15, 300))
        win.blit(textsurface_version, (65, 450))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if not(key[pygame.K_a]):
                break

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if key[pygame.K_a]:
                break
        plot = 11
    elif plot == 11:
        win.fill((0, 0, 0))
        spirite5.winblit()
        textsurface_intro = font.render(
            'ESSAS FORAM AS DECLARAÇÕES DADAS PELOS TRIPULANTES:', False, RED)
        textsurface_six = font.render(
            'Se Iron-Man estava na administração passando o cartão, então Sonic encontrou o corpo no salão principal;', False, WHITE)
        textsurface_seven = font.render(
            'Se Inosuk estava na sala do café limpando mesa, então Totoro é o assasino do Chewbacca;', False, WHITE)
        textsurface_eight = font.render(
            'Se Iron-Man estava na administração passando o cartão, então Venom é um dos assassinos de Chewbacca;', False, WHITE)
        textsurface_nine = font.render(
            'Se Spider-Man estava na sala de controle observando as câmeras, então Inosuk estava na sala do café limpando mesa;', False, WHITE)
        textsurface_ten = font.render(
            'Se Inosuk estava na sala do café limpando mesa, então Sem Rosto matou Chewbacca;', False, WHITE)
        textsurface_eleven = font.render(
            'Inosuk não estava na sala do café limpando mesa ou Sonic estava na sala do café limpando mesa;', False, WHITE)
        textsurface_version2 = font_2.render(
            'Press "a" para ver todas as pistas...', False, GREEN)
        win.blit(textsurface_intro, (20, 50))
        win.blit(textsurface_six, (15, 100))
        win.blit(textsurface_seven, (15, 150))
        win.blit(textsurface_eight, (15, 200))
        win.blit(textsurface_nine, (15, 250))
        win.blit(textsurface_ten, (15, 300))
        win.blit(textsurface_eleven, (15, 350))
        win.blit(textsurface_version2, (65, 450))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if not(key[pygame.K_a]):
                break

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if key[pygame.K_a]:
                break
        plot = 12
    elif plot == 12:
        win.fill((0, 0, 0))
        spirite5.winblit()
        textsurface_intro = font.render(
            'ESSAS FORAM AS DECLARAÇÕES DADAS PELOS TRIPULANTES:', False, RED)
        textsurface_one = font.render(
            'Chewbacca foi encontrado morto na elétrica.', False, WHITE)
        textsurface_two = font.render(
            'Tobi estava na administração comprando bebidas ou Darth Vader é cúmplice;', False, WHITE)
        textsurface_three = font.render(
            'Se Tobi não estava na administração comprando bebidas, então Venom não é um dos assassinos de Chewbacca;', False, WHITE)
        textsurface_four = font.render(
            'Inosuk estava na sala do café limpando mesa ou Iron-man estava na administração fazendo checagem de exame;', False, WHITE)
        textsurface_five = font.render(
            'Se Spider-Man estava na sala de controle observando as câmeras, então Sonic estava na sala do café limpando mesa;', False, WHITE)
        textsurface_six = font.render(
            'Se Iron-Man estava na administração passando o cartão, então Sonic encontrou o corpo no salão principal;', False, WHITE)
        textsurface_seven = font.render(
            'Se Inosuk estava na sala do café limpando mesa, então Totoro é o assasino do Chewbacca;', False, WHITE)
        textsurface_eight = font.render(
            'Se Iron-Man estava na administração passando o cartão, então Venom é um dos assassinos de Chewbacca;', False, WHITE)
        textsurface_nine = font.render(
            'Se Spider-Man estava na sala de controle observando as câmeras, então Inosuk estava na sala do café limpando mesa;', False, WHITE)
        textsurface_ten = font.render(
            'Se Inosuk estava na sala do café limpando mesa, então Sem Rosto matou Chewbacca;', False, WHITE)
        textsurface_eleven = font.render(
            'Inosuk não estava na sala do café limpando mesa ou Sonic estava na sala do café limpando mesa;', False, WHITE)
        textsurface_version2 = font_2.render(
            'Press "s" para saber quem são os assassinos...', False, GREEN)
        win.blit(textsurface_intro, (20, 30))
        win.blit(textsurface_one, (15, 60))
        win.blit(textsurface_two, (15, 90))
        win.blit(textsurface_three, (15, 120))
        win.blit(textsurface_four, (15, 150))
        win.blit(textsurface_five, (15, 180))
        win.blit(textsurface_six, (15, 210))
        win.blit(textsurface_seven, (15, 240))
        win.blit(textsurface_eight, (15, 270))
        win.blit(textsurface_nine, (15, 300))
        win.blit(textsurface_ten, (15, 330))
        win.blit(textsurface_eleven, (15, 360))
        win.blit(textsurface_version2, (65, 450))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if not(key[pygame.K_s]):
                break

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if key[pygame.K_s]:
                break
        plot = 13

    elif plot == 13:
        win.fill((0, 0, 0))
        spirite5.winblit()
        font_3 = pygame.font.SysFont('Comic Sans MS', 28)
        textsurface_result = font_3.render(
            'Darth Vader é cúmplice e Totoro é o assassino de Chewbacca', False, RED)
        textsurface_version2 = font_2.render(
            'Press ESC para sair...', False, GREEN)

        win.blit(textsurface_result, (20, 200))
        win.blit(textsurface_version2, (65, 450))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if not(key[pygame.K_ESCAPE]):
                break

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = pygame.key.get_pressed()

            if key[pygame.K_ESCAPE]:
                break
        plot = 14

    elif plot == 14:
        break

pygame.quit()
