from umqtt.simple import MQTTClient
import config
import time

# Configurações do Broker Público
MQTT_BROKER    = "broker.hivemq.com"
MQTT_CLIENT_ID = "aquacontrol_si_001"
TOPICO_DADOS   = "aquacontrol/status"
TOPICO_COMANDO = "aquacontrol/comando"

client = None

def sub_cb(topic, msg):
    print(f"\n[MQTT] Comando recebido: {msg.decode()}")
    if msg == b"ALIMENTAR":
        import perifericos
        perifericos.acionar_alimentador(3)

def conectar_mqtt():
    global client
    try:
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
        client.set_callback(sub_cb)
        client.connect()
        client.subscribe(TOPICO_COMANDO)
        print("Conectado ao Broker MQTT!")
        return True
    except Exception as e:
        print("Erro ao conectar MQTT:", e)
        return False

def enviar_status(temp, vol):
    if client:
        try:
            msg = f"temp:{temp:.1f};vol:{vol:.1f}"
            client.publish(TOPICO_DADOS, msg)
            print(f"[MQTT] Enviado: {msg}")
        except:
            print("Falha ao enviar dados MQTT")

def verificar_mensagens():
    if client:
        try:
            client.check_msg()
        except:
            pass
