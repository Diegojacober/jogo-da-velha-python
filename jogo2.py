import time

class Jogo:
    
    def __init__(self, player1='', player2=''):
        self.__player1 = player1
        self.__player2 = player2
        self.__option = 'X'
        self.__board = [
            {'A1': ' ', 'B1': ' ', 'C1': ' '},
            {'A2': ' ', 'B2': ' ', 'C2': ' '},
            {'A3': ' ', 'B3': ' ', 'C3': ' '} 
            ]
        
    
    def status(self):
        status = 'not connected'
        if self.__player1 in '' and self.__player1 in '':
            status = 'Nenhum Jogador conectado'
        elif self.__player1 not in '' and self.__player2 in '':
            status = 'Aguardando jogador 2'
        elif self.__player2 not in '' and self.__player1 in '':
            status = 'Aguardando jogador 1'
        elif self.__player2 not in '' and self.__player1 not in '':
            status = 'Preparado'
        
        return status
    
    @property
    def option(self):
        return self.__option       
    
    @property
    def player1(self):
        return self.__player1
    
    @player1.setter
    def player1(self, player1):
        self.__player1 = player1    
        
    @property
    def player2(self):
        return self.__player1
    
    @player2.setter
    def player2(self, player2):
        self.__player2 = player2    
        
        
    def render_board(self):
        print("\x1b[2J\x1b[1;1H", end="")
        for item in self.__board:
            print('| ',end='')
            for c,v in item.items():
                print(f' {v} |',end=' ')
            print()
    
    def add_option(self, pos):
        for linha in enumerate(self.__board):
            for line in linha[1]:
                if line == pos:
                    if self.__board[linha[0]][line] in 'XO':
                        print('\033[31m OPÇÃO INVÁLIDA\033[m')
                        time.sleep(1)
                    else:
                        self.__board[linha[0]][line] = self.__option
                        self.__option = 'O' if self.__option == 'X' else 'X'
                        
    def check_win(self):
        wins = [
            ['A1','A2','A3'],
            ['B1','B2','B3'],
            ['C1','C2','C3'],

            ['A1','B1','C1'],
            ['A2','B2','C2'],
            ['A3','B3','C3'],

            ['A1','B2','C3'],
            ['A3','B2','C1'],
            ['C1','B2','A3'],
            ['C3','B2','A1']
        ]
        
        onde_tem = [[],[]]
        
        for chave,item in enumerate(self.__board):
            for c,v in item.items():
                if v == 'O':
                    onde_tem[0].append(c)
                elif v == 'X':
                    onde_tem[1].append(c)
                    
        for tipo in wins:
            if tipo == onde_tem[0]:
                return True,'O'
            if tipo == onde_tem[1]:
                return True, 'X'
        return False, None
                        
                        
                    
        
def get_option():
     while True:
            try: 
                opc = input(f'Digite a o numero da posição deseja entre 1 e 9: ').strip()[0:1]
                opc = int(opc)
            except:
                print('\033[31mDigite apenas numeros\033[m')
            else:
                if opc > 0 and opc <= 9:
                    if opc == 1:
                        return 'A1'
                    elif opc == 2:
                        return 'B1'
                    elif opc == 3:
                        return 'C1'
                    elif opc == 4:
                        return 'A2'
                    elif opc == 5:
                        return 'B2'
                    elif opc == 6:
                        return 'C2'
                    elif opc == 7:
                        return 'A3'
                    elif opc == 8:
                        return 'B3'
                    elif opc == 9:
                        return 'C3'
                print('\033[31mDigite apenas um desses: 1, 2, 3, 4, 5, 6, 7, 8, 9\033[m')   
                continue


def play():
    jogo = Jogo(player1='', player2='i8h66h')
    status_jogo = jogo.status()
    
    if status_jogo == 'Preparado':
        jogo.render_board()

        while True:
            print(status_jogo)
            player = jogo.option
            if player == 'X':
                player = jogo.player1
            elif player == 'O':
                player = jogo.player2
                
                
            print(f'Vez do jogador {player}')
            finish, player = jogo.check_win()
            if not finish:
                posicao = get_option()
                time.sleep(1)
                jogo.add_option(posicao)
                jogo.render_board()
            else:
                print('acabou')
                exit()
    else:
        while True:
            print(status_jogo)
            time.sleep(2)
        
play()