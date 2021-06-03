import pygame, sys

def animation():
    global ball_speed_X,ball_speed_Y
    ball.x += ball_speed_X
    ball.y += ball_speed_Y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_Y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_X *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_X *= -1

pygame.init()
clock = pygame.time.Clock()

#fenster erstellen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PONG the Game')

#objekte erstellen
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 -70,10,140)
opponent = pygame.Rect(10, screen_height/2 -70,10,140)

color = pygame.Color('grey12')
grau = (200,200,200)

ball_speed_X = 7
ball_speed_Y = 7
player_speed = 0

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed += -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed += -7


    animation()

    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    
    #zeichnen des gerüstes
    screen.fill(color)
    pygame.draw.rect(screen,grau,player)
    pygame.draw.rect(screen,grau,opponent)
    pygame.draw.ellipse(screen, grau, ball)
    pygame.draw.aaline(screen,grau,(screen_width/2,0),(screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)