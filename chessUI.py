
import math
import pygame
import os
import chess
import sys
import random

def index2pos(index):
    return (index%8,math.floor(index/8));

def pos2index(pos):
    return pos[0] + pos[1]*8;

def piece_by_symbol(pos, symb):
    if(symb == 'p' or symb == 'P'):
        return pawn(pos = pos, symbol = symb)
    if(symb == 'r' or symb == 'R'):
        return rook(pos = pos, symbol = symb)
    if(symb == 'b' or symb == 'B'):
        return bishop(pos = pos, symbol = symb)
    if(symb == 'n' or symb == 'N'):
        return knight(pos = pos, symbol = symb)
    if(symb == 'q' or symb == 'Q'):
        return queen(pos = pos, symbol = symb)
    if(symb == 'k' or symb == 'K'):
        return king(pos = pos, symbol = symb)
    
def back2front_move(bmove):
    letters = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7};
    pos1 = (letters[bmove[0]],int(bmove[1])-1)
    pos2 = (letters[bmove[2]],int(bmove[3])-1)
    return pos1, pos2


class pawn:
symbol = None;
pos = (0,0);
team = -1;
spritesheet = (pygame.image.load("chesspieces.png"),45);
spriteIndex = (5,6+5);

def __init__(self,pos = (4,6),symbol = 'p'):
    
    if(symbol != 'p' and symbol != 'P'):
        raise ValueError('Invalid symbol when declaring a pawn.')
        
    self.pos = pos;
    self.symbol = symbol;
    if symbol == 'p':
        self.team = -1;
    else: self.team = 0;

def move_to(self,pos):
    self.pos = pos;
    
def render(self,display,box_size):
    p = self;
    s = self.spritesheet;
    display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                    ((p.spriteIndex[p.team]%6)*s[1],
                    math.floor(p.spriteIndex[p.team]/6)*s[1],
                    s[1],s[1]));



class rook:
    symbol = None;
    pos = (0,0);
    team = -1;
    spritesheet = (pygame.image.load("chesspieces.png"),45);
    spriteIndex = (4,6+4);
    
    def __init__(self,pos = (4,6),symbol = 'r'):
        
        if(symbol != 'r' and symbol != 'R'):
            raise ValueError('Invalid symbol when declaring a rook.')
            
        self.pos = pos;
        self.symbol = symbol;
        if symbol == 'r':
            self.team = -1;
        else: self.team = 0;
    
    def move_to(self,pos):
        self.pos = pos;
        
    def render(self,display,box_size):
        p = self;
        s = self.spritesheet;
        display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                     ((p.spriteIndex[p.team]%6)*s[1],
                      math.floor(p.spriteIndex[p.team]/6)*s[1],
                      s[1],s[1]));


class bishop:
    symbol = None;
    pos = (0,0);
    team = -1;
    spritesheet = (pygame.image.load("chesspieces.png"),45);
    spriteIndex = (2,6+2);
    
    def __init__(self,pos = (4,6),symbol = 'b'):
        
        if(symbol != 'b' and symbol != 'B'):
            raise ValueError('Invalid symbol when declaring a bishop.')
            
        self.pos = pos;
        self.symbol = symbol;
        if symbol == 'b':
            self.team = -1;
        else: self.team = 0;
    
    def move_to(self,pos):
        self.pos = pos;
        
    def render(self,display,box_size):
        p = self;
        s = self.spritesheet;
        display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                     ((p.spriteIndex[p.team]%6)*s[1],
                      math.floor(p.spriteIndex[p.team]/6)*s[1],
                      s[1],s[1]));



class knight:
    symbol = None;
    pos = (0,0);
    team = -1;
    spritesheet = (pygame.image.load("chesspieces.png"),45);
    spriteIndex = (3,6+3);
    
    def __init__(self,pos = (4,6),symbol = 'n'):
        
        if(symbol != 'n' and symbol != 'N'):
            raise ValueError('Invalid symbol when declaring a knight.')
            
        self.pos = pos;
        self.symbol = symbol;
        if symbol == 'n':
            self.team = -1;
        else: self.team = 0;
    
    def move_to(self,pos):
        self.pos = pos;
        
    def render(self,display,box_size):
        p = self;
        s = self.spritesheet;
        display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                     ((p.spriteIndex[p.team]%6)*s[1],
                      math.floor(p.spriteIndex[p.team]/6)*s[1],
                      s[1],s[1]));



class queen:
    symbol = None;
    pos = (0,0);
    team = -1;
    spritesheet = (pygame.image.load("chesspieces.png"),45);
    spriteIndex = (1,6+1);
    
    def __init__(self,pos = (4,6),symbol = 'q'):
        
        if(symbol != 'q' and symbol != 'Q'):
            raise ValueError('Invalid symbol when declaring a queen.')
            
        self.pos = pos;
        self.symbol = symbol;
        if symbol == 'q':
            self.team = -1;
        else: self.team = 0;
    
    def move_to(self,pos):
        self.pos = pos;
        
    def render(self,display,box_size):
        p = self;
        s = self.spritesheet;
        display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                     ((p.spriteIndex[p.team]%6)*s[1],
                      math.floor(p.spriteIndex[p.team]/6)*s[1],
                      s[1],s[1]));


