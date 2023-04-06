import random
import time

from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io'
# port = 1883
# topic = "diegoalencar/jogo-da-velha"
# client_id = f'player-2'
# username = 'emqx'
# password = 'public'

broker = '10.21.160.16'
port = 1883
topic = "ets/jogo-da-velha-diego"
client_id = f'player-1'
username = 'emqx'
password = 'public'

def connect_mqtt():
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


def publish(client):
    msg_count = 0
    msg = ""
    while True:
        time.sleep(1)
        print("\x1b[2J\x1b[1;1H", end="")
        while True:
            msg = input("Qual posição você deseja jogar?").strip().upper()[0:2]
            if msg[0:1] in 'ABC' and msg[1:2] in '123':
                msg = f"{msg};{client_id};O"
                result = client.publish(topic, msg)
                # result: [0, 1]
                status = result[0]
                if status == 0:
                    print(f"Enviando a posição")
                else:
                    print(f"Failed to send message to topic {topic}")
                msg_count += 1

                break
            else:
                print('\033[31m Posição inválida!! Digite apenas a linha(A, B, C) e em seguida a coluna(1, 2, 3) EXEMPLO: A3\033[m')
                continue
            
       

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()