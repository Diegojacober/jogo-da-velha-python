import time

class Game:
    
    def __init__(self) -> None:
        self.__quadro = [{"A1": ' ', "B1" : ' ', "C1" : ' '}, {"A2" : ' ', "B2" : ' ', "C2" : ' '},{"A3" : ' ', "B3" : ' ', "C3" : ' '}]
        self.__vez = 'X'
        
    @property
    def vez(self):
        return self.__vez    
    
    def render_frame(self):
        print("\x1b[2J\x1b[1;1H", end="")
        for item in self.__quadro:
            print('| ',end='')
            for c,v in item.items():
                print(f' {v} |',end=' ')
            print()
            
    def __get_option(self):
        while True:
            opc = input(f'Digite a posição ({self.__vez})').upper()[0:2]
            if opc[0:1] in 'ABC' and opc[1:2] in '123':
                return opc
            print('\033[31mDigite apenas um desses: A1, A2, A3, B1, B2, B3, C1, C2, C3\033[m')
            
    def add_option(self,posicao):
        for chave,item in enumerate(self.__quadro):
            for c,v in item.items():
                if c == posicao:
                    if self.__quadro[chave][c] in 'XO':
                        return False
                    else:
                        self.__quadro[chave][c] = self.__vez
                        self.__vez = 'O' if self.__vez == 'X' else 'X'
                        return True
                
    def next_player(self, player):
        if player == 'O':
            return 'X'
        elif player == 'X':
            return 'O'
        
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
            ['C1','B2','A3']
        ]
        
        onde_tem = [[],[]]
        
        for chave,item in enumerate(self.__quadro):
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
    
    def play(self):
        while True:
            self.render_frame()
            ganhou, ganhador = self.check_win()
            if not ganhou:
                opc = self.__get_option()
                
                if not self.add_option(posicao=opc):
                    print('\033[31mVocê não pode adicionar nessa posição\033[m')
                    time.sleep(1.5)
                else:
                    print('\033[32mAdicionado com sucesso! \033[m')
                    time.sleep(1)
            else: 
                print(f'\033[32mO vencedor foi o {ganhador}\033[m')
                break
            
            
if __name__ == '__main__':
    jogo_da_velha = Game()
    


    jogo_da_velha.play()