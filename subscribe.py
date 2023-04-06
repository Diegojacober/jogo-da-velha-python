import random
from Game import Game

from paho.mqtt import client as mqtt_client

# broker = 'broker.emqx.io'
# port = 1883
# topic = "diegoalencar/jogo-da-velha"
# # generate client ID with pub prefix randomly
# client_id = f'broker-jogo'
# username = 'emqx'
# password = 'public'

broker = '10.21.160.16'
port = 1883
topic = "ets/jogo-da-velha-diego"
client_id = f'player-1'
username = 'emqx'
password = 'public'

jogo_da_velha = Game()
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        jogo_da_velha.render_frame()
        mensagem = msg.payload.decode().strip().split(';')
        conteudo = mensagem[0]
        user = mensagem[1]
        vez = mensagem[2]
        
        if vez == jogo_da_velha.vez:
           if jogo_da_velha.add_option(posicao=conteudo):
                win, winner = jogo_da_velha.check_win()
                if not win:
                    jogo_da_velha.render_frame()
                else:
                    print(f'The winner is {winner}')
                    exit()
           else:
               print(f'\033[04;31m O jogador {user} escolheu uma posição já ocupada\033[m')
        else:
            print(f'Jogador {user} tentou jogar na vez do outro player')
        
        print(f"Vez do jogador {jogo_da_velha.vez}")
     
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()