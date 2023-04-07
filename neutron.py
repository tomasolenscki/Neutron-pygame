import pygame

WIDTH, HEIGHT = 800, 800
BORDA = 150
ROWS, COLS = 5, 5
SQUARE_SIZE = (WIDTH-BORDA)//COLS

# cores
RED = (250, 128, 114)
WHITE = (255, 255, 128)
BLACK = (0, 0, 0)
BLUE = (173,216,230)
GREEN = (144, 238, 144)
GREY = (108,108,108)

FPS = 60


# classe da peça
class Piece:
    PADDING = 20
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + BORDA/2 + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + BORDA/2 + SQUARE_SIZE // 2
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

# classe borda  

class Board:
    def __init__(self):
        self.board = []
        self.green_win = False
        self.blue_win = False  
        self.create_board()
    
    def draw_squares(self, win):
        win.fill((49, 46, 43))
        pygame.draw.rect(win,(118,150,86),(BORDA//2,BORDA//2,COLS*SQUARE_SIZE, ROWS*SQUARE_SIZE))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, (238,238,210), (row * SQUARE_SIZE + BORDA/2, col * SQUARE_SIZE + BORDA/2, SQUARE_SIZE, SQUARE_SIZE))
        fonte = 'ebrima'
        cor = (255, 255, 128)        
        largeFont = pygame.font.SysFont(fonte, 40)

        text = largeFont.render('A',True, cor)
        win.blit(text,(BORDA//2 + 1*SQUARE_SIZE//2 - text.get_width()//2, BORDA//2 + 5*SQUARE_SIZE + 10) )

        text = largeFont.render('B',True, cor)
        win.blit(text,(BORDA//2 + 3*SQUARE_SIZE//2 - text.get_width()//2, BORDA//2 + 5*SQUARE_SIZE + 10) )

        text = largeFont.render('C',True, cor)
        win.blit(text,(BORDA//2 + 5*SQUARE_SIZE//2 - text.get_width()//2, BORDA//2 + 5*SQUARE_SIZE + 10) )

        text = largeFont.render('D',True, cor)
        win.blit(text,(BORDA//2 + 7*SQUARE_SIZE//2 - text.get_width()//2, BORDA//2 + 5*SQUARE_SIZE + 10) )

        text = largeFont.render('E',True, cor)
        win.blit(text,(BORDA//2 + 9*SQUARE_SIZE//2 - text.get_width()//2, BORDA//2 + 5*SQUARE_SIZE + 10) )

        text = largeFont.render('5',True, cor)
        win.blit(text,(BORDA//2 - text.get_width() - 20, BORDA//2 + 1*SQUARE_SIZE//2 - text.get_height()//2) )

        text = largeFont.render('4',True, cor)
        win.blit(text,(BORDA//2 - text.get_width() - 20, BORDA//2 + 3*SQUARE_SIZE//2 - text.get_height()//2) )

        text = largeFont.render('3',True, cor)
        win.blit(text,(BORDA//2 - text.get_width() - 20, BORDA//2 + 5*SQUARE_SIZE//2 - text.get_height()//2) )

        text = largeFont.render('2',True, cor)
        win.blit(text,(BORDA//2 - text.get_width() - 20, BORDA//2 + 7*SQUARE_SIZE//2 - text.get_height()//2) )

        text = largeFont.render('1',True, cor)
        win.blit(text, (BORDA//2 - text.get_width()- 20, BORDA//2 + 9*SQUARE_SIZE//2 - text.get_height()//2) )



    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if piece.color == WHITE:
            if row == ROWS - 1:
                self.blue_win = True
            elif row == 0:
                self.green_win = True      

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col == 2 and row == 2:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row < 1:
                    self.board[row].append(Piece(row, col, GREEN))
                elif row > 3:
                    self.board[row].append(Piece(row, col, BLUE))
                else:
                    self.board[row].append(0)
            
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
        

    def winner(self):
        if self.green_win:
            return "GREEN wins"
        elif self.blue_win:
            return "BLUE wins"
        else:
            return None

    
    def get_valid_moves(self, piece):
        moves = {}
        col = piece.col
        row = piece.row

        #cima
        a = row
        numero_de_casas = 0
        while a > 0:
            a = a - 1
            # print(a,self.board[a][col])
            if self.board[a][col] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row - numero_de_casas,col] = []

        # print("cima:",numero_de_casas)

        #baixo
        b = row
        numero_de_casas = 0
        while b < 4:
            b = b + 1
            if self.board[b][col] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row + numero_de_casas,col] = []

        # print("direita:",numero_de_casas)

        #direita
        c = col
        numero_de_casas = 0
        while c > 0:
            c = c - 1
            if self.board[row][c] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row,col - numero_de_casas] = []

        #esquerda
        d = col
        numero_de_casas = 0
        while d < 4:
            d = d + 1
            if self.board[row][d] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row,col + numero_de_casas] = []       
    
        #diag_baixo_direita

        e = col
        f = row
        numero_de_casas = 0
        while e < 4 and f < 4:
            e = e + 1
            f = f + 1
            if self.board[f][e] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row + numero_de_casas,col + numero_de_casas] = []

        #diag_baixo_esquerda

        e = col
        f = row
        numero_de_casas = 0
        while e > 0 and f < 4:
            e = e - 1
            f = f + 1
            if self.board[f][e] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row + numero_de_casas,col - numero_de_casas] = []

        #diag_cima_direita

        e = col
        f = row
        numero_de_casas = 0
        while e < 4 and f > 0:
            e = e + 1
            f = f - 1
            if self.board[f][e] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row - numero_de_casas,col + numero_de_casas] = [] 

        #diag_cima_esquerda

        e = col
        f = row
        numero_de_casas = 0
        while e > 0 and f > 0:
            e = e - 1
            f = f - 1
            if self.board[f][e] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row - numero_de_casas,col - numero_de_casas] = []         

        return moves

# classe de regras do jogo 

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.neutron_moved = True
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece == 0:
            self.valid_moves = {}
            largar.play()
        # print("piece")
        if piece != 0 and piece.color == self.turn and self.neutron_moved:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            pegar.play()
            # print(self.valid_moves)
            return True
        elif piece != 0 and piece.color == WHITE and not self.neutron_moved:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            pegar.play()
            if self.valid_moves == {}:
                if self.turn == BLUE:
                    self.board.green_win = True
                elif self.turn == GREEN:
                    self.board.blue_win = True            
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            mover.play()
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED, (BORDA//2 + col * SQUARE_SIZE + SQUARE_SIZE//2 , BORDA//2 + row*SQUARE_SIZE + SQUARE_SIZE/2), SQUARE_SIZE/5 )

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == GREEN and self.neutron_moved:
            self.turn = BLUE
            self.neutron_moved = False
        elif self.turn == BLUE and self.neutron_moved:
            self.turn = GREEN
            self.neutron_moved = False
        elif self.turn == GREEN and not self.neutron_moved:
            self.turn = GREEN
            self.neutron_moved = True
        elif self.turn == BLUE and not self.neutron_moved:
            self.turn = BLUE
            self.neutron_moved = True

# Jogo em si

pygame.init()

file = 'tomasmusica2.wav'

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

pegar = pygame.mixer.Sound("pegar.wav")
mover = pygame.mixer.Sound("mover.wav")
fim = pygame.mixer.Sound("fim.wav")
comeco = pygame.mixer.Sound("comeco.wav")
largar = pygame.mixer.Sound("largar.wav")

pygame.mixer.music.load(file)
musica = pygame.mixer.music
musica.set_volume(0.1)
musica.play(loops = -1)

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
    comeco.play()

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            fim.play()
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