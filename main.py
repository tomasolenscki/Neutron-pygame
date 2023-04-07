import pygame
from neutron.constantes import WIDTH, HEIGHT, SQUARE_SIZE, RED, FPS, BORDA
from neutron.game import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Neutron')

def get_row_col_from_mouse(pos):
    x, y = pos
    if x > BORDA//2 and y > BORDA//2 and x < WIDTH - BORDA//2 and y < HEIGHT - BORDA//2:
        row = (y - BORDA//2) // SQUARE_SIZE
        col = (x - BORDA//2) // SQUARE_SIZE
        return row, col
    else:
        return 0,0

def end_screen(winner):
    fonte = 'ebrima'
    run2 = True


    Font = pygame.font.SysFont(fonte, 30)
    text3 = Font.render("Jogar novamente",True,(78,78,78) )
    textx = WIDTH/2 - text3.get_width()/2
    texty = HEIGHT/1.5
    textx_size = text3.get_width()
    texty_size = text3.get_height()

    while run2:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2= False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # if the user hits the mouse button
                x, y = event.pos
                if x >= textx - 5 and x <= textx + textx_size + 5:
                    if y >= texty - 5 and y <= texty + texty_size + 5:
                        run2 = False
                        main()
                        break 

        largeFont = pygame.font.SysFont(fonte, 80) # creates a font object
        if winner == "GREEN wins":
            cor = (124, 218, 124)
        elif winner == "BLUE wins":
            cor = (153,196,210)
        text = largeFont.render(winner,True, cor)
        text2 = largeFont.render(winner,True, (78,78,78))
        WIN.blit(text2,(WIDTH/2.03 - text.get_width()/2, HEIGHT/2.03 - text.get_height()/2) )
        WIN.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2) )
        WIN.blit(text3,(WIDTH/2 - text3.get_width()/2, HEIGHT/1.5) )

        pygame.display.update() 

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            end_screen(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()