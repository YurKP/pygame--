import pygame
from random import randint
import sys


# создания окна
pygame.init()
size = width, height = 930, 800
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()
    sys.exit()


# начальное окно
def start_screen():
    screen.fill('white')

    text_1 = ['Игра "Гонки против течения"', "",
              "Суть игры в том, чтобы собирать",
              "звездочки и не врезаться в ",
              "другие машины больше", "определенного количества раз.", "",
              "       В игре есть 3 уровня."]

    text_2 = ['1 уровень. Лёгкий', '', 'На этом уровне будут', 'всего 3 встречные машины.', '',
              'Можно врезаться только 1 раз']

    text_3 = ['2 уровень. Средний', '', 'Врежетесь 3 раза =>', 'проиграете']

    text_4 = ['3 уровень. Сложный', '', 'Много звездочек,', 'много встречных машин,', 'высокая скорость...',
              '', 'Врезаться можно всего ', '5 раз']

    screen.blit(game_icon, (300, 0))

    font = pygame.font.Font(None, 30)
    text_coord = 250

    for line in text_1:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 300
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    text_coord += 30

    text_coord_4 = text_coord
    text_coord_5 = text_coord
    text_coord_6 = text_coord

    for line in text_2:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord_4 += 3
        intro_rect.top = text_coord_4
        intro_rect.x = 12
        text_coord_4 += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    for line in text_3:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord_5 += 3
        intro_rect.top = text_coord_5
        intro_rect.x = 350
        text_coord_5 += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    for line in text_4:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord_6 += 3
        intro_rect.top = text_coord_6
        intro_rect.x = 650
        text_coord_6 += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    text_coord_5 += 120

    string_rendered = font.render('Чтобы начать игру, нажмите пробел', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord_5
    intro_rect.x = 270
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return

        pygame.display.flip()
        clock.tick(60)


# экран ввода имени
def screen_entry_name():
    text = ''

    screen.fill('white')

    font = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 27)
    font3 = pygame.font.Font(None, 50)

    text_coord = 200

    string_rendered = font.render('Для начала введите имя', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 320
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 15

    string_rendered = font2.render('длина = 5 символов', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 350
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    pygame.draw.rect(screen, 'black', [220, 340, 500, 100], 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(text) == 5:
                        return text
                else:
                    if len(text) < 5:
                        text += event.unicode

        pygame.draw.rect(screen, 'white', [223, 343, 494, 94])

        string = font3.render(text, 1, pygame.color.Color('black'))
        size_string = string.get_rect()
        size_string.x, size_string.y = 415, 370
        screen.blit(string, size_string)

        pygame.display.flip()
        clock.tick(60)


# экран между уровнями
def screen_between_levels():
    screen.fill('white')
    screen.blit(smile_between_levels, (320, 30))

    font = pygame.font.Font(None, 35)

    text_coord = 350

    string_rendered = font.render('Неплохо', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 405
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 50

    string_rendered = font.render('Нажмите пробел, чтобы', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 325
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 3

    string_rendered = font.render('перейти к следующему уровню', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 270
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                sp = list(d.keys())
                return sp[sp.index(ans) + 1]

        pygame.display.flip()
        clock.tick(60)


# экран проигрыша
def loss_screen():
    screen.fill('white')

    screen.blit(loss_smile, (270, 30))

    font = pygame.font.Font(None, 30)
    text_coord = 300

    string_rendered = font.render('К сожалению, Вы проиграли', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 300
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 50

    string_rendered = font.render('Для того, чтобы перезапустить уровень, нажмите пробел.',
                                  1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    text_coord += 15
    intro_rect.top = text_coord
    intro_rect.x = 200
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                return

        pygame.display.flip()
        clock.tick(60)


# победный экран
def victory_screen():
    screen.fill('white')

    screen.blit(img_of_cup, (350, 30))
    screen.blit(img_of_star, (460, 485))

    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 60)

    text_coord = 300

    string_rendered = font.render('Урраа!!! Победа!!!', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 380
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 50

    string_rendered = font.render('Для того, чтобы перезапустить игру, нажмите пробел.', 1,
                                  pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    text_coord += 15
    intro_rect.top = text_coord
    intro_rect.x = 180
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord += 100
    text_coord_2 = text_coord - 10

    string_rendered = font.render('Вы набрали', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 320
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    string_rendered = font2.render(str(count_stars), 1, pygame.Color('gold'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord_2
    intro_rect.x = 523
    text_coord_2 += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                return 'f'

        pygame.display.flip()
        clock.tick(60)


# загрузка фонов
img_background_1 = pygame.image.load("фон.png")
img_background_2 = pygame.image.load('фон для сложного уровня.png')

# загрузка других изображений
img2 = pygame.image.load('аватарка.png')
img_of_star = pygame.image.load('звезда.png')
img_of_boom = pygame.image.load('boom.png')
game_icon = pygame.image.load('иконка_игра.png')
smile_between_levels = pygame.image.load('подмигивающий смайлик.png')
loss_smile = pygame.image.load('отрицательный смайлик.png')
img_of_cup = pygame.image.load('кубок.png')

# изначальные координаты фона (по оси OY)
background_coordinates = -3960

# счетчик звездочек
count_stars = 0


# отрисовка фона для 1 и 2 уровней
def draw():
    screen.fill('white')

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 30)

    txt_number_stars = font2.render(str(cr.count_stars), True, 'gold')
    txt_number_booms = font2.render(str(cr.count_booms), True, 'red')

    txt_warning = font3.render('Осторожно!', True, 'black')
    txt_motivation = font3.render('Хорошо!', True, 'black')
    txt_super_motivation = font3.render('Круто!', True, 'black')

    txt = font3.render('Чтобы управлять машиной,', True, 'black')
    txt_2 = font3.render('нажимайте на стрелочки', True, 'black')
    txt_3 = font3.render('("<-" и "->")', True, 'black')

    screen.blit(img_background_1, (0, background_coordinates))
    screen.blit(img2, (700, 130))

    screen.blit(txt_name_users, (715, 80))

    screen.blit(txt_number_stars, (765, 312))
    screen.blit(img_of_star, (705, 315))

    screen.blit(img_of_boom, (650, 390))
    screen.blit(txt_number_booms, (775, 415))

    screen.blit(txt, (625, 610))
    screen.blit(txt_2, (625, 640))
    screen.blit(txt_3, (625, 670))

    if cr.count_booms == d[ans][3]:
        screen.blit(txt_warning, (690, 510))

    if cr.count_stars >= 5:
        if cr.count_stars >= 10:
            screen.blit(txt_super_motivation, (730, 280))
        else:
            screen.blit(txt_motivation, (720, 280))


# отрисовка 3 уровня
def draw_3():
    screen.fill('white')

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 30)

    txt_number_stars = font2.render(str(cr.count_stars), True, 'gold')
    txt_number_booms = font2.render(str(cr.count_booms), True, 'red')

    txt_warning = font3.render('Осторожно!', True, 'black')
    txt_motivation = font3.render('Хорошо!', True, 'black')
    txt_super_motivation = font3.render('Круто!', True, 'black')

    screen.blit(img_background_2, (0, background_coordinates))
    screen.blit(img2, (790, 130))
    screen.blit(txt_name_users, (805, 80))

    screen.blit(txt_number_stars, (845, 312))
    screen.blit(img_of_star, (785, 315))

    screen.blit(img_of_boom, (770, 390))
    screen.blit(txt_number_booms, (890, 415))

    if cr.count_booms == d[ans][3]:
        screen.blit(txt_warning, (790, 510))

    if cr.count_stars >= 5:
        if cr.count_stars >= 10:
            screen.blit(txt_super_motivation, (830, 280))
        else:
            screen.blit(txt_motivation, (820, 280))


# общая группа спрайтов
all_sprites = pygame.sprite.Group()

# группа других машинок
sprites_of_other_cars = pygame.sprite.Group()

# группа звездочек
sprites_of_stars = pygame.sprite.Group()

# группа взрывов
sprites_of_booms = pygame.sprite.Group()


# спрайт основная машинка
class Car(pygame.sprite.Sprite):
    # картинка машинки
    image = pygame.image.load("машинка.png")

    def __init__(self):
        super().__init__()
        self.image = Car.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # начальные координаты
        self.rect.x = 330
        self.rect.y = 550

        # счетчик для звезд
        self.count_stars = 0

        self.count_booms = 0

        # скорость
        self.speed = d[ans][6]

    def move_forward(self):
        self.rect.y -= self.speed

    def move_left(self):
        # проверка, что машинка не уехала за границы дороги
        if (self.rect.x - 7) >= d[ans][4][0]:
            self.rect.x -= 7

    def move_right(self):
        # проверка, что машинка не уехала за границы дороги
        if (self.rect.x + 7 + self.image.get_size()[0]) <= d[ans][4][1]:
            self.rect.x += 7


class OtherCars(pygame.sprite.Sprite):
    # картинка машинки
    image = pygame.image.load("другая машинка.png")

    def __init__(self, speed):
        super().__init__()
        self.image = OtherCars.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # начальные координаты
        self.rect.x = randint(d[ans][4][0], d[ans][4][1] - self.rect.w)
        self.rect.y = -self.rect.w

        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def update(self):
        if self.rect.y > 800:
            self.kill()

        if pygame.sprite.collide_mask(self, cr):
            cr.count_booms += 1
            self.kill()
            return True
        return False


class AnimatedBoom(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, speed):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

        self.speed = speed

        self.fl = True

    def move(self):
        self.rect.y += self.speed

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        if self.cur_frame == 0:
            if self.fl:
                self.image = self.frames[self.cur_frame]
                self.fl = False
        else:
            if self.fl:
                self.image = self.frames[self.cur_frame]


# спрайт звездочка
class Star(pygame.sprite.Sprite):
    image = pygame.image.load('звезда.png')

    def __init__(self, speed):
        super().__init__()
        self.image = Star.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # начальные координаты
        self.rect.x = randint(d[ans][4][0], d[ans][4][1] - self.rect.w)
        self.rect.y = -self.rect.w

        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def update(self):
        if pygame.sprite.collide_mask(self, cr):
            cr.count_stars += 1
            self.kill()


# часики
clock = pygame.time.Clock()

# словарь с необходимыми значениями для уровней
# [функция отрисовки фона, частота появления встречных машин, частота появления звездочек, количество разрешенных
#  взрывов, диапазон размещения машинок и звездочек (по оси OX), скорость движения фона, скорость движения машинки]
d = {'f': [draw, 500, 150, 1, (15, 560), 2, 4], 'g': [draw, 90, 80, 2, (15, 560), 4, 6],
     'w': [draw_3, 35, 30, 5, (10, 750), 6, 8]}

start_screen()
name_users = screen_entry_name()
txt_name_users = pygame.font.Font(None, 40).render(name_users, True, 'red')

# переменная, хранящая текущий уровень
ans = 'f'

# добавление машинки в группу спрайтов
cr = Car()
all_sprites.add(cr)

# счетчик
k = 0

# отрисовка фона
d[ans][0]()

running = True

# игровой цикл
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # проверка событий (направление движения машинки)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        cr.move_left()
    if key[pygame.K_RIGHT]:
        cr.move_right()

    if cr.rect.y < -20:
        count_stars += cr.count_stars

        if ans == 'w':
            ans = victory_screen()

            with open('имя пользователей.txt', 'r', encoding='utf-8') as file:
                lst_of_file = list()

                sp = file.readlines()

                for i in sp:
                    i = i.strip()
                    lst_of_file.append(i.split(' - '))

            cnt = 0

            for i in lst_of_file:
                if name_users in i:
                    lst_of_file[lst_of_file.index(i)][1] = str(count_stars)
                else:
                    cnt += 1

            if cnt == len(lst_of_file):
                lst_of_file.append([name_users, str(count_stars)])

            with open('имя пользователей.txt', 'w', encoding='utf-8') as file2:
                for i in lst_of_file:
                    file2.write(f'{i[0]} - {i[1]}\n')

            count_stars = 0

        else:
            ans = screen_between_levels()

        # обнуляем все результаты
        cr.count_booms = 0
        cr.count_stars = 0

        # двигаем фон обратно
        background_coordinates = -3960

        # очищаем группы спрайтов других машин, звездочек и взрывов
        for x in sprites_of_other_cars:
            x.kill()
        for y in sprites_of_booms:
            y.kill()
        for z in sprites_of_stars:
            z.kill()

        # обнуляем счетчик
        k = 0

        # двигаем машинку обратно
        cr.rect.x = 330
        cr.rect.y = 550

    # отрисовка фона
    if cr.count_booms > d[ans][3]:
        # обнуляем все результаты
        cr.count_booms = 0
        cr.count_stars = 0

        # двигаем фон обратно
        background_coordinates = -3960

        # очищаем группы спрайтов других машин, звездочек и взрывов
        for x in sprites_of_other_cars:
            x.kill()
        for y in sprites_of_booms:
            y.kill()
        for z in sprites_of_stars:
            z.kill()

        loss_screen()

        # обнуляем счетчик
        k = 0

        # двигаем машинку обратно
        cr.rect.x = 330
        cr.rect.y = 550

    else:
        d[ans][0]()

    if background_coordinates <= 0:
        # создание звездочку
        if k % d[ans][2] == 0:
            st_2 = Star(d[ans][5])
            sprites_of_stars.add(st_2)
            all_sprites.add(st_2)

        # создание встречной машинки
        if k % d[ans][1] == 0 and k != 0:
            oth_cr_2 = OtherCars(d[ans][6])
            sprites_of_other_cars.add(oth_cr_2)
            all_sprites.add(oth_cr_2)

        # перемещение фона на определенное количество (в зависимости от уровня)
        background_coordinates += d[ans][5]

    else:
        # движение машинки
        cr.move_forward()

    # движение других машинок
    for i in sprites_of_other_cars:
        i.move()
        fl = i.update()

        if fl:
            boom = AnimatedBoom(pygame.image.load("Mobile - Blocks Of Pyramid Breaker - Explosion.png"), 8,
                                3, i.rect.x, i.rect.y, d[ans][5])
            sprites_of_booms.add(boom)

    # движение звездочек
    for p in sprites_of_stars:
        if background_coordinates <= 0:
            p.move()

    # движение взрывов
    for f in sprites_of_booms:
        if background_coordinates <= 0:
            f.move()

    # обновление всех спрайтов и их отрисовка
    all_sprites.update()
    all_sprites.draw(screen)

    clock.tick(120)

    pygame.display.flip()

    # изменяем счетчик
    k += 1

pygame.quit()