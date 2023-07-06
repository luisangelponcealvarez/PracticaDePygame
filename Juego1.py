import pygame

pygame.init()

# colores
black = (0, 0, 0)
white = (255, 255, 255)
player_width = 15
player_height = 90

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

# Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

        # Modifica las coordenadas para dar mov. a los jugadores/ pelota
        player1_y_coor += player1_y_speed
        player2_y_coor += player2_y_speed

    screen.fill(black)
    # Zona de dibujo
    pygame.draw.rect(
        screen, white, (player1_x_coor, player1_y_coor, player_width, player_height)
    )
    pygame.draw.rect(
        screen, white, (player2_x_coor, player2_y_coor, player_width, player_height)
    )

    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
