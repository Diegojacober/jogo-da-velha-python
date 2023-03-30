import time

quadro = [
    {"A1": ' ', "B1" : ' ', "C1" : ' '},
    {"A2" : ' ', "B2" : ' ', "C2" : ' '},
    {"A3" : ' ', "B3" : ' ', "C3" : ' '},
    ]

def render_quadro():
    print("\x1b[2J\x1b[1;1H", end="")
    for item in quadro:
        print('| ',end='')
        for c,v in item.items():
            print(f' {v} |',end=' ')
        print()

def get_option():
    while True:
        opc = input(f'Digite a posição ({vez})').upper()[0:2]
        if opc[0:1] in 'ABC' and opc[1:2] in '123':
            return opc
        print('\033[31mDigite apenas um desses: A1, A2, A3, B1, B2, B3, C1, C2, C3\033[m')
    
def add_option(posicao, opcao):
    for chave,item in enumerate(quadro):
        for c,v in item.items():
            if c == posicao:
               if quadro[chave][c] in 'XO':
                  return False
               else:
                   quadro[chave][c] = opcao
                   return True
    
def check_win():
    wins = [
        ['A1','A2','A3'],
        ['B1','B2','B3'],
        ['C1','C2','C3'],

        ['A1','B1','C1'],
        ['A2','B2','C2'],
        ['A3','B3','C3'],

        ['A1','B2','C3'],
        ['A3','B2','C1']
    ]
    
    onde_tem = [[],[]]
    
    for chave,item in enumerate(quadro):
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
    
    
    
vez = 'X'
cont = 1
while True:
    render_quadro()
    ganhou, ganhador = check_win()
    if not ganhou:
        opc = get_option()
        
        if not add_option(posicao=opc,opcao=vez):
            print('\033[31mVocê não pode adicionar nessa posição\033[m')
            time.sleep(1.5)
        else:
            print('\033[32mAdicionado com sucesso! \033[m')
            time.sleep(1)
            vez = 'O' if vez == 'X' else 'X'
    else: 
        print(f'O vencedor foi o {ganhador}')
        break
    
    
    
#10.21.160.16
#1883
#ets
#12345