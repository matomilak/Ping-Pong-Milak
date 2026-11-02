print("Program sa spustil")

ball_x = 640
ball_y = 360
ball_radius = 30
ball_speed_x = -3
ball_speed_y = 2
rychlost_x = 3
rychlost_y = 2
paddle_x = 50
paddle_y = 300
paddle_width = 20
paddle_height = 180
paddle2_x = 1215
paddle2_y = 300
paddle2_width = 20
paddle2_height = 180
skore1 = 0
skore2 = 0
koniec_hry = False
menu = True

import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
print("Okno sa vykreslilo")
clock = pygame.time.Clock()
font = pygame.font.Font(None , 60)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and menu:
            if event.key == pygame.K_1:
                rychlost_x = 3
                rychlost_y = 2
                ball_speed_x = -3
                ball_speed_y = 2
                menu = False
            if event.key == pygame.K_2:
                rychlost_x = 5
                rychlost_y = 3
                ball_speed_x = -5
                ball_speed_y = 3
                menu = False
            if event.key == pygame.K_3:
                rychlost_x = 8
                rychlost_y = 5
                ball_speed_x = -8
                ball_speed_y = 5
                menu = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y -= 8
    if keys[pygame.K_s]:
        paddle_y += 8
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > 540:
        paddle_y = 540
    if keys[pygame.K_UP]:
        paddle2_y -= 8
    if keys[pygame.K_DOWN]:
        paddle2_y += 8
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > 540:
        paddle2_y = 540
    if not koniec_hry and not menu:
        ball_x += ball_speed_x
        ball_y += ball_speed_y
    if ball_y + ball_radius >= 720:
        ball_y = 720 - ball_radius
        ball_speed_y = -abs(ball_speed_y)
    if ball_y - ball_radius <= 0:
        ball_y = ball_radius
        ball_speed_y = abs(ball_speed_y)
    if ball_speed_x < 0 and ball_x - ball_radius <= paddle_x + paddle_width:
        if paddle_y <= ball_y <= paddle_y + paddle_height:
            ball_x = paddle_x + paddle_width + ball_radius
            ball_speed_x = abs(ball_speed_x)
    if ball_speed_x > 0 and ball_x + ball_radius >= paddle2_x:
        if paddle2_y <= ball_y <= paddle2_y + paddle2_height:
            ball_x = paddle2_x - ball_radius
            ball_speed_x = -abs(ball_speed_x)
    if ball_x + ball_radius < 0:
        skore2 += 1
        ball_x = 640
        ball_y = 360
        ball_speed_x = rychlost_x
        ball_speed_y = rychlost_y
    if ball_x - ball_radius > 1280:
        skore1 += 1
        ball_x = 640
        ball_y = 360
        ball_speed_x = -rychlost_x
        ball_speed_y = rychlost_y
    if skore1 >= 5 or skore2 >= 5:
        koniec_hry = True
    screen.fill("blue")
    if menu:
        nadpis2 = font.render("PING PONG", True, "white")
        vyber = font.render("VYBER SI OBTIAŽNOSŤ HRY!", True, "white")
        lahka = font.render("1 - ZAČIATOČNÍK", True, "green")
        stredna = font.render("2 - POKROČILÝ", True, "yellow")
        tazka = font.render("3 - PROFESIONÁL", True, "red")
        screen.blit(nadpis2, (480, 100))
        screen.blit(vyber, (380, 200))
        screen.blit(lahka, (480, 300))
        screen.blit(stredna, (480, 380))
        screen.blit(tazka, (480, 460))
    else:
        text_skore1 = font.render(str(skore1), True , "red")
        text_skore2 = font.render(str(skore2), True , "red")
        screen.blit(text_skore1, (400, 20))
        screen.blit(text_skore2, (700, 20))
        if koniec_hry:
            if skore1 >= 5:
                vitaz = "HRÁČ 1 VYHRAL!"
            else:
                vitaz = "HRÁČ 2 VYHRAL!"
            text_vitaz = font.render(vitaz, True, "white")
            screen.blit(text_vitaz, (500, 300))
    if not menu and not koniec_hry:
        pygame.draw.circle(screen, "white", (ball_x, ball_y), ball_radius)
        pygame.draw.rect(screen, "white", (paddle_x, paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, "white", (paddle2_x, paddle2_y, paddle2_width, paddle2_height))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
