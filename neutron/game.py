import pygame
from .constantes import RED, WHITE, BLUE, SQUARE_SIZE, GREEN, BORDA
from neutron.board import Board

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
        print("piece")
        if piece != 0 and piece.color == self.turn and self.neutron_moved:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            print(self.valid_moves)
            return True
        elif piece != 0 and piece.color == WHITE and not self.neutron_moved:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
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
