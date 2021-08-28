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

    def exist(self, screen, level):
        self.move(level)
        box_letter = LetterBoxes.box_font.render(self.letter, True, (0, 0, 0))
        screen.blit(self.image, (self.x, self.y))
        screen.blit(box_letter, (self.x + (self.width/3), self.y + (self.height/5)))

    def move(self, level):
        self.x += 2 * level


class GameLoop:
    window_width = 1000
    window_height = 700
    game_window = pygame.display.set_mode((window_width, window_height))
    game_run = True
    fps = pygame.time.Clock()
    pressed_letter_box = ''
    spawn_timer = 20
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_taken = []
    letters_available = []
    in_game_font = pygame.font.SysFont("monospace", 30)
    game_score = 0
    lives = 10
    current_screen = 'gameplay'
    level = 1

    @classmethod
    def screen_controller(cls):
        if cls.lives <= 0:
            cls.current_screen = 'game_over'

    @classmethod
    def game_over_screen(cls):
        game_over_font = pygame.font.SysFont("monospace", 30)
        game_over_label = game_over_font.render('GAMEOVER', True, (255, 0, 0))
        cls.game_window.blit(game_over_label, (300, 300))

    @classmethod
    def game_texts(cls):
        score_label = cls.in_game_font.render('Score: ' + str(cls.game_score), True, (255, 0, 255))
        cls.game_window.blit(score_label, (0, 0))
        life_label = cls.in_game_font.render('Lives: ' + str(cls.lives), True, (255, 0, 255))
        cls.game_window.blit(life_label, (300, 0))
        ps = cls.in_game_font.render('Level: ' + str(cls.level), True, (255, 0, 255))
        cls.game_window.blit(ps, (500, 0))

    @classmethod
    def spawn_boxes(cls):
        cls.spawn_timer -= 1
        if cls.spawn_timer <= 0:
            cls.letters_available.clear()
            for i in cls.alphabet:
                if i not in cls.letters_taken:
                    cls.letters_available.append(i)

            if len(cls.letters_available) > 0:
                chosen_letter = random.choice(cls.letters_available)
                box_monster = LetterBoxes(-50, random.randrange(50, cls.window_height-50), random.choice(chosen_letter))
                cls.letters_taken.append(chosen_letter)
                cls.spawn_timer = 30
            else:
                cls.letters_taken.clear()
                cls.spawn_timer = 300

        for i in LetterBoxes.all_boxes:
            i.exist(cls.game_window, cls.level)
            if cls.pressed_letter_box == i.letter:
                cls.game_score += 1
                LetterBoxes.all_boxes.remove(i)

            if i.x > cls.window_width:
                try:
                    cls.letters_taken.remove(i.letter)
                    LetterBoxes.all_boxes.remove(i)
                    cls.lives -= 1

                except:
                    pass

        cls.pressed_letter_box = ''

    @classmethod
    def reset_variables(cls):
        cls.lives = 10
        cls.spawn_timer = 30
        cls.game_score = 0
        cls.level = 1
        LetterBoxes.all_boxes.clear()
        cls.letters_taken.clear()
        cls.letters_available.clear()

    @classmethod
    def game_runner(cls):
        while cls.game_run:
            cls.game_window.fill((0, 0, 0))
            cls.fps.tick(60)
            cls.screen_controller()
            cls.level += 0.0001

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
                    elif event.key == pygame.K_SPACE:
                        if cls.current_screen == 'game_over':
                            cls.current_screen = 'gameplay'
                            cls.reset_variables()
                    if cls.pressed_letter_box in cls.letters_taken:
                        cls.letters_taken.remove(cls.pressed_letter_box)

            if cls.current_screen == 'game_over':
                cls.game_over_screen()
            else:
                cls.game_texts()
                cls.spawn_boxes()
            pygame.display.update()


GameLoop.game_runner()
