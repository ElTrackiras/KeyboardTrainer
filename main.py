import pygame
import random
pygame.init()


class LetterBoxes:
    monster_img = pygame.image.load('Assets/Monster.png')
    all_boxes = list()
    box_font = pygame.font.SysFont("monospace", 30)

    def __init__(self, x, y, letter):
        self.image = LetterBoxes.monster_img
        self.x = x
        self.y = y
        self.letter = letter
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
        LetterBoxes.all_boxes.append(self)

    def exist(self, screen):
        self.move()
        box_letter = LetterBoxes.box_font.render(self.letter, True, (0, 0, 0))
        screen.blit(self.image, (self.x, self.y))
        screen.blit(box_letter, (self.x + (self.width/3), self.y + (self.height/5)))

    def move(self):
        self.x += 2


class GameLoop:
    game_window = pygame.display.set_mode((1000, 700))
    game_run = True
    fps = pygame.time.Clock()
    pressed_letter_box = ''
    spawn_timer = 20
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    @classmethod
    def spawn_boxes(cls):
        cls.spawn_timer -= 1
        if cls.spawn_timer <= 0:
            box_monster = LetterBoxes(-20, random.randrange(0, 650), random.choice(cls.alphabet))
            cls.spawn_timer = 30

        for i in LetterBoxes.all_boxes:
            i.exist(cls.game_window)
            if cls.pressed_letter_box == i.letter:
                LetterBoxes.all_boxes.remove(i)

        cls.pressed_letter_box = ''

    @classmethod
    def game_runner(cls):
        while cls.game_run:
            cls.game_window.fill((0, 0, 0))
            cls.fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        cls.pressed_letter_box = 'q'
                    elif event.key == pygame.K_w:
                        cls.pressed_letter_box = 'w'
                    elif event.key == pygame.K_e:
                        cls.pressed_letter_box = 'e'
                    elif event.key == pygame.K_r:
                        cls.pressed_letter_box = 'r'
                    elif event.key == pygame.K_t:
                        cls.pressed_letter_box = 't'
                    elif event.key == pygame.K_y:
                        cls.pressed_letter_box = 'y'
                    elif event.key == pygame.K_u:
                        cls.pressed_letter_box = 'u'
                    elif event.key == pygame.K_i:
                        cls.pressed_letter_box = 'i'
                    elif event.key == pygame.K_o:
                        cls.pressed_letter_box = 'o'
                    elif event.key == pygame.K_p:
                        cls.pressed_letter_box = 'p'
                    elif event.key == pygame.K_a:
                        cls.pressed_letter_box = 'a'
                    elif event.key == pygame.K_s:
                        cls.pressed_letter_box = 's'
                    elif event.key == pygame.K_d:
                        cls.pressed_letter_box = 'd'
                    elif event.key == pygame.K_f:
                        cls.pressed_letter_box = 'f'
                    elif event.key == pygame.K_g:
                        cls.pressed_letter_box = 'g'
                    elif event.key == pygame.K_h:
                        cls.pressed_letter_box = 'h'
                    elif event.key == pygame.K_j:
                        cls.pressed_letter_box = 'j'
                    elif event.key == pygame.K_k:
                        cls.pressed_letter_box = 'k'
                    elif event.key == pygame.K_l:
                        cls.pressed_letter_box = 'l'
                    elif event.key == pygame.K_z:
                        cls.pressed_letter_box = 'z'
                    elif event.key == pygame.K_x:
                        cls.pressed_letter_box = 'x'
                    elif event.key == pygame.K_c:
                        cls.pressed_letter_box = 'c'
                    elif event.key == pygame.K_v:
                        cls.pressed_letter_box = 'v'
                    elif event.key == pygame.K_b:
                        cls.pressed_letter_box = 'b'
                    elif event.key == pygame.K_n:
                        cls.pressed_letter_box = 'n'
                    elif event.key == pygame.K_m:
                        cls.pressed_letter_box = 'm'

            cls.spawn_boxes()
            pygame.display.update()


GameLoop.game_runner()