class king:
    symbol = None;
    pos = (0,0);
    team = -1;
    spritesheet = (pygame.image.load("chesspieces.png"),45);
    spriteIndex = (0,6);
    
    def __init__(self,pos = (4,6),symbol = 'k'):
        
        if(symbol != 'k' and symbol != 'K'):
            raise ValueError('Invalid symbol when declaring a king.')
            
        self.pos = pos;
        self.symbol = symbol;
        if symbol == 'k':
            self.team = -1;
        else: self.team = 0;
    
    def move_to(self,pos):
        self.pos = pos;
        
    def render(self,display,box_size):
        p = self;
        s = self.spritesheet;
        display.blit(s[0],(p.pos[0]*box_size + 9,p.pos[1]*box_size + 9),
                     ((p.spriteIndex[p.team]%6)*s[1],
                      math.floor(p.spriteIndex[p.team]/6)*s[1],
                      s[1],s[1]));



class board:
    board = [None for i in range(64)]; 
    box_size = 64;
    background = pygame.image.load("bg3.gif");
    back = chess.Board();
    whites_turn = True;

    def __init__(self):
        pass
    
    def setup(self):
        self.board[0] = pawn(pos = (0,0),symbol = 'p');
        
    def setup_normal(self):
        self.back = chess.Board()
        self.sync_with_backend()
    
    def get_piece_at(self,pos):
        return self.board[pos2index(pos)];
    
    def move(self,pos1,pos2):
        b1 = self.board[pos2index(pos1)];
        b1.move_to(pos2)
        self.board[pos2index(pos2)] = b1;
        self.board[pos2index(pos1)] = None;
    
        
    def render_all(self,display):
        for item in self.board:
            if item != None:
                p = item
                p.render(display,self.box_size);
    
    
    def by_symbol(self):
        result = {}
        for i,item in enumerate(self.board):
            if item != None:
                result[i] = item.symbol
        return result
    
    def update_backend(self,verbose = False):
        D = self.by_symbol()
        new_dict = {}
        for key, value in D.items():
            new_dict[key] = chess.Piece.from_symbol(value)
        self.back.set_piece_map(new_dict)
        self.back.turn = not self.back.turn
        
        
        if(verbose):
            print()
            print(self.back)
            print("Turn: {}".format(self.back.turn))
            print()
    
    
    def get_legal_moves(self):
        LM = []
        for move in self.back.legal_moves:
            LM.append(back2front_move(move.uci()))
        return(LM)

    
    def get_back_moves(self):
        LM = []
        for move in self.back.legal_moves:
            LM.append(move)
        return(LM)
    
    
    
    def sync_with_backend(self):
        self.board = [None for i in range(64)];
        new_dict = self.back.piece_map()
        for key, value in new_dict.items():
            self.board[key] = piece_by_symbol(index2pos(key),'{}'.format(value))
        
        if(self.back.turn):self.whites_turn = True;
        else: self.whites_turn = False;



class bot:
    name = "";
    board = None
    
    def __init__(self, name = 'Egil', board = None):
        self.name = name
        self.board = board
    
    
    def get_move(self):
        LM = self.board.get_legal_moves()
        choice = random.randint(0,len(LM)-1)
        
        for i,move in enumerate(LM):
            back_move = self.board.get_back_moves()[i]
            if(self.board.back.gives_check(back_move)):
                coice = i
            
            
        return LM[choice]



def main():
    pygame.init()
    pygame.display.list_modes()
    

    b = board()
    b.setup_normal()
    
    screenSize = 512,512;
    box_size = screenSize[0]/8;
    display = pygame.display.set_mode(screenSize);
    pygame.display.set_caption("El sjakk");
    pygame.display.update()
    
    piece_in_hand = None;
    
    Egil = bot(board = b)
    
    print(b.get_legal_moves())
    
    Game = True;
    
    while Game:
        display.fill((0,0,0));
        display.blit(b.background,(0,0),(0,0,512,512));
        b.render_all(display)
        pygame.display.update();
        
        if(b.back.is_game_over()):
            print("GAME OVER: {} won".format(not b.whites_turn))
            Game = False;
        
        if(b.whites_turn):
            pygame.display.set_caption("Chess - turn: white");
        
        else:
            pygame.display.set_caption("Chess - turn: black");
        
        
        if(not b.whites_turn):
            pos1, pos2 = Egil.get_move()
            
            
            b.move(pos1,pos2);
            b.update_backend()
            b.sync_with_backend()

            display.fill((0,0,0));
            display.blit(b.background,(0,0),(0,0,512,512));
            b.render_all(display)
            pygame.display.update();
            
            
        
        else:
            turn_done = False;
            
            while(not turn_done):    
                mPos = pygame.mouse.get_pos();
                for evt in pygame.event.get():

                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        Game = False


                    if(evt.type == 5):
                        i1 = b.get_piece_at(pos = (int(mPos[0]/box_size),int(mPos[1]/box_size)));
                        if i1 != None:
                            mOffset = (int(mPos[0]%45),int(mPos[1]%45));
                            piece_in_hand = i1;


                    if(evt.type == 6 and piece_in_hand != None):
                        if((piece_in_hand.pos,(int(mPos[0]/box_size),int(mPos[1]/box_size))) in b.get_legal_moves()):
                            b.move(piece_in_hand.pos,(int(mPos[0]/box_size),int(mPos[1]/box_size)));
                            b.update_backend()
                            b.sync_with_backend()
                            piece_in_hand = None;

                            display.fill((0,0,0));
                            display.blit(b.background,(0,0),(0,0,512,512));

                            b.render_all(display)

                            pygame.display.update();

                            turn_done = True;
                        else:
                            print("illegal move, try again")



if __name__ == "__main__":
    main()
  