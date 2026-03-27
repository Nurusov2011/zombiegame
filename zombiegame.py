import pygame
from random import randint
import math
pygame.init()
def get_center_mouse(mouse_pos):
    return (mouse_pos[0] - target_surf.get_width() // 2, mouse_pos[1] - target_surf.get_height() // 2)

def player_animation():
    global player_index, player_surf
    player_index += 0.2
    if player_index >= len(player_walk):
        player_index = 0
    player_surf = player_walk[int(player_index)]

def player_rotate():
    mouse_pos = pygame.mouse.get_pos()
    rel_x = mouse_pos[0] - player_rect.centerx
    rel_y = mouse_pos[1] - player_rect.centery
    angle = -math.degrees(math.atan2(rel_y, rel_x)) - 90
    rotated_surf = pygame.transform.rotate(player_surf, int(angle))
    rotated_rect = rotated_surf.get_rect(center=player_rect.center)
    screen.blit(rotated_surf, rotated_rect)

def check_collisions():
    global score, score_text
    for bullet in bullets[:]:
        if zombie_rect.colliderect(bullet.rect):
            zombie_killed()
            bullets.remove(bullet) 
            score += 1
            score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            return
        
def zombie_killed():
    global zombie_x, zombie_y, zombie_speed
    print("Zombi vuruldu!")
    zombie_x = randint(0, BOUNDS_X - zombie_rect.width)
    zombie_y = randint(-100, -40) 
    zombie_speed += 1
    zombie_rect.topleft = (zombie_x, zombie_y)

def zombie_rotate():
    mx, my = player_rect.center
    zx, zy = zombie_rect.center
    dx = mx - zx
    dy = my - zy
    angle = math.degrees(math.atan2(-dy, dx))
    rotated_surf = pygame.transform.rotate(zombie_surf, angle)
    rotated_rect = rotated_surf.get_rect(center=(zx, zy))
    screen.blit(rotated_surf, rotated_rect)

def zombie_move():
    global zombie_x, zombie_y
    zombie_vec = pygame.math.Vector2(zombie_rect.center)
    player_vec = pygame.math.Vector2(player_rect.center)
    direction = player_vec - zombie_vec
    distance = direction.length()
    
    if distance > zombie_speed:
        direction = direction.normalize() * zombie_speed
        zombie_x += direction.x
        zombie_y += direction.y
    else:
        zombie_x, zombie_y = player_rect.topleft

    zombie_rect.topleft = (zombie_x, zombie_y)

class Bullet:
    def __init__(self, x, y, target_pos):
        self.pos = pygame.Vector2(x, y)
        self.speed = 20 
        mouse_x, mouse_y = target_pos
        direction = pygame.Vector2(mouse_x, mouse_y) - self.pos
        
        if direction.length() > 0:
            self.velocity = direction.normalize() * self.speed
        else:
            self.velocity = pygame.Vector2(0, 0)

        self.rect = bullet_surf.get_rect(center=(x, y))

    def update(self):
        self.pos += self.velocity
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def blit(self, surface):
        surface.blit(bullet_surf, self.rect)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 255)) 
