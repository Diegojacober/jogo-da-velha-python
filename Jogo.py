quadro = [
    {"a1": ' ', "b1" : 'X', "c1" : ' '},
    {"a2" : ' ', "b2" : 'O', "c2" : ' '},
    {"a3" : ' ', "b3" : ' ', "c3" : 'X'},
    ]

for item in quadro:
    print('| ',end='')
    for c,v in item.items():
        print(f'{v} |',end=' ')
    
    print()
#10.21.160.16
#1883
#ets
#12345