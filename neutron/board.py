import pygame
from .constantes import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, BLUE, GREEN, BORDA, WIDTH, HEIGHT
from .piece import Piece

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
                self.green_win = True
            elif row == 0:
                self.blue_win = True      

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
            print(a,self.board[a][col])
            if self.board[a][col] == 0:
                numero_de_casas += 1
            else:
                break
        
        if numero_de_casas == 0:
            pass
        else:
            moves[row - numero_de_casas,col] = []

        print("cima:",numero_de_casas)

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

        print("direita:",numero_de_casas)

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
    