clock = pygame.time.Clock()
ground_surf = pygame.image.load("ground.png").convert()
player_walk1 = pygame.image.load("player.png").convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, (96, 152))
player_walk2 = pygame.image.load("player2.png").convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, (96, 152))
player_walk3 = pygame.image.load("player3.png").convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, (96, 152))
player_walk4 = pygame.image.load("player4.png").convert_alpha()
player_walk4 = pygame.transform.scale(player_walk4, (96, 152))
player_walk5 = pygame.image.load("player5.png").convert_alpha()
player_walk5 = pygame.transform.scale(player_walk5, (96, 152))
player_shoot = pygame.image.load("playershoot.png").convert_alpha()
player_shoot = pygame.transform.scale(player_shoot, (96,152))
player_walk = [player_walk1,player_walk2,player_walk3,player_walk4,player_walk5]
player_index = 0
player_surf = player_walk[player_index]
player_surf = pygame.transform.scale(player_surf, (96, 152))
player_rect = player_surf.get_rect()
player_rect.x = 600
player_rect.y = 400
player_speed = 5
BOUNDS_X = screen.get_width()
BOUNDS_Y = screen.get_height()
mouse_pos = pygame.mouse.get_pos()
target_surf = pygame.image.load("crosshair.png").convert_alpha()
target_surf = pygame.transform.scale(target_surf, (32, 32))
target_pos = get_center_mouse(mouse_pos)
zombie_surf = pygame.image.load("zombie_01\\idle\\idle0000.png").convert_alpha()
zombie_rect = zombie_surf.get_rect()
zombie_x = randint(0, BOUNDS_X - zombie_rect.width)
zombie_y = 50
zombie_speed = 10
zombies = 1
bullet_surf = pygame.image.load("bullet.png").convert_alpha()
bullet_surf = pygame.transform.scale(bullet_surf, (8, 8))
bullet_rect = bullet_surf.get_rect()
bullets = []
wait_time = 100
score = 0
score_font = pygame.font.SysFont(None, 36)
score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
health_bar_back = pygame.Surface((200, 20))
health_bar_back.fill((255, 0, 0))
health_bar_back_rect = health_bar_back.get_rect(topleft=(10, 50))
health_bar_scale_x = 200
health_bar_front = pygame.Surface((health_bar_scale_x, 20))
health_bar_front.fill((0, 255, 0))
health_bar_front_rect = health_bar_front.get_rect(topleft=(10, 50))
shoot_sound = pygame.mixer.Sound("shootsound.mp3")
colliding = False
Game_Active = False
is_shooting = False
shoot_duration = 500
last_shoot_time = 0

while True:
    if Game_Active:
        current_time = pygame.time.get_ticks()
        screen.fill((0, 0, 255))       
        screen.blit(ground_surf, (0, 0))
        wait_time -= 1 
        if wait_time <= 0:
                zombie_rotate()
                zombie_move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit() 
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_shooting = True
                last_shoot_time = current_time
                bullets.append(Bullet(player_rect.centerx, player_rect.centery, pygame.mouse.get_pos()))
                shoot_sound.play()


        screen.blit(target_surf, (target_pos))

        if is_shooting:
            if current_time - last_shoot_time > shoot_duration:
                is_shooting = False
        
        if is_shooting:
            player_surf = player_shoot
        else:
            player_surf = player_walk[int(player_index)]

        for b in bullets:
            b.update()
            b.blit(screen)

        if pygame.key.get_pressed()[pygame.K_w]:
            player_rect.y -= player_speed
            if player_rect.y < 0:
                player_rect.y = 0
            player_animation()
        if pygame.key.get_pressed()[pygame.K_s]:
            player_rect.y += player_speed
            if player_rect.y > BOUNDS_Y - player_rect.height:
                player_rect.y = BOUNDS_Y - player_rect.height
            player_animation()
        if pygame.key.get_pressed()[pygame.K_a]:
            player_rect.x -= player_speed
            if player_rect.x < 0:
                player_rect.x = 0
            player_animation()
        if pygame.key.get_pressed()[pygame.K_d]:
            player_rect.x += player_speed 
            if player_rect.x > BOUNDS_X - player_rect.width:
                player_rect.x = BOUNDS_X - player_rect.width
            player_animation()
        
        if zombie_rect.colliderect(player_rect):
            colliding = True

        while colliding:
            health_bar_scale_x -= 1
            if health_bar_scale_x <= 0:
                Game_Active = False
                health_bar_scale_x = 200
                zombie_killed()
            else:   
                health_bar_front = pygame.Surface((health_bar_scale_x, 20))
                health_bar_front.fill((0, 255, 0))
            colliding = False

        screen.blit(score_text, (10, 10))
        screen.blit(health_bar_back, health_bar_back_rect)
        screen.blit(health_bar_front, health_bar_front_rect)
        check_collisions()

        pygame.mouse.set_visible(False)
        target_pos = get_center_mouse(pygame.mouse.get_pos())
        player_rotate()
    else:
        screen.blit(ground_surf, (0, 0)) 
        Exit_font = pygame.font.SysFont(None, 36)
        Exit_text = Exit_font.render("Press Esc to Exit", True, (255,255,255))
        screen.blit(Exit_text,(10,10))
        Start_text_scale = 72
        Start_font = pygame.font.SysFont(None, Start_text_scale)
        Start_text = Start_font.render("Press SPACE to Start", True, (255, 255, 255))
        screen.blit(Start_text, (BOUNDS_X // 2 - Start_text.get_width() // 2, BOUNDS_Y // 2 - Start_text.get_height() // 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    Game_Active = True
    pygame.display.update()
    clock.tick(60)